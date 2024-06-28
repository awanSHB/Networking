import socket

HOST = ''
PORT = 5001

##AF_INET --------> Address Family Internet
##SOCK_DGRAM -----> Socket DataGram

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
print("Waiting...")
while True:
	data, addr = s.recvfrom(1024)				##1024bytes maximum data received at once
	print('Received data: ', data.decode())		##decode will convert bytes to string
	print('From Address : ',addr )
	s.close()

# data variable will contain up to 1024 bytes of data sent by the client,
# while the addr variable will contain the address of the client that sent the data 