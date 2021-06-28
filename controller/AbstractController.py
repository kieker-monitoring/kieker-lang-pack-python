# -*- coding: utf-8 -*-

#
import logging
from abc import ABC, abstractmethod
class AbstractController(ABC) :
    
    
    def __init__(self, domain, tcp_enabled, reader_thread, port,
               terminated):
        self.domain=domain
        self.tcp_enabled=tcp_enabled
        self.reader_function=reader_thread
        self.port=port
        self.terminated=terminated
        self.logger=logging.getLogger('ControllerLogger')
   
    @abstractmethod    
    def initialize(self):
        if self.tcp_enabled==True :
            self.logger.info('Start Thread reader')
            self.threading.start()
    
    @abstractmethod
    def cleanup(self):
        if self.tcp_enabled:
            self.logger.info('Terminate')
    
    
    @abstractmethod
    def toString(self):
        pass