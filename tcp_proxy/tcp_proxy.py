#!/usr/bin/env python
import sys
import socket
import threading
from customExceptions import *

class TCP_Proxy:
    
    def __init__(self):
        self.localhost = None
        self.localport = None
        self.remotehost = None
        self.remoteport = None
        self.receive_first = None

    def server_loop(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
    def read_input(self):
        try:
            if len(sys.argv[1:]) != 5:
                usage = "Usage: ./tcp_proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]"
                example = "Example: ./tcp_proxy.py 127.0.0.1 9000 10.12.132.1 9000 True"
                raise ArgumentNumberError(usage,example)
            self.localhost = sys.argv[1]
            self.localport = sys.argv[2]
            self.remotehost = sys.argv[3]
            self.remoteport = sys.argv[4]
            self.receive_first = sys.argv[5]
            
            #convert port strings to integers with input validation
            if not self.localport.isdigit():
                raise PortValueError("local port",self.localport)
            else:
                self.localport = int(self.localport)
            if not self.remoteport.isdigit():
                raise PortValueError("remote port", self.remoteport)
            else:
                self.remoteport = int(self.remoteport)
            #input validation for receive_first
            if self.receive_first.lower() == "true" or self.receive_first.lower() == "false":
                self.receive_first =  True if self.receive_first.lower() == "true" else False
            else:
                raise BooleanValueError(self.receive_first)
        except ArgumentNumberError as e:
            print(e)
        except PortValueError as e:
            print(e)
        except BooleanValueError as e:
            print(e)

    def main(self):
        pass

if __name__ == "__main__":
    tp = TCP_Proxy()
    tp.read_input()
