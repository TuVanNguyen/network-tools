#!/usr/bin/python

import socket
import sys
from customExceptions import PortValueError

class TCPClient:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.client = None

    def start(self):
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
            if not self.port.isdigit():
                raise PortValueError("", self.port)

            # create socket object
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # connect to client
            self.client.connect((self.host, int(self.port)))
            #send data
            self.client.sendall("GET / HTTP/1.1\r\nHost:{}\r\n\r\n".format(self.host).encode('utf-8'))
            #receive some data
            response = self.client.recv(4096)
            print(response)
            return response
        except socket.gaierror:
            print("Error: {} is an invalid host name".format(self.host))
            self.stop()
        except PortValueError as e:
            print(e)
            self.stop()

    def stop(self):
        if self.client != None:
            self.client.close()


if __name__ == "__main__":
    """
    Input:
        sys.argv[1] : target host name (e.g "google.com")
        sys.argv[2]: target port number (e.g 80)
    """
    target_host = sys.argv[1]
    target_port = sys.argv[2]
    t = TCPClient(target_host,target_port)
    t.start()
    t.stop()


