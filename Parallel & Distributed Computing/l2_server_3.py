import socket

def recv_all(sock, length):
    data = ''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('Socket closed %d bytes into a %d-byte message' % (len(data), length))
        data += more.decode("utf-8")
    return data

# Server code
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 8888

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)

while True:
    print('Listening at', s.getsockname())
    sc, sockname = s.accept()
    print('We have accepted a connection from', sockname)
    print('Socket connects', sc.getsockname(), 'and', sc.getpeername())
    length_header = recv_all(sc, 3)  # Receive the length header
    msg_length = int(length_header)
    message = recv_all(sc, msg_length)  # Receive the rest of the message
    print('The incoming message says', repr(message))
    sc.sendall('BYE BYE CLIENT...'.encode("utf-8"))
    sc.close()
    print('Reply sent, socket closed')