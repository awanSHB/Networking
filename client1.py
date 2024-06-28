import socket

HOST = 'localhost'
PORT = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(b' Hello, BOY ', (HOST, PORT))
s.close()
print("--------> Message Sent")