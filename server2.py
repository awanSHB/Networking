import socket

def evaluate_math_expr(expr):
	try:
		return str(eval(expr))
	except:
		return "Error: invalid expression"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 1334)

sock.bind(server_address)

sock.listen(3)

print(f'Server listening on {server_address[0]} : {server_address[1]}')

while True:
	print('Waiting for the client connection...')
	connection, client_address = sock.accept()
	
	try:
		print('connection from', client_address)
		data = connection.recv(1024).decode()
		print('Received "{}" '.format(data))
		result = evaluate_math_expr(data)
		print('Sending result "{}" '.format(result))
		connection.sendall(result.encode())
	finally:
		connection.close()