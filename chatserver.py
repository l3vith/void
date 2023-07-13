'''
Plan-
parse command 1st
server connnection
client connection

#annoying ahh need to add multithreading so multiple chatroom clienjts and work
'''

# Importing Libraries

import argparse
import socket
import threading
import rsa

# Server Shit
public_key,private_key=rsa.newkeys(1024)
public_partner=None
HOST_IP = "127.0.0.1" # Non Routable Meta Address
HOST_PORT = 6666 # Designated Port

def client_handler(client_socket, client_address):
    while True:
        client_socket.send(public_key.save_pkcs1("PEM"))
        data = rsa.decrypt(client_socket.recv(1024), private_key).decode()
        if not data:
            break
        print(f"Data Recieved: {client_address}: {data}")
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST_IP, HOST_PORT))
    server_socket.listen()
    print(f"Server is listening on {HOST_IP}:{HOST_PORT}")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")
        threading.Thread(target=client_handler, args=(client_socket, client_address)).start()

start_server()


'''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET (IPv4) & SOCK_STREAM (TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST_IP, HOST_PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connection Established - {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
'''