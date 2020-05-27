#!/usr/bin/env python

import unittest
from unittest import TestCase
import tcp_server
import sys
import threading
import time
import socket
from io import StringIO
from unittest.mock import patch

class TestTCPServer(unittest.TestCase):
    
    def test_invalidport(self):
        host = "localhost"
        port = "notaport"

        #test stdout
        with patch('sys.stdout', new = StringIO()) as fake_out:
            t = tcp_server.TCPServer(host,port)
            t.start()
            self.assertEqual(fake_out.getvalue(), "'{}' is an invalid port number\n".format(port))

    def test_valid_server_connection(self):
        host = "localhost"
        port = "9999"
        t = tcp_server.TCPServer(host,port)
        server_thread = threading.Thread(target=t.start)
        server_thread.start()

        time.sleep(0.000001)

        fake_client = socket.socket()
        fake_client.settimeout(1)
        fake_client.connect((host,int(port)))
        fake_client.close()

        t.quit_server()
        server_thread.join()

    
if __name__ == "__main__":
    unittest.main()
