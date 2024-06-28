import socket

def recv_all(sock, length):
    data = ''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('Socket closed %d bytes into a %d-byte message' % (len(data), length))
        data += more.decode("utf-8")
    return data

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 8888

s.connect((HOST, PORT))
print('Client has been assigned socket name', s.getsockname())
msg = 'Hello!! Server!!'
length = str(len(msg)).zfill(3)  # Determine length of message and pad with leading zeros
msg_with_length = length + msg  # Add length information to the message
s.sendall(msg_with_length.encode('utf-8'))
reply = recv_all(s, 16)
print('THE SERVER SAID', repr(reply))
s.close()