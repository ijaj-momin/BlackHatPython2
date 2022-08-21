#!/bin/python

from http import client
from pydoc import cli
import socket
from urllib import response

target_Host = "www.google.com"
target_Port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connet the client
client.connect((target_Host,target_Port))

#send some data
client.send(b"GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")

#receive some data
response = client.recv(4096)

#uncomment below code for full output 
"""
print(f"client: {client}\n")
print("\n clien end \n")
print(response)
print("\n response end \n")
print()
"""
print(response.decode())
client.close()

"""
OUTPUT
$ python TCP.py    
client: <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.92.128', 33360), raddr=('142.250.182.4', 80)>


 clien end 

b'HTTP/1.1 301 Moved Permanently\r\nLocation: http://www.google.com/\r\nContent-Type: text/html; charset=UTF-8\r\nDate: Sun, 21 Aug 2022 14:44:18 GMT\r\nExpires: Tue, 20 Sep 2022 14:44:18 GMT\r\nCache-Control: public, max-age=2592000\r\nServer: gws\r\nContent-Length: 219\r\nX-XSS-Protection: 0\r\nX-Frame-Options: SAMEORIGIN\r\n\r\n<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">\n<TITLE>301 Moved</TITLE></HEAD><BODY>\n<H1>301 Moved</H1>\nThe document has moved\n<A HREF="http://www.google.com/">here</A>.\r\n</BODY></HTML>\r\n'

 response end 


HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Sun, 21 Aug 2022 14:44:18 GMT
Expires: Tue, 20 Sep 2022 14:44:18 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
"""
