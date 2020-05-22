#!/usr/bin/python

import socket
import sys

def udp_client(host,port, message):
    # create socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    #send data
    client.sendto(message, (host,port))

    #receive some data
    data,addr = client.recvfrom(4096)

    print data

if __name__ == "__main__":
    """
    Input:
        sys.argv[1]: target host
        sys.argv[2]: target port
        sys.argv[3]: some payload message
    """
    host = sys.argv[1]
    port = int(sys.argv[2])
    message = sys.argv[3]
    udp_client(host, port, message)
