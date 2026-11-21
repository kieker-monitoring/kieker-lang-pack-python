# -*- coding: utf-8 -*-
# version 1.15
# author Reiner Jung

from kieker.common.record.remotecontrol.IParameterValueEvent import IParameterValueEvent

class AddParameterValueEvent (IParameterValueEvent):
	def __init__(self, pattern, name, value):
		self.pattern = (""
			if pattern is None 
			else pattern)
		self.name = (""
			if name is None 
			else name)
		self.value = (""
			if value is None 
			else value)

	def serialize(self, serializer):
		serializer.put_string(self.pattern)
		serializer.put_string(self.name)
		serializer.put_string(self.value) 
	
	
