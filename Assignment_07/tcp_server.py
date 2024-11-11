from socket import *
import threading

HOST = '127.0.0.1'
PORT = 3000

def log(prefix, message):
    print(f"[{prefix}]\t\t{message}")

def handle_client(client_socket: socket):
    while True:
        data:bytes = client_socket.recv(1024)

        if not data:
            break

        log("INFO", f"Message from Client : {data.decode()}")
        client_socket.send(data)

    client_socket.close()

def main():

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(10)

    log("INFO", "listening on Port 3000")

    while True:

        try:
            clientSocket, client_addr = serverSocket.accept()
            log("INFO", f"Client Connected : {client_addr[0]}:{client_addr[1]}")
            client_thread = threading.Thread(target=handle_client, args=(clientSocket,))
            client_thread.start()

        except KeyboardInterrupt:
            log("LOG", "Server Shutting Down...")
            break
        except Exception as e:
            log("ERROR", "error occurred")
            print(e)
            break

    serverSocket.close()  

    

if __name__ == "__main__":
    main()