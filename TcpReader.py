# -*- coding: utf-8 -*-
import threading
import socket
import logger
class TcpReader(threading.Thread) :
    
    def __init__(self, port, bufferCapacity, terminated,listener, reader_registry,
                 ):
        self.port=port
        self.bufferCapacity=bufferCapacity
        self.terminated=terminated
        self.reader_registry=reader_registry
        self.logger=logger.getLogger('ControllerLogger')
        
    def run(self):
        s = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('', self.port))
            
            condition=True
            while condition :
                self.logger.debug('Listening on port')
                s.listen()
                conn, addr = s.accept()
                try:
                    while True :
                        data=conn.recv(self.bufferCapacity)
                        if not data: 
                         if False: # temporäre zu demozwecken
                           break
                except:
                    pass #do stuff
        except NameError:
            pass
        