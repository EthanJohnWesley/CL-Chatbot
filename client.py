
import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back


init()

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

client_color = random.choice(colors)

#Server host (if not on this network use private network IP (192.168.1.2))
HOST = "10.0.0.80"
PORT = 5002
separator_token = "<SEP>"

s = socket.socket()
print(f"[*] Connecting to {HOST}:{PORT}...")

s.connect((HOST,PORT))

print("[*] Connected. Welcome to the Server")

name = input("What's your name: ")

def listen_for_messages():
    while True:
        try:
            message = s.recv(1024).decode()
            print("\n" + message)
        except Exception as e:
            print("-----Good Bye-----")

t = Thread(target = listen_for_messages)
t.daemon = True
t.start()


while True:
    
    to_send = input()
    left_msg = "***LEFT THE CHAT***"
    
    if to_send.lower() == "q":
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        to_send = f"{client_color}[{date_now}] {name}{separator_token}{left_msg}{Fore.RESET}"
        s.send(to_send.encode())
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
    s.send(to_send.encode())
    
s.close()