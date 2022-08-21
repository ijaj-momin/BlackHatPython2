#!/bin/python

from http import client
from pydoc import cli
import socket
from traceback import print_tb
target_host = "127.0.0.1"
target_port = 9997

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto(b"AAABBBCC",(target_host, target_port))

#receive some data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
