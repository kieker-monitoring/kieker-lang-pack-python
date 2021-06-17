# -*- coding: utf-8 -*-

#
import logging

class AbstractController :
    
    def __init__(self, domain, tcp_enabled, reader_thread, port, buffer_capacity,
               terminated):
        self.domain=domain
        self.tcp_enabled=tcp_enabled
        self.reader_function=reader_thread
        self.port=port
        self.buffer_capacity=buffer_capacity
        self.terminated=terminated
        self.logger=logging.getLogger('ControllerLogger')
        
    def initialize(self):
        if self.tcp_enabled==True :
            self.logger.info('Start Thread reader')
            self.threading.start()
    

    def cleanup(self):
        if self.tcp_enabled:
            self.logger.info('Terminate')
        