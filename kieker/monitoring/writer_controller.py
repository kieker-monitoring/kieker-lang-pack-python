# -*- coding: utf-8 -*-

from configparser import ConfigParser
from monitoring.writer import FileWriter, TCPWriter, DummyWriter


class WriterController:
    ''' This class is responsible for how the record data is written.
        Depending on the provided configuration, the files are either written
        directly into a local file or is send via TCP to the remote
        data collector'''

    def __init__(self, config, path=None):
        if config is not None:
            config_parser = ConfigParser()
            config_parser.read(config)
            if not config_parser.items:
                raise ValueError('File empty or could not be found.')
            mode = config_parser.get('Main', 'mode', fallback='text')
            if mode == 'tcp':
                self.monitoring_writer = TCPWriter(config)
            elif mode == 'text':
                self.monitoring_writer = FileWriter(
                    config_parser.get('FileWriter', 'file_path'), [])
            else:
                self.monitoring_writer = DummyWriter()
        else:
            raise ValueError('Path for configuration file was not provided.')

    def initialize(self):
        pass

    def cleanup(self):
        pass

    def new_monitoring_record(self, record):
        ''' Writes monitoring record.'''
        self.monitoring_writer.writeMonitoringRecord(record)
