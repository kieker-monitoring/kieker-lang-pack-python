# -*- coding: utf-8 -*-
import AbstractMonitoringWriter
class FileWriter(AbstractMonitoringWriter):
    def __init__(self,writer_registry):
        self.writer_registry=writer_registry
    
    def writeMonitoringRecord(self, monitring_record):
        pass