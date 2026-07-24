# noqa: E402
# -*- coding: utf-8 -*-
from monitoring.writer_controller import WriterController
import logging
from abc import ABC, abstractmethod
from monitoring.util import TimeStamp

# I think that calss can/should be removed. But in the future we might
# have more complex MonitoringController


class AbstractController(ABC):

    def __init__(self, domain, tcp_enabled, reader_thread, port, terminated):
        self.domain = domain
        self.tcp_enabled = tcp_enabled
        self.reader_thread = reader_thread
        self.port = port
        self.terminated = terminated
        self.logger = logging.getLogger('ControllerLogger')
        self.threading = None

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


class MonitoringController:
    ''' This class controlls the monitoring process. Only one instance of this
    class can exist at one time. '''
    __inst = None  # instance

    def __new__(cls, config=None):
        if MonitoringController.__inst is None:
            MonitoringController.__inst = object.__new__(cls)
        if config is not None:
            MonitoringController.__inst.write_ctrl = WriterController(
                config)
            MonitoringController.__inst.timesource_ctrl = TimeSourceController(
                TimeStamp())
        return MonitoringController.__inst

    def new_monitoring_record(self, record):
        ''' Delegates a record to a write_ctrl'''
        # This method is the same as
        # MonitoringController.__inst.write_ctrl.new_monitoring_record
        return self.write_ctrl.new_monitoring_record(record)


# This class can/should be removed since it does not provide something
# which cannot be achieved without it
class TimeSourceController(AbstractController):

    def __init__(self, time_source):

        self.time_source = time_source

    def initialize(self):
        pass

    def cleanup(self):
        pass

    def toString(self):
        pass

    def get_time(self):
        return self.time_source.get_time()
