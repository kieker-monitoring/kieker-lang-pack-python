# -*- coding: utf-8 -*-
import socket
class TCPClient:
    
    def __init__(self):
        self.port = None
        self.host = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    
    def set_port_and_host(self, port, host):
        self.port = port
        self.host = host
    
    def send(self, data):
        self.socket.sendall(data)
    
    def connect(self):
        self.socket.connect_ex((self.host, self.port))
        