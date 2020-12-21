from web_server import Server, Handler
from display import Display

display = Display()


def on_upload():
    display.show_latest()


if __name__ == "__main__":
    display.show_latest()
    myServer = Server(on_upload, ("0.0.0.0", 8000), Handler)

    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass
