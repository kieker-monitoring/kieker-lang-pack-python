# -*- coding: utf-8 -*-
# version 1.5
# author Andre van Hoorn, Jan Waller


class TimestampRecord:
	def __init__(self, timestamp):
		self.timestamp = timestamp

	def serialize(self, serializer):
		serializer.put_long(self.timestamp) 
	
	
