from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        subprocess.run(["/bin/bash", "/home/ubuntu/dev/SRE_final/webhook_handler.sh"])

server_address = ('', 8000)
httpd = HTTPServer(server_address, WebhookHandler)
httpd.serve_forever()
