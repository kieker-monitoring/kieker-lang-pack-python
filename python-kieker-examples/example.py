# -*- coding: utf-8 -*-


from src.Record import DummyRecord
from src.Controller import WriterController, MonitoringController
from src.Writer import FileWriter
from src.Controller import MonitoringController
def  test_file_writer():   
    record=DummyRecord("param1", "param2")
   
    writer_cont=WriterController("aa.log")
    
    monit_cont=MonitoringController(writer_cont,None)
    
    monit_cont.new_monitoring_record(record)

def  test_tcp_writer():
    record=DummyRecord("param1", "param2")
    writer_cont=WriterController(None)
    monit_cont=MonitoringController(writer_cont,None)
    monit_cont.new_monitoring_record(record)