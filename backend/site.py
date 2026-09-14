from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/data':
            data = {
                'message': 'Привет от бэкенда!',
                'items': ['Python', 'JavaScript', 'HTTP-сервер', 'HTML']
            }
            response = json.dumps(data).encode('utf-8')

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(response)
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('localhost', 5000), MyHandler)
    print('Сервер запущен на http://localhost:5000')
    print('Доступен эндпоинт: http://localhost:5000/api/data')
    server.serve_forever()