# version 1.14
# author Marc Adolf

from kieker.common.record.remotecontrol.IRemoteControlEvent import IRemoteControlEvent


class ActivationEvent (IRemoteControlEvent):
	def __init__(self, pattern):
		self.pattern = (""
			if pattern is None 
			else pattern)

	def serialize(self, serializer):
		serializer.put_string(self.pattern) 
	
	
