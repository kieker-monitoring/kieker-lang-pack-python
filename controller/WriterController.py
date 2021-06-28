# -*- coding: utf-8 -*-
import logging
#from queue import Queue
from controller.AbstractController import AbstractController
class WriterController:
    def __init__(self,monitoring_writer):
        self.monitoring_writer=monitoring_writer
    
    def initialize(self):
        pass 
    
    def cleanup(self):
        pass
    #  self.LOGGER.debug('Initialize')     
     # if self.monitoring_writer_thread!=None:
      #    self.monitoring_writer_thread.terminate()
    def toString(self):
        return 'foo'
    def new_monitoring_record(self,record):
        self.monitoring_writer.writeMonitoringRecord(record)