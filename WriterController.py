# -*- coding: utf-8 -*-
import logging
from queue import Queue
import threading.Thread
class WriterController:
    PREFIX="Prefix Foo"
    RECORD_QUEUE_SIZE = "RecordQueueSize"
    RECORD_QUEUE_INSERT_BEHAVIOR = "RecordQueueInsertBehavior"
    RECORD_QUEUE_FQN = "RecordQueueFQN"
    QUEUE_PUT_STRATEGY = "QueuePutStrategy"
    QUEUE_TAKE_STRATEGY = "QueueTakeStrategy"
    LOGGER=logging.getLogger
    
def __init__(self,log_metadata_record,queue_capacity,
             writer_queue, monitoring_writer,
             monitoring_writer_thread):
        self.log_metadata_record=log_metadata_record
        self.queue_capacity=queue_capacity
        self.writer_queue=Queue(self.queue_capacity) ## original mor complicated
        self.monitoring_writer=monitoring_writer
        self.monitoring_writer_thread=monitoring_writer_thread
        
 
def initialize(self):
      self.LOGGER.debug('Initialize')     
      if self.monitoring_writer_thread!=None:
          self.monitoring_writer_thread.start()

def cleanup(self):
      self.LOGGER.debug('Initialize')     
      if self.monitoring_writer_thread!=None:
          self.monitoring_writer_thread.terminate()

def toString(self):
    return 'foo'
          
          