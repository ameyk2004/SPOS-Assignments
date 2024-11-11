from socket import *
import threading

HOST = '127.0.0.1'
PORT = 3000

def log(prefix, message:str):
    print(f"[{prefix}]\t\t{message}")

def run_client(client_id, message):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((HOST, PORT))

    log("INFO", f"\n{client_id} Connected to server")
    log("INFO", f"Sending message : {message}")

    clientSocket.sendall(message.encode())
    data:bytes = clientSocket.recv(1024)

    log("INFO", f"Message Received from server: {data.decode()}")
    clientSocket.close()

def main():

    messages = ["Message 1", "Message 2", "Message 3", "Message 4",]

    for i in range(len(messages)):
        client_thread = threading.Thread(target=run_client, args = (i+1, messages[i]))
        client_thread.start()
    

if __name__ == "__main__":
    main()