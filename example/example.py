# -*- coding: utf-8 -*-

from controller import MonitoringController
from common.records.DummyRecord import DummyRecord
from controller.WriterController import WriterController
from writer.FileWriter import FileWriter
from controller.MonitoringController import MonitoringController
def  function1():
    arr=[]
   
    record=DummyRecord("param1", "param2")
    writer=FileWriter("test8.log", arr)
    writer_cont=WriterController(writer)
    
    monit_cont=MonitoringController(writer_cont,None)
    
    monit_cont.new_monitoring_record(record)