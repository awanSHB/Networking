import socket


def calculate_sum(string):
    if not string.isdigit():
        return "Sorry, cannot compute!"
    s = 0
    for k in string:
        s += int(k)
    return str(s)

host = "127.0.0.1" 
port = 2004  


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind((host, port))


server_socket.listen(1)

print("Waiting for the client to establish a connection...")


client_socket, address = server_socket.accept()
print("Client connected:", address)

while True:
    
    data = client_socket.recv(1024).decode()
    
    if not data:
        break
    
    if not data.isdigit():
        result = "Sorry, cannot compute!"
    else:
        result = str(sum(int(digit) for digit in data))
    
    client_socket.send(result.encode())

client_socket.close()
server_socket.close()
