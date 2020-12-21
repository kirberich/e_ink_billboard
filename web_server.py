from http.server import BaseHTTPRequestHandler, HTTPServer
from display import Display

display = Display()


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        with open("latest", "wb") as f:
            length = self.headers["content-length"]
            data = self.rfile.read(int(length))
            f.write(data)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.server.on_upload()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            bytes("<html><head><title>Title goes here.</title></head>", "utf-8")
        )
        self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


class Server(HTTPServer):
    def __init__(self, on_upload, *args, **kwargs):
        self.on_upload = on_upload
        super().__init__(*args, **kwargs)
