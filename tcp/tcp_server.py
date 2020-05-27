#!/usr/bin/env python

import socket
import threading
import sys
from customExceptions import QuitServer
from customExceptions import PortValueError

class TCPServer:    
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.on = False

    def start(self):
        
        #input check
        try:
            if not self.port.isdigit():
                raise PortValueError("",self.port)
        except PortValueError as e:
            print(e)
            return

        self.on = True
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host,int(self.port)))
        server.listen(5) # 5 is maximum backlog of connections

        print("[*] Listening on {0}:{1}".format(self.host,self.port))
        
        while True:
            try:
                if not self.on:
                    raise(QuitServer(self.host, self.port))

                client,addr = server.accept()
                print("[*] Accepted connection from: {0}:{1}".format(addr[0], addr[1]))

                #spin up client thread to handle incoming data
                client_handler = threading.Thread(target=self.handle_client, args=(client,))
                client_handler.start()
            except KeyboardInterrupt: #graceful shutdown
                self.quit_server()
            except QuitServer as e: #graceful shutdown
                server.close()
                print(e)
                break


    def quit_server(self):
        self.on = False
        
    def handle_client(self,client_socket):
        
        #print client requests
        request = client_socket.recv(1024)

        print("[*] Received: {}".format(request))

        #send back a packet
        client_socket.sendall("Thanks for hitting up your trusty local tcp server".encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    """
    Input:
        sys.argv[1]: ip address server will listen on (e.g "0.0.0.0")
        sys.argv[2]: port server will listen on (e.g 9999)
    """
    bind_ip = sys.argv[1]
    bind_port = sys.argv[2]
    tcp_server = TCPServer(bind_ip, bind_port)
    tcp_server.start()
