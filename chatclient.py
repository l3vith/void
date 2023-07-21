# Client Side

import socket
import threading
from termcolor import colored
import rsa
import sys
import select 

if len(sys.argv) != 2:
    print ("Correct usage: script, port number")
    exit()
HOST_IP = "0.tcp.in.ngrok.io"
HOST_PORT = int(sys.argv[1])
public_partner=None
def word_count(message):
    word_list = message.split()
    return len(word_list)
   
user=input("Enter your username" + "➜ ")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST_IP, HOST_PORT))
    while True:
        message = input(colored(user, 'light_blue') + "➜ ")
        public_partner= rsa.PublicKey.load_pkcs1(s.recv(1024))
        s.sendall(rsa.encrypt(message.encode(), public_partner))
        
        

    
    
print(f"Recieved {data!r}")