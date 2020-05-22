#!/usr/bin/python

import socket
import sys
from customExceptions import PortValueError

def portscan(t_host, t_port):
    """
    Scans host at specific port to see if that port is open or closed
    """
    try:
        sock = socket.socket()
        t_ip = socket.gethostbyname(t_host)
        if not t_port.isdigit():
            raise PortValueError("",t_port)
        res = sock.connect((t_ip, int(t_port)))
        print("Port {}: Open".format(t_port))
    except socket.gaierror:
        print("Error: {} is an invalid host name".format(t_host))
    except PortValueError as e:
        print(e)
    except Exception as e:
        print("Port {}: Closed".format(t_port))
        #print(e)
        #print(e.__class__.__name__)
    finally:
        sock.close()
        print("Port Scanning Complete")


def banner(t_host, t_port):
    """
    Banner grabbing for specified host at specified port
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
        if not t_port.isdigit():
            raise PortValueError("",t_port)
        sock.connect((t_host,int(t_port)))
        sock.send("GET / HTTP/1.1\r\nHost:{}\r\n\r\n".format(t_host))
        response = sock.recv(4096)
        print(response)

    except socket.gaierror:
        print("Error: {} is an invalid host name".format(t_host))
    except PortValueError as e:
        print(e)
    finally:
        sock.close()
 

if __name__ == '__main__':
    """
    Input:
        sys.argv[1] : host name
        sys.argv[2] : port number
        sys.argv[n] : any number of additional options
    """

    if '-b' in sys.argv:
        banner(sys.argv[1], sys.argv[2])
    if len(sys.argv) == 3:
        portscan(sys.argv[1], sys.argv[2])

