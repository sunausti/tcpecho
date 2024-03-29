import sys
from socket import *

serverHost = '127.0.0.1'
serverPort = 1237
print("serverPort is %s" % serverPort)
message = [b'Hello network']

if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))
print(sockobj.getsockname())

for line in message:
    sockobj.send(line)
    data = sockobj.recv(1024)
    print('Client received:',data)
