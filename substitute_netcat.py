#!/usr/bin/python

import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False
execute = False
target = ""
upload_destination = ""
port = 0

def help():
    """
    Substitute Netcat Tool

    usage: substitute_netcat.py -t target_host -p port

    Options:
        - l --listen        -listen on [host]:[port] for incoming connections

    """
    print(help.__doc__)

if __name__ == "__main__":
    
    if "-h" in sys.argv:
        help()
