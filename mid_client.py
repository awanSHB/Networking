import socket


host = "127.0.0.1"
port = 2004

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))
    
string = input("Enter The String: ")
    
client_socket.send(string.encode())
    
result = client_socket.recv(1024).decode()
print("\nThe sum of the individual digits as a string:")
print("Server response is:", result)
    
client_socket.close()

