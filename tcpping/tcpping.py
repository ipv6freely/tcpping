#!/usr/bin/python

import socket

def tcpping(host, port, timeout = 5):
    """ Does a TCP 'ping'
        Simply attempts a socket connection on the specified port
        22 = SSH
        23 = Telnet
        Timeout is 5 seconds
        Code "borrowed" from yantisj
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((host, int(port)))
        s.shutdown(socket.SHUT_RD)
        return True
    except:
        pass
        return False