from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import logging

logging.basicConfig(filename='/home/ubuntu/dev/SRE_final/webhook_server.log', level=logging.INFO)

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        logging.info("Webhook received!")
        result = subprocess.run(["/bin/bash", "/home/ubuntu/dev/SRE_final/webhook_handler.sh"], capture_output=True, text=True)
        logging.info(result.stdout)
        logging.error(result.stderr)

server_address = ('', 8000)
httpd = HTTPServer(server_address, WebhookHandler)
httpd.serve_forever()
