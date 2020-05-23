#!/usr/bin/env python

import unittest
from unittest import TestCase
import tcp_client
from io import StringIO
import sys
from unittest.mock import patch

class TestTCP(unittest.TestCase):

    def test_invalidhost1(self):
        host = "notahost"
        port = "80"
        
        with patch('sys.stdout', new = StringIO()) as fake_out:
            tcp_client.tcp_client(host,port)
            self.assertEqual(fake_out.getvalue(), "Error: {} is an invalid host name\n".format(host))
    
    def test_invalidport1(self):
        host = "google.com"
        port = "notaport"
        
        with patch('sys.stdout', new = StringIO()) as fake_out:
            tcp_client.tcp_client(host,port)
            self.assertEqual(fake_out.getvalue(), "'{}' is an invalid port number\n".format(port))
  
    def test_valid_connection(self):
        host = "google.com"
        port = "80"
        
        response = tcp_client.tcp_client(host,port)
        self.assertIsNotNone(response)

if __name__ == "__main__":
    unittest.main()
