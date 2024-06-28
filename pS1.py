import socket as skt

PORT = 5001
HOST = ''

s = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
s.bind((HOST, PORT))
print("Waiting ...")

while True:
	data, address = s.recvfrom(1024)
	print("Received data is  ", data.decode())
	print("Client address is ", address)
	
	if data.decode() == "exit":
		s.close()
		break
s.close()