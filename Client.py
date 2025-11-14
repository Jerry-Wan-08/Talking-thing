import socket

HOST = input("IP: ")
PORT = 6969

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    message_to_send = "Hello from the client!"
    s.sendall(message_to_send.encode('utf-8')) 

    data = s.recv(1024)
    received_message = data.decode('utf-8') 

    print(f"Received from server: {received_message}")
