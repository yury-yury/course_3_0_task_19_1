import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

host = "localhost"
port = 8000


class MyServer(BaseHTTPRequestHandler):

    def _get_html(self, fail_path):
        with open(fail_path, 'r', encoding='utf-8') as file:
            html_code = file.read()
        return html_code

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        page_content = self._get_html('./templates/page_2.html')
        # json_content = json.dumps({'version': '1.0', 'name': 'Ping-Pong server'})

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((host, port), MyServer)
    print(f"Server started http://{host}:{port}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
