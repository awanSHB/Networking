import socket as skt

s = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

server_address = ('localhost', 5001)

print("Connecting To The ", server_address)

s.connect(server_address)

try:
	math_exp = input("Enter the Expression: ")
	s.sendall(math_exp.encode())
	data = s.recvfrom(1024).decode()
	print("The result is ", data)
finally:
	s.close()