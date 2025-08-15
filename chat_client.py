import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:  # noqa: E722
            print("An error occurred!")
            client_socket.close()
            break

# Client setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

# Get username
username = input("Enter your username: ")
client.send(username.encode('utf-8'))

# Start a thread to receive messages
threading.Thread(target=receive_messages, args=(client,)).start()

while True:
    message = input("")
    if message.lower() == "exit":
        break
    client.send(message.encode('utf-8'))

client.close()
