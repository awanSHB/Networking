import socket as skt

def evaluate_exp(exp):
	try:
		return str(eval(exp))
	except:
		return "Error: Invalid Expression"
	
s	= skt.socket(skt.AF_INET, skt.SOCK_STREAM)

server_address = ('localhost', 5001)

s.bind(server_address)

s.listen(3)

print(f"Listening on {server_address[0]} : {server_address[1]}")

while True:
	