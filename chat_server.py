import socket
import threading

clients = {}
history = []

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                full_message = f"{username}: {message}"
                history.append(full_message)  # Store message in history
                print(full_message)
                # Broadcast message to all connected clients
                for client in clients.values():
                    if client != client_socket:
                        client.send(full_message.encode('utf-8'))
            else:
                break
        except:  # noqa: E722
            break
    client_socket.close()
    del clients[username]

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(5)
print("Server is listening on port 12345")

try:
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")

        client_socket.send("Enter your username: ".encode('utf-8'))
        username = client_socket.recv(1024).decode('utf-8')

        clients[username] = client_socket
        print(f"User {username} connected.")
        
        threading.Thread(target=handle_client, args=(client_socket, username)).start()

except KeyboardInterrupt:
    print("\nShutting down the server...")

finally:
    for client in clients.values():
        client.close()
    server.close()
    print("Server closed.")
