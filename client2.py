import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 1334)

print('Connecting to ',server_address)

sock.connect(server_address)

try:
	math_exp = input("Enter the math expression: ")
	sock.sendall(math_exp.encode())
	data = sock.recv(1024).decode()
	print('Result: ', data)
finally:
	sock.close()