# -*- coding: utf-8 -*-
import logging
from queue import Queue
import AbstractController
class WriterController(AbstractController):
    
    __PREFIX__="Prefix Foo"
    __RECORD_QUEUE_SIZE__ = "RecordQueueSize"
    __RECORD_QUEUE_INSERT_BEHAVIOR__ = "RecordQueueInsertBehavior"
    RECORD_QUEUE_FQN = "RecordQueueFQN"
    QUEUE_PUT_STRATEGY = "QueuePutStrategy"
    QUEUE_TAKE_STRATEGY = "QueueTakeStrategy"
    LOGGER=logging.getLogger
    
def __init__(self,log_metadata_record,queue_capacity,
             writer_queue, monitoring_writer,
             monitoring_writer_thread,
             domain, tcp_enabled, reader_thread, port, buffer_capacity,
             terminated):
    
        super.__init__(domain, tcp_enabled, reader_thread, port, buffer_capacity,
             terminated)    
        self.log_metadata_record=log_metadata_record
        self.queue_capacity=queue_capacity
        self.writer_queue=Queue(self.queue_capacity) ## original more complicated
        self.monitoring_writer=monitoring_writer
        self.monitoring_writer_thread=monitoring_writer_thread
        
 
def initialize(self):
      self.LOGGER.debug('Initialize')     
      if self.monitoring_writer_thread!=None:
          self.threading.Thread.start(self.monitoring_writer_thread)

def cleanup(self):
      self.LOGGER.debug('Initialize')     
      if self.monitoring_writer_thread!=None:
          self.monitoring_writer_thread.terminate()

def toString(self):
    return 'foo'
          
def new_monitoring_record(self,record):
              self.monitoring_writer.writeMonitoringRecord(record)