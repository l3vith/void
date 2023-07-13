# Client Side

import socket
import threading
from termcolor import colored
import rsa
user = "levi"
HOST_IP = "127.0.0.1"
HOST_PORT = 6666

public_partner=None
def word_count(message):
    word_list = message.split()
    return len(word_list)
   

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST_IP, HOST_PORT))
    while True:
        message = input(colored(user, 'light_blue') + "➜ ")
        public_partner= rsa.PublicKey.load_pkcs1(s.recv(1024))
        s.sendall(rsa.encrypt(message.encode(), public_partner))
        

    
    
print(f"Recieved {data!r}")