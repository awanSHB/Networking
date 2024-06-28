import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	# Bind the socket to the address and port
	s.bind((HOST, PORT))
	
	# listen for incomming calls
	
	s.listen()
	print("Server is listening...")
	
	# Accept incoming connnections
	conn, addr = s.accept()
	
	with conn:
		print(f"Connected by {addr}")
		
		# Receive data from the client
		data = conn.recv(1024)
		
		print(f"Received data: {data.decode()}")
		
		# send a response back to the client
		
		conn.sendall(b"Message received by the server")
		conn.close();