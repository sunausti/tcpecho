import sys
from socket import *

serverHost = '10.97.165.88'
serverPort = 1237
print("serverPort is %s" % serverPort)
message = [b'Hello network']

if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

for line in message:
    sockobj.send(line)
    data = sockobj.recv(1024)
    print('Client received:',data)
