import socket
import os
import mimetypes
from template import Template

def tcp_server():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 8080
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen()
    print('Listen on http://127.0.0.1:8080')

    while True:
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024).decode()
        print('Request : %s' % request)

        if request and request.strip():
            response = handle_request(request)
            client_connection.sendall(response)
        client_connection.close()
    server_socket.close()

def handle_request(request):
    request_message = request.split("\r\n")
    request_line = request_message[0]
    words = request_line.split()
    method = words[0]
    uri = words[1].strip("/")
    http_version = words[2]

    http_version = words[2]
    if(uri == ''):
        uri = "index.html"
    if(method == "GET"):
        response = handle_get(uri, http_version)
    if(method =="POST"):
        data = request_message[len(request_message)-1]
        response = handle_post(uri, http_version, data)
    return response

def handle_get(uri, http_version):
    uri = "htdocs/%s" % uri

    if os.path.exists(uri) and not os.path.isdir(uri):
        response_line = b'HTTP/1.1 200 OK\r\n'
        content_type = mimetypes.guess_type(uri)[0] or 'text/html'
        entity_header = b'Content-Type: ' + content_type.encode() + b'\r\n\r\n'

        with open(uri, 'rb') as file:
            message_body = file.read()

        return b''.join([response_line, entity_header, message_body])
    else:
        response_line = b'HTTP/1.1 404 Not Found\r\n'
        entity_header = b'Content-Type: text/html\r\n\r\n'
        message_body = b'<h1>404 Not Found</h1>'

        return b''.join([response_line, entity_header, message_body])

def handle_post(uri, http_version, data):
    uri = "htdocs/%s" % uri

    if os.path.exists(uri) and not os.path.isdir(uri):
        response_line = b'HTTP/1.1 200 OK\r\n'
        content_type = mimetypes.guess_type(uri)[0] or 'text/html'
        entity_header = b'Content-Type: ' + content_type.encode() + b'\r\n\r\n'

        with open(uri, 'r') as file:
            html = file.read()

        _POST = {}
        for item in data.split("&"):
            key, value = item.split("=")
            _POST[key] = value

        context = {'_POST': _POST}
        t = Template(html)
        message_body = t.render(context).encode()

        return b''.join([response_line, entity_header, message_body])
    else:
        response_line = b'HTTP/1.1 404 Not Found\r\n'
        entity_header = b'Content-Type: text/html\r\n\r\n'
        message_body = b'<h1>404 Not Found</h1>'

        return b''.join([response_line, entity_header, message_body])

if __name__ == "__main__":
    tcp_server()
