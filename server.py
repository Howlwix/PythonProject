import socket
import threading

server = socket.socket()

server.bind(("localhost", 6767))
server.listen()

print("Server is listening on port 6767...")

connections = 0

def handle_client(client):
    while True:
        msg = client.recv(1024)

        if not msg:
            break

        print(f"client {connections}: {msg.decode()}")
        print(threading.current_thread().name)
        client.send(msg.encode())
    print(f"client {connections} disconnected")
    client.close()


lock = threading.Lock()

while True:
    client, addr = server.accept()
    with lock:
        connections += 1
    print(f"Connected from {addr},client {connections} ")
    thread = threading.Thread(target=handle_client, args=(client,connections))
    thread.start()