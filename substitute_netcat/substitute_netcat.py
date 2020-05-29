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
        self.target = None
        self.upload_destination = ""
        self.port = None

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

            if self.target == None or self.port == None:
                print("Missing valid target or port")
                sys.exit(0)
            #client mode 
            elif not self.listen:
                buffer = sys.stdin.read()
                #send data off
                self.client_sender(buffer)
            #server-mode: listen and maybe upload, execute, or drop shell back
            elif self.listen:
                self.server_loop()

    def client_sender(self,buffer):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            #connect to target host
            print(self.target, self.port)
            client.connect((self.target,self.port))
            if len(buffer):
                client.sendall(buffer.encode('utf-8'))

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
                client.sendall(buffer.encode('utf-8'))
        except Exception as e:
            print(e)
            client.close()

    def server_loop(self):
        print(self.target,self.port)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.target,self.port))
        listeners = 5
        server.listen(listeners)

        while True:
            try:
                client_socket,addr = server.accept()
                print("[*] Accepted connection from: {0}:{1}".format(addr[0], addr[1]))
                client_thread = threading.Thread(target=self.client_handler,
                        args=(client_socket,))
                client_thread.start()
            except KeyboardInterrupt: #graceful shutdown
                server.close()
                print("Server is now shutting down")
                break

    def run_command(self,command):
        command = command.rstrip() #trim newline
        # run the command and get the output back
        try:
            output = subprocess.check_output(command,stderr=subprocess.STDOUT,
                    shell=True)
        except:
            output = "Failed to execute command.\r\n"
        # send output back to the client
        return output
    
    def client_handler(self,client_socket):
        if len(self.upload_destination):
            file_buffer=""
            #keep reading data until none is available
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                else:
                    file_buffer += data
                    file_buffer += data

            try:
                file_descriptor = open(upload_destination, "wb")
                file_descriptor.write(file_buffer)
                file_descriptor.close()

            except:
                client_socket.sendall("Failed to save file to {}\r\n".format(self.upload_destination).encode('utf-8'))
        
        #check for command execution
        if self.execute:
            output = self.run_command(self.execute)
            client_socket.sendall(output.encode('utf-8'))

        if self.command:
            while True:
                # show simple prompt
                client_socket.sendall("<Netcat:#>".encode('utf-8'))
                cmd_buffer = ""
                while "\n" not in cmd_buffer:
                    cmd_buffer += client_socket.recv(1024)
            #send back command output
            response = self.run_command(cmd_buffer)

            #send back response
            client_socket.sendall(response.encode('utf-8'))
            client_socket.close()


if __name__ == "__main__":
    nc = Netcat()
    nc.main()
