import socketserver
import os
print('hello')
class Handler_TCPServer(socketserver.BaseRequestHandler):
    """
    The TCP Server class for demonstration.

    Note: We need to implement the Handle method to exchange data
    with TCP client.

    """

    def handle(self):
        # self.request - TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} sent:".format(self.client_address[0]))
        print(self.data)
        # just send back ACK for data arrival confirmation
        self.request.sendall("ACK from TCP Server".encode())
if __name__ == "__main__":
    print("hello")
    try:
        HOST = os.environ['TCPSOCKET_ECHO_PORT_50007_TCP_ADDR']
        print("using HOST %s" % HOST)
    except:
        HOST = 'localhost'
        print("using HOST %s" % HOST)
        pass
    PORT = 1237
    # Init the TCP server object, bind it to the localhost on 9999 port
    tcp_server = socketserver.TCPServer((HOST,PORT), Handler_TCPServer)

    # Activate the TCP server.
    # To abort the TCP server, press Ctrl-C.
    tcp_server.serve_forever()
