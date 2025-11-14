import socket

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 6969

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = s.accept()  # Accepts an incoming connection
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024) 
            if not data:
                break
            decoded_data = data.decode('utf-8')
            input(f"Received from client: {decoded_data}")
            response = f"Server received: {decoded_data}"
            conn.sendall(response.encode('utf-8'))

        print(f"Connection with {addr} closed.")