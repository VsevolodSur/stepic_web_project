#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 12:36:13 2017

@author: sbt-suryaninov-va
"""

import socket
#import sys

def myrecive(sock, msglen):
#    print (type(sock),sock)
#    print ('in myrecive')
    msg = ''.encode()
    while len(msg) < msglen:
        chunk = sock.recv(msglen - len(msg))
#        sock.send(chunk)
        msg = msg + chunk
#        print(msg)
        if msg.decode().find('close') >= 0: return ""
    return msg

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 2222))
#s.bind(('0.0.0.0', 2222))
s.listen(1)
while True:
    conn, addr = s.accept()
#    print (type(addr),addr)
    while True:
        data = myrecive(conn, 1024)
        #        print(data.decode().find('close'))
        if len(data) == 0:  break
        conn.send(data)
    break
conn.close
