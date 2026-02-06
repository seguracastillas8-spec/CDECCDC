"""Simple static server for the CDE document site."""

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

HOST = "0.0.0.0"
PORT = 8000


class NoCacheRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def main() -> None:
    with TCPServer((HOST, PORT), NoCacheRequestHandler) as httpd:
        print(f"Serving on http://{HOST}:{PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
