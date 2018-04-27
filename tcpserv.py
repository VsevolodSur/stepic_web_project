#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 12:36:13 2017

@author: sbt-suryaninov-va
"""

import socket
#import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(1)
while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data:  break
        print(data)
        if data.decode().find('close') >= 0:
            conn.close()
            break
        conn.send(data)
        
