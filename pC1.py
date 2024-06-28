import socket as skt

HOST = 'localhost'
PORT = 5001

s = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)

print("Don't Want To send? Enter exit!\n\n")
while True:
	data = input("\nEnter the data You want to send : ").encode()
	s.sendto(data, (HOST, PORT))
	if data.decode()=="exit":
		s.close()
		break
s.close()
print("----------->sent")
