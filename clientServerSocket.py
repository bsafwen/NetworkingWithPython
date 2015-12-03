import argparse, socket
from datetime import datetime

MAX_BYTES = 65535

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 4444))
    print('Server listening on 127.0.0.1:4444 ....')
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        print(address, ' just sent me this information :')
        print(data.decode('ascii'))
        reply = b'who r u ?'
        sock.sendto(reply, address)
        
def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        packet = input('Hello, type a message to send...\n')
        if packet == '':
            break
        sock.sendto(packet.encode('ascii'), ('127.0.0.1', 4444))
        data, address = sock.recvfrom(MAX_BYTES)
        print(data.decode('ascii'))
        print(address)

if __name__ == '__main__':
    choices = {'client':client, 'server':server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
