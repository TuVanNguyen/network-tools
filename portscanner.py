#!/usr/bin/python

import socket
import sys

def portscan(t_host, t_port):

    try:
        sock = socket.socket()
        t_ip = socket.gethostbyname(t_host)
        res = sock.connect((t_ip, int(t_port)))
        print("Port {}: Open".format(t_port))
    except socket.gaierror:
        print("Error: {} is an invalid host name".format(t_host))
    except Exception as e:
        print("Port {}: Closed".format(t_port))
        print(e.__class__.__name__)
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
