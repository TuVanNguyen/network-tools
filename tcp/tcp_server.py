#!/usr/bin/python

import socket
import threading
import sys

def tcp_server(bind_ip, bind_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip,bind_port))
    server.listen(5) # 5 is maximum backlog of connections

    print("[*] Listening on {0}:{1}".format(bind_ip,bind_port))
    
    while True:
        try:
            client,addr = server.accept()

            print("[*] Accepted connection from: {0}:{1}".format(addr[0], addr[1]))

            #spin up client thread to handle incoming data
            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()

        except KeyboardInterrupt: #graceful shutdown
            server.close()
            print("Shutting down server")
            break

def handle_client(client_socket):
    
    #print client requests
    request = client_socket.recv(1024)

    print("[*] Received: {}".format(request))

    #send back a packet
    client_socket.send("Thanks for hitting up your trusty local tcp server")
    client_socket.close()

if __name__ == "__main__":
    """
    Input:
        sys.argv[1]: ip address server will listen on (e.g "0.0.0.0")
        sys.argv[2]: port server will listen on (e.g 9999)
    """
    bind_ip = sys.argv[1]
    bind_port = int(sys.argv[2])
    tcp_server(bind_ip, bind_port)
