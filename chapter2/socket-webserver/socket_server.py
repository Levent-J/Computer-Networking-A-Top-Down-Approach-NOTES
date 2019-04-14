#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os

__author__ = 'levent_j'

from socket import *


def server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', 1234))
    server_socket.listen(1)
    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = server_socket.accept()
        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            with open(os.path.join(filename[1:].decode())) as f:
                output = f.read()
                header = 'HTTP/1.1 200 OK\n' \
                         'Connection: close\n' \
                         'Content-Type: ' \
                         'text/html\n' \
                         'Content-Length: %d\n' \
                         '\n' \
                         '' % (len(output))
                connectionSocket.send(header.encode())
                for i in range(0, len(output)):
                    connectionSocket.send(output[i].encode())
            connectionSocket.close()
        except IOError:
            # Send response message for file not found
            header = ' HTTP/1.1 404 Found'
            connectionSocket.send(header.encode())
            connectionSocket.close()
        finally:
            pass
    server_socket.close()


if __name__ == "__main__":
    server()
