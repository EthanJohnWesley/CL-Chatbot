
from pydoc import cli
import sys
import socket
from threading import Thread

# SERVER IP address
host = "0.0.0.0"
port = 5002
sep_token = "<SEP>"

#Initialize set of all connected client's sockets

client_sockets = set()

#TCP Socket creation and making port reusable
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host,port))
s.listen(5)

print(f"[*] Listening as {host}:{port}")

def listen_for_client(cs):
    while True: #Continues to listen for message from 'cs' socket
        try: #decoded message now exists
            msg = cs.recv(1024).decode()
        except Exception as e: #removes socket in event of error
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else: #Message recieved
            msg = msg.replace(sep_token, " : ")
            
        #iterate over all connected sockets
        for client_socket in client_sockets:
            client_socket.send(msg.encode())
            

while True: #Always listening for new connections all the time
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected")
    client_sockets.add(client_socket)
    
    #start a thread that always listens to client's messages
    t = Thread(target=listen_for_client, args=(client_socket,))
    
    #daemon = True ~ ends whenever the main thread ends
    t.daemon = True
    
    t.start()
    

for cs in client_sockets:
    cs.close()
s.close()