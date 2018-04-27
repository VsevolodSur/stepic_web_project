#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 2222))
server_socket.listen(10)

while True:
    client_scoket, remote_addr = server_socket.accept()
    try:
        while True:
            request = client_scoket.recv(1024)
            print ('{} : {}'.format(client_scoket.getpeername(), request))
            if request.decode().find('close') >= 0:
                client_scoket.close()
            client_scoket.send(request)
    except:
        pass

server_socket.close()
