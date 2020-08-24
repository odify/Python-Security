import ssl

import BaseHTTPServer, SimpleHTTPServer


httpd = BaseHTTPServer.HTTPServer(('localhost', XXXX), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./server.pem', server_side=True)
httpd.serve_forever()
