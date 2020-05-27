#!/usr/bin/env python

import unittest
from unittest import TestCase
import tcp_client
from io import StringIO
import sys
from unittest.mock import patch
import threading
import socket
import time

class TestTCPClient(unittest.TestCase):

    def mock_server():
        server_sock = socket.socket()
        server_sock.bind(('localhost', 9000))
        server_sock.listen()
        client,addr = server_sock.accept()
        request = client.recv(1024)
        client.sendall("You got the message".encode('utf-8'))
        server_sock.close()

    @classmethod
    def setUpClass(self):
        self.server_thread = threading.Thread(target=self.mock_server)
        self.server_thread.start()
   
    @classmethod
    def tearDownClass(self):
        self.server_thread.join()
   
    def test_invalidhost1(self):
        host = "notahost"
        port = "80"
       
       #test stdout
        with patch('sys.stdout', new = StringIO()) as fake_out:
            t =  tcp_client.TCPClient(host,port)
            t.start()
            t.stop()
            self.assertEqual(fake_out.getvalue(), "Error: {} is an invalid host name\n".format(host))
    
    def test_invalidport1(self):
        host = "google.com"
        port = "notaport"
        
        #test stdout
        with patch('sys.stdout', new = StringIO()) as fake_out:
            t =  tcp_client.TCPClient(host,port)
            t.start()
            t.stop()
            self.assertEqual(fake_out.getvalue(), "'{}' is an invalid port number\n".format(port))
  
    def test_valid_connection(self):
        host = "localhost"
        port = "9000"
        
        t =  tcp_client.TCPClient(host,port)
        response = t.start()
        t.stop()
        self.assertIsNotNone(response)
if __name__ == "__main__":
    unittest.main()
