"""Vérifie que chaque page du site respecte le budget publié dans la déclaration d'écoconception.

Usage : python3 scripts/check-budget.py public [--chrome COMMANDE]

À lancer sur le site tel qu'il sera publié, après purge-css.py et subset-icons.py. Le script sert
le dossier en local, compressé en gzip comme par GitHub Pages, puis ouvre chaque page dans Chrome,
cache désactivé, en 1 366 × 768 et 390 × 844, et la fait défiler jusqu'en bas. Il relève le nombre
de requêtes, le poids transféré et le nombre d'éléments du DOM, et échoue si une page dépasse le
budget.

Les pages appellent certains fichiers par leur adresse publique (https://…) : Chrome les demande
au serveur local, sans que la page voie la différence.

Dépendance : websocket-client (pip install websocket-client), et Chrome ou Chromium installé.
"""
import argparse
import gzip
import http.server
import json
import mimetypes
import os
import re
import shlex
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time
import urllib.parse
import urllib.request

import websocket

# Budget publié dans la section « Budget par page » de la déclaration d'écoconception
BUDGET = {"poids": 100 * 1024, "requêtes": 10, "DOM": 1500}
VIEWPORTS = [(1366, 768), (390, 844)]
# GitHub Pages compresse en gzip de niveau 5 (mêmes tailles à l'octet près), sauf ces formats
GZIP_LEVEL = 5
PRECOMPRESSED = {".avif", ".gif", ".jpeg", ".jpg", ".mp4", ".pdf", ".png", ".webm", ".webp", ".woff", ".woff2", ".zip"}
CHROMES = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser"]
# Défilement par pas de deux écrans : Chrome charge les images différées dès qu'elles
# approchent à moins de 1 250 px de l'écran, aucune n'est donc sautée
SCROLL = """(async () => {
  for (let y = 0; y < document.documentElement.scrollHeight; y += 2 * innerHeight) {
    scrollTo(0, y);
    await new Promise(r => setTimeout(r, 20));
  }
  scrollTo(0, document.documentElement.scrollHeight);
  return true;
})()"""

mimetypes.add_type("application/manifest+json", ".webmanifest")
mimetypes.add_type("font/woff2", ".woff2")


def free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def serve(root, prefix):
    """Sert `root` sous le chemin `prefix`, comme GitHub Pages (index.html, 404.html, gzip)."""
    bodies = {}

    def body(path):
        if path not in bodies:
            with open(path, "rb") as f:
                data = f.read()
            compress = os.path.splitext(path)[1].lower() not in PRECOMPRESSED
            bodies[path] = (gzip.compress(data, GZIP_LEVEL) if compress else data, compress)
        return bodies[path]

    class Handler(http.server.BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def do_GET(self):
            path = urllib.parse.unquote(urllib.parse.urlsplit(self.path).path)
            status, file = 404, os.path.join(root, "404.html")
            if path.startswith(prefix):
                local = os.path.normpath(os.path.join(root, path[len(prefix):]))
                if os.path.isdir(local) and not path.endswith("/"):
                    self.send_response(301)
                    self.send_header("Location", path + "/")
                    self.send_header("Content-Length", "0")
                    self.end_headers()
                    return
                if os.path.isdir(local):
                    local = os.path.join(local, "index.html")
                if local.startswith(root) and os.path.isfile(local):
                    status, file = 200, local
            data, compressed = body(file)
            self.send_response(status)
            self.send_header("Content-Type", mimetypes.guess_type(file)[0] or "application/octet-stream")
            if compressed:
                self.send_header("Content-Encoding", "gzip")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def log_message(self, *args):
            pass

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


class Chrome:
    """Chrome sans interface, piloté par le protocole DevTools."""

    def __init__(self, command, site_origin, local_origin):
        self.site_origin, self.local_origin = site_origin, local_origin
        self.profile = tempfile.mkdtemp()
        port = free_port()
        self.process = subprocess.Popen(
            shlex.split(command) + ["--headless=new", f"--remote-debugging-port={port}",
                                    f"--user-data-dir={self.profile}", "--no-first-run",
                                    "--no-default-browser-check", "about:blank"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(100):
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/version") as r:
                    url = json.load(r)["webSocketDebuggerUrl"]
                break
            except OSError:
                time.sleep(0.2)
        else:
            sys.exit(f"Chrome ne répond pas : {command}")
        self.ws = websocket.create_connection(url, suppress_origin=True, max_size=None)
        self.last_id = 0
        self.events = []

    def post(self, method, params=None, session=None):
        self.last_id += 1
        message = {"id": self.last_id, "method": method, "params": params or {}}
        if session:
            message["sessionId"] = session
        self.ws.send(json.dumps(message))
        return self.last_id

    def receive(self, timeout=None):
        self.ws.settimeout(timeout)
        try:
            message = json.loads(self.ws.recv())
        except websocket.WebSocketTimeoutException:
            return None
        if message.get("method") == "Fetch.requestPaused":
            # Requête vers l'adresse publique du site : la servir depuis le build local
            params = message["params"]
            self.post("Fetch.continueRequest", {
                "requestId": params["requestId"],
                "url": self.local_origin + params["request"]["url"][len(self.site_origin):]},
                message["sessionId"])
        elif "method" in message:
            self.events.append(message)
        return message

    def send(self, method, params=None, session=None):
        sent = self.post(method, params, session)
        while True:
            message = self.receive()
            if message.get("id") == sent:
                if "error" in message:
                    raise RuntimeError(f"{method} : {message['error']}")
                return message.get("result", {})

    def wait_for(self, done, timeout):
        end = time.time() + timeout
        while not done() and time.time() < end:
            self.receive(0.1)

    def close(self):
        try:
            self.send("Browser.close")
            self.process.wait(10)
        except Exception:
            self.process.kill()
        shutil.rmtree(self.profile, ignore_errors=True)


def measure(chrome, url, width, height):
    """Requêtes, octets transférés et éléments du DOM d'une page, au premier chargement."""
    chrome.events.clear()
    context = chrome.send("Target.createBrowserContext", {"disposeOnDetach": True})["browserContextId"]
    target = chrome.send("Target.createTarget", {"url": "about:blank", "browserContextId": context})["targetId"]
    s = chrome.send("Target.attachToTarget", {"targetId": target, "flatten": True})["sessionId"]
    chrome.send("Fetch.enable", {"patterns": [{"urlPattern": chrome.site_origin + "/*"}]}, s)
    chrome.send("Network.enable", {}, s)
    chrome.send("Network.setCacheDisabled", {"cacheDisabled": True}, s)
    chrome.send("Page.enable", {}, s)
    chrome.send("Emulation.setDeviceMetricsOverride",
                {"width": width, "height": height, "deviceScaleFactor": 1, "mobile": width < 600}, s)

    def seen(method):
        return [e["params"] for e in chrome.events if e.get("sessionId") == s and e["method"] == method]

    def idle(quiet=0.2, timeout=10):
        end, calm = time.time() + timeout, time.time()
        while time.time() < end:
            chrome.receive(0.05)
            ended = {p["requestId"] for p in seen("Network.loadingFinished") + seen("Network.loadingFailed")}
            if {p["requestId"] for p in seen("Network.requestWillBeSent")} - ended:
                calm = time.time()
            elif time.time() - calm > quiet:
                return

    chrome.send("Page.navigate", {"url": url}, s)
    chrome.wait_for(lambda: seen("Page.loadEventFired"), 30)
    idle()
    chrome.send("Runtime.evaluate", {"expression": SCROLL, "awaitPromise": True}, s)
    idle()
    dom = chrome.send("Runtime.evaluate", {
        "expression": "document.getElementsByTagName('*').length", "returnByValue": True}, s)["result"]["value"]
    requests = [p for p in seen("Network.requestWillBeSent") if not p["request"]["url"].startswith(("data:", "blob:"))]
    size = sum(p["encodedDataLength"] for p in seen("Network.loadingFinished"))
    chrome.send("Target.disposeBrowserContext", {"browserContextId": context})
    return {"poids": size, "requêtes": len(requests), "DOM": dom}


def site_url(root):
    """Adresse publique du site, lue dans le sitemap (la plus courte est l'accueil)."""
    with open(os.path.join(root, "sitemap.xml"), encoding="utf-8") as f:
        return min(re.findall(r"<loc>([^<]+)</loc>", f.read()), key=len)


def pages(root):
    for dirpath, _, files in os.walk(root):
        for name in files:
            if name.endswith(".html"):
                path = os.path.relpath(os.path.join(dirpath, name), root).replace(os.sep, "/")
                yield path[:-len("index.html")] if name == "index.html" else path


def show(metric, value):
    return f"{value / 1024:.1f} Ko" if metric == "poids" else str(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("root", nargs="?", default="public")
    parser.add_argument("--chrome", help="commande qui lance Chrome ou Chromium")
    args = parser.parse_args()
    root = os.path.abspath(args.root)
    command = args.chrome or next((c for c in CHROMES if shutil.which(c)), None)
    if not command:
        sys.exit("Chrome ou Chromium introuvable : préciser --chrome")

    base = site_url(root)
    origin = "{0.scheme}://{0.netloc}".format(urllib.parse.urlsplit(base))
    prefix = urllib.parse.urlsplit(base).path or "/"
    server = serve(root, prefix)
    chrome = Chrome(command, origin, f"http://127.0.0.1:{server.server_address[1]}")

    github = os.environ.get("GITHUB_ACTIONS")
    worst, over = {m: (0, None) for m in BUDGET}, 0
    try:
        for page in sorted(pages(root)):
            for width, height in VIEWPORTS:
                result = measure(chrome, base + page, width, height)
                label = f"/{page} ({width} × {height})"
                for metric, value in result.items():
                    if value > worst[metric][0]:
                        worst[metric] = (value, label)
                exceeded = [m for m in BUDGET if result[m] > BUDGET[m]]
                if exceeded:
                    over += 1
                    detail = ", ".join(f"{m} {show(m, result[m])} (budget {show(m, BUDGET[m])})" for m in exceeded)
                    print(("::error title=Budget par page dépassé::" if github else "Budget dépassé : ")
                          + f"{label} : {detail}")
    finally:
        chrome.close()
        server.shutdown()

    lines = [f"| {m} | {show(m, BUDGET[m])} | {show(m, value)} | {label} |" for m, (value, label) in worst.items()]
    print("\n".join(["Maximum mesuré par critère :"] + lines))
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
            f.write("### Budget par page\n\n| | Budget | Maximum mesuré | Page |\n|---|---:|---:|---|\n"
                    + "\n".join(lines) + "\n")
    if over:
        sys.exit(f"{over} mesure(s) au-delà du budget")


if __name__ == "__main__":
    main()
