#!/usr/bin/env python

import unittest
import substitute_netcat as netcat
from io import StringIO
from unittest.mock import patch
import sys

class TestTCPClient(unittest.TestCase):

    def testHelp(self):
        #test stdout
        with patch('sys.stdout',new = StringIO()) as fake_out:
            with self.assertRaises(SystemExit): #help function should exit 
                nc = netcat.Netcat()
                nc.help()
                self.assertEqual(fake_out.getvalue().strip(), nc.help.__doc__.strip())
    
    def testMainInput_H(self):
        #test stdin and stdout
        with patch('sys.stdout', new = StringIO()) as fake_out:
            with self.assertRaises(SystemExit):
                sys.argv = "./substitute_netcat -h".split()
                nc = netcat.Netcat()
                nc.main()
                self.assertEqual(fake_out.getvalue().strip(), nc.help.__doc__.strip())

    def testMainInput_help(self):
        #test stdin and stdout
        with patch('sys.stdout', new = StringIO()) as fake_out:
            with self.assertRaises(SystemExit):
                sys.argv = "./substitute_netcat -help".split()
                nc = netcat.Netcat()
                nc.main()
                self.assertEqual(fake_out.getvalue().strip(), nc.help.__doc__.strip())

    def testMainInput_l(self):
        sys.argv = "./substitute_netcat -l".split()
        nc = netcat.Netcat()
        nc.main()
        self.assertEqual(nc.listen, True)

    def testMainInput_c(self):
        sys.argv = "./substitute_netcat -c".split()
        nc = netcat.Netcat()
        nc.main()
        self.assertEqual(nc.command, True)

    def testMainInput_u(self):
        sys.argv = "./substitute_netcat -u test.txt".split()
        nc = netcat.Netcat()
        nc.main()
        self.assertEqual(nc.upload_destination, "test.txt")
    
if __name__ == "__main__":
    unittest.main()

