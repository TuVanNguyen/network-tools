#!/usr/bin/python

import socket
import sys

def tcp_client(host, port):
    # create socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to client
    client.connect((host, port))
    #send data
    client.send("GET / HTTP/1.1\r\nHost:{}\r\n\r\n".format(host))
    #receive some data
    response = client.recv(4096)
    print(response)



if __name__ == "__main__":
    """
    Input:
        sys.argv[1] : target host name (e.g "google.com")
        sys.argv[2]: target port number (e.g 80)
    """
    target_host = sys.argv[1]
    target_port = int(sys.argv[2])
    tcp_client(target_host,target_port)


