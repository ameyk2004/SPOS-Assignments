from socket import *
import threading

HOST = '127.0.0.1'
PORT = 3000
def log(prefix, message):
    print(f"[{prefix}]\t\t{message}")

def run_client(id, message):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    log("INFO", f"Client {id} connected to server")
    log("INFO", f"Sending message {message}")

    client_socket.sendall(message.encode())

    data = client_socket.recv(1024)
    log("INFO", f"Recieved back message {data}")
    
    client_socket.close()

def main():

    messages = ["Hello There", "How are You"]

    for i in range(len(messages)):
        message = messages[i]
        client_thread = threading.Thread(target=run_client, args=(i+1, message))
        client_thread.start()
    
    # client_socket = socket(AF_INET, SOCK_STREAM)
    # client_socket.connect((HOST, PORT))

    # log("INFO", "Client Connected")
        
if __name__ == "__main__":
    main()