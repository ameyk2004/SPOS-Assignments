from socket import *
import threading

HOST = '127.0.0.1'
PORT = 3000
def log(prefix, message):
    print(f"[{prefix}]\t\t{message}")

def handle_client(client_socket: socket):
    while True:
        
        data = client_socket.recv(1024)

        if not data:
            break
        log("INFO", f"Data Recieved : {data.decode()}")
        client_socket.sendall(data)
    client_socket.close()

def main():

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(10)

    log("INFO", "Listening on Port 3000")

    while True:

        client_socket, client_addr = serverSocket.accept()
        log("INFO", f"Connected to Client : {client_addr[0]}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
        
if __name__ == "__main__":
    main()