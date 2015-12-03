import socket
from urllib.parse import quote_plus

request_text = """\
GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.1\r
Host: maps.google.com:80\r
User-Agent: GHOST\r
Connection: close\r
\r
"""
def geocode(address):
    sock = socket.socket()
    sock.connect(('maps.google.com', 80))
    request = request_text.format(quote_plus(address))
    sock.sendall(request.encode('ascii'))
    raw_reply=b''
    while True:
        data = sock.recv(4444)
        if not data:
            break
        raw_reply += data
    answer = raw_reply.decode('utf-8')
    print(answer)

if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
