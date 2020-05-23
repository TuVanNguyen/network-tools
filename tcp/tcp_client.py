#!/usr/bin/python

import socket
import sys
from customExceptions import PortValueError

def tcp_client(host, port):
    """
    Creates a tcp connection
    
    Args:
        host (string): target host name (e.g "google.com")
        port (string): port number, in string form because of input from command-line, must validate that it's number
    Returns:
        response (string): response from tcp connection
    """
    try:
        #Check input
        if not port.isdigit():
            raise PortValueError("", port)

        # create socket object
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to client
        client.connect((host, int(port)))
        #send data
        client.send("GET / HTTP/1.1\r\nHost:{}\r\n\r\n".format(host))
        #receive some data
        response = client.recv(4096)
        client.close()
        print(response)
        return response
    except socket.gaierror:
        print("Error: {} is an invalid host name".format(host))
        client.close()
    except PortValueError as e:
        print(e)



if __name__ == "__main__":
    """
    Input:
        sys.argv[1] : target host name (e.g "google.com")
        sys.argv[2]: target port number (e.g 80)
    """
    target_host = sys.argv[1]
    target_port = sys.argv[2]
    tcp_client(target_host,target_port)


