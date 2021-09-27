# -*- coding: utf-8 -*-
import socket
class TCPClient:
    
    def __init__(self):
        self.port=65432
        self.host ='127.0.0.1'
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
    
    def send(self, data):
        self.socket.sendall(data)