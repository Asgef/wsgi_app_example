from wsgiref.simple_server import make_server


def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])


httpd = make_server('', 8000, app)
print("Serving on port 8000...")
httpd.serve_forever()