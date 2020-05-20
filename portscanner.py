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

if __name__ == '__main__':
    """
    Input:
        sys.argv[1] : host name
        sys.argv[2] : port number
    """
    portscan(sys.argv[1], sys.argv[2])
