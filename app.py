from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

print("Server running on port", PORT)

server = HTTPServer(('', PORT), SimpleHTTPRequestHandler)
server.serve_forever()
