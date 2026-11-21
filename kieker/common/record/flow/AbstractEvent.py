# -*- coding: utf-8 -*-
# version 1.5
# author Jan Waller

from kieker.common.record.flow.IEventRecord import IEventRecord

class AbstractEvent (IEventRecord):
	def __init__(self, timestamp):
		self.timestamp = timestamp

	def serialize(self, serializer):
		serializer.put_long(self.timestamp) 
	
	
