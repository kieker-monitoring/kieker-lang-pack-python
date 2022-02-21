# noqa: E402
# -*- coding: utf-8 -*-
import logging
from abc import ABC, abstractmethod
from monitoring.util import TimeStamp
from configparser import ConfigParser

class AbstractController(ABC):
    def __init__(self, domain, tcp_enabled, reader_thread, port,
                 terminated):
        self.domain = domain
        self.tcp_enabled = tcp_enabled
        self.reader_function = reader_thread
        self.port = port
        self.terminated = terminated
        self.logger = logging.getLogger('ControllerLogger')

    @abstractmethod
    def initialize(self):
        if self.tcp_enabled is True:
            self.logger.info('Start Thread reader')
            self.threading.start()

    @abstractmethod
    def cleanup(self):
        if self.tcp_enabled:
            self.logger.info('Terminate')

    @abstractmethod
    def toString(self):
        pass


class SingleMonitoringController(object):

    __instance = None
   
    def __new__(cls, config=None):
        if SingleMonitoringController.__instance is None:
            SingleMonitoringController.__instance = object.__new__(cls)
        if config is not None:
            SingleMonitoringController.__instance.writer_controller = WriterController(config)
            SingleMonitoringController.__instance.time_source_controller = TimeSourceController(TimeStamp())
        return SingleMonitoringController.__instance
        
        
    
    
#    def __init__(self, config):
 #       self.writer_controller = WriterController(config)
  #      self.time_source_controller = TimesourceController(TimeStamp())
    #def __init__(self, writer_controller=None, time_source_controller=None):
    #    if writer_controller is None:
    #        self.writer_controller = WriterController("./monitoring.log")
    #    else:
    #        self.writer_controller = WriterController()
    #    self.time_source_controller = TimeSourceController(TimeStamp())

    def new_monitoring_record(self, record):
        return self.writer_controller.new_monitoring_record(record)


class TimeSourceController(AbstractController):

    def __init__(self, time_source):
        # super().__init__()
        self.time_source = time_source
    
    def initialize(self):
        pass

    def cleanup(self):
        self.debug("shuttig down")

    def toString(self):
        pass
    
    def get_time(self):
        return self.time_source.get_time()


from monitoring.writer import FileWriter, TCPWriter
#from monitoring.tcpwriter import TCPWriter


class WriterController:

    def __init__(self, config, path=None):
        if config is not None:
            config_parser = ConfigParser()
            config_parser.read(config)
            if config_parser.getboolean('General', 'isTCP'):
                self.monitoring_writer = TCPWriter('127.0.0.1', 65432, [], 1000, config)
            else:
                self.monitoring_writer = FileWriter(config_parser.get('FileWriter', 'file_path'), [])
        else:
            self.monitoring_writer = TCPWriter('127.0.0.1', 65432, [], 1000)
        # if path is not None:
       #     self.monitoring_writer = FileWriter(path, [])
       # else:
       #     self.monitoring_writer = TCPWriter('127.0.0.1', 65432, [], 1000)

    def initialize(self):
        pass

    def cleanup(self):
        return 'foo'

    def new_monitoring_record(self, record):
        self.monitoring_writer.writeMonitoringRecord(record)
