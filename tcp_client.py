#!/usr/bin/python

import socket

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
    target_host = "www.google.com"
    target_port = 80
    tcp_client(target_host,target_port)


