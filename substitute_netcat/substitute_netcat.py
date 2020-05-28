#!/usr/bin/python

import sys
import socket
import getopt
import threading
import subprocess

class Netcat:
    
    def __init__(self):
        self.listen = False
        self.command = False
        self.upload = False
        self.execute = False
        self.target = ""
        self.upload_destination = ""
        self.port = 0

    def help(self):
        """
        Substitute Netcat Tool

        usage: substitute_netcat.py -t target_host -p port

        Options:
            -l --listen                 -listen on [host]:[port] for incoming connections
            -e --execute=file_to_run    -execute the given file upon receiving connection
            -c --command                -initialize a command shell
            -u --upload=destination     - upon receiving connection upload a file and write to [destination]

        Examples:
            substitute_netcat.py -t 192.168.0.1 -p 5555 -l -c
            substitute_netcat.py -t 192.168.0.1 -p 5555 -e=\"cat /etc/passwd\"
            echo 'hello' | ./substitute_netcat.py -t 192.168.11.12 -p 135
        """
        print(self.help.__doc__)
        sys.exit(0)

    def main(self):
        if "-h" in sys.argv or not len(sys.argv[1:]):
            self.help()
        
        #read commandline options
        try:
            opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",
                    ["help","listen","execute","target","port","command","upload"])
        except getopt.GetoptError as err:
            print(str(err))
            help()

        for o,a in opts:
            if o in ("-h", "--help"):
                self.help()
            elif o in ("-l","--listen"):
                self.listen = True
            elif o in ("-c","--commandshell"):
                self.command = True
            elif o in ("-u", "--upload"):
                self.upload_destination = a
            elif o in ("-t","--target"):
                self.target = a
            elif o in ("-p","--port"):
                self.port = int(a)
            else:
                assert False, "Unhandled Option"

            # are we going to listen or just send data from stdin?
            if not self.listen and len(self.target) and self.port > 0:
                print("Enter a message to send to target")
                buffer = sys.stdin.readline()
                #send data off
                self.client_sender(buffer)

            #listen and maybe upload, execute, or drop shell back

            if self.listen:
                self.server_loop()

    def client_sender(self,buffer):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            #connect to target host
            client.connect((self.target,self.port))
            if len(buffer):
                client.sendall(buffer)

            while True:
                #now wait for data back
                recv_len = 1
                response = ""

                while recv_len:
                    data = client.recv(4096)
                    recv_len = len(data)
                    response += data

                    if recv_len < 4096:
                        break
                print(response)
                buffer = raw_input("")
                buffer += "\n"
                #send it off
                client.sendall(buffer)
        except Exception as e:
            print(e)
            client.close()

    def server_loop(self):
        pass

if __name__ == "__main__":
    nc = Netcat()
    nc.main()
