#!/usr/bin/env python
import unittest
from unittest import TestCase
import tcp_proxy
from io import StringIO
from unittest.mock import patch
import sys

class TestTCPProxy(unittest.TestCase):
    def testInvalidNumberInput(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
                sys.argv = "./tcp_proxy.py".split()
                expectedoutput = "Usage: ./tcp_proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]\nExample: ./tcp_proxy.py 127.0.0.1 9000 10.12.132.1 9000 True"
                tp = tcp_proxy.TCP_Proxy()
                tp.read_input()
                self.assertEqual(fake_out.getvalue().strip(),expectedoutput)

    def testInvalidLocalPort(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
                sys.argv = "./tcp_proxy.py 127.0.0.1 notaport 10.12.132.1 9000 True".split()
                expectedoutput = "'{}' is an invalid port number for local port".format(sys.argv[2])
                tp = tcp_proxy.TCP_Proxy()
                tp.read_input()
                self.assertEqual(fake_out.getvalue().strip(),expectedoutput)

    def testInvalidRemotePort(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
                sys.argv = "./tcp_proxy.py 127.0.0.1 9000 10.12.132.1 notaport True".split()
                expectedoutput = "'{}' is an invalid port number for remote port".format(sys.argv[4])
                tp = tcp_proxy.TCP_Proxy()
                tp.read_input()
                self.assertEqual(fake_out.getvalue().strip(),expectedoutput)
 
    def testInvalidReceiveFirst(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
                sys.argv = "./tcp_proxy.py 127.0.0.1 9000 10.12.132.1 9000 notbool".split()
                expectedoutput = "'{}' is not a valid boolean value. Please enter true/false".format(sys.argv[5])
                tp = tcp_proxy.TCP_Proxy()
                tp.read_input()
                self.assertEqual(fake_out.getvalue().strip(),expectedoutput)
 

if __name__ == "__main__":
    unittest.main()
