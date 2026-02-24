from __future__ import annotations

import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from service import ComputeRentalService

service = ComputeRentalService()


class DemoHandler(BaseHTTPRequestHandler):
    def _json(self, code: int, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self) -> dict:
        length = int(self.headers.get("Content-Length", "0"))
        if length == 0:
            return {}
        return json.loads(self.rfile.read(length).decode("utf-8"))

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path == "/api/v1/plans":
            self._json(HTTPStatus.OK, {"items": service.list_plans()})
            return
        if parsed.path == "/api/v1/rentals":
            self._json(HTTPStatus.OK, {"items": service.list_rentals()})
            return
        if parsed.path == "/api/v1/dashboard":
            self._json(HTTPStatus.OK, service.dashboard())
            return

        self._json(HTTPStatus.NOT_FOUND, {"error": "未找到接口"})

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)

        try:
            if parsed.path == "/api/v1/customers":
                data = self._read_json()
                result = service.create_customer(data["name"], data["email"])
                self._json(HTTPStatus.CREATED, result)
                return

            if parsed.path == "/api/v1/rentals":
                data = self._read_json()
                result = service.create_rental(data["customer_id"], data["plan_id"])
                self._json(HTTPStatus.CREATED, result)
                return

            parts = [p for p in parsed.path.split("/") if p]
            if len(parts) == 5 and parts[:3] == ["api", "v1", "rentals"] and parts[4] == "start":
                result = service.start_rental(parts[3])
                self._json(HTTPStatus.OK, result)
                return

            if len(parts) == 5 and parts[:3] == ["api", "v1", "rentals"] and parts[4] == "stop":
                params = parse_qs(parsed.query)
                hours = params.get("hours", [None])[0]
                result = service.stop_rental(parts[3], hours=hours)
                self._json(HTTPStatus.OK, result)
                return

            self._json(HTTPStatus.NOT_FOUND, {"error": "未找到接口"})
        except (KeyError, json.JSONDecodeError):
            self._json(HTTPStatus.BAD_REQUEST, {"error": "请求参数错误"})
        except ValueError as exc:
            self._json(HTTPStatus.BAD_REQUEST, {"error": str(exc)})


def run() -> None:
    server = ThreadingHTTPServer(("0.0.0.0", 8000), DemoHandler)
    print("Compute rental demo backend running at http://127.0.0.1:8000")
    server.serve_forever()


if __name__ == "__main__":
    run()
