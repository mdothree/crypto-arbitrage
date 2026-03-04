#!/usr/bin/env python3
"""
Crypto Arbitrage

Cryptocurrency arbitrage trading
"""

import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

PORT = int(os.environ.get("PORT", 10000))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        response = {
            "service": "crypto_arbitrage",
            "status": "running",
            "message": "Cryptocurrency arbitrage trading"
        }
        self.wfile.write(json.dumps(response).encode())

    def log_message(self, format, *args):
        print(f"[crypto_arbitrage] {args[0]}")


if __name__ == "__main__":
    print(f"Starting crypto_arbitrage on port {PORT}")
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()
