import socket, sys
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST='127.0.0.1'
PORT=8888

def recv_all(sock, length):
	data=''
	while len(data) <length:
		more=sock.recv(length - len(data))
		if not more:
			print("......end")
			raise EOFError('socket closed %d bytes into a %d-byte message' %(len(data), length))
		data+=more.decode("utf-8")
	return data
	
	
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)

while True:
	print('Listening at',s.getsockname())
	sc, sockname=s.accept()
	print('We have accepted a connection from ', sockname)
	print('Socket connects', sc.getsockname(), 'and', sc.getpeername())
	message= recv_all(sc,16)
	print('The incoming 16-octect message says', repr (message))
	sc.sendall('BYE BYE CLIENT...'.encode("utf-8"))
	sc.close()
	print('Reply sent, socket closed')