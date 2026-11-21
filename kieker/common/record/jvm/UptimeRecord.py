# -*- coding: utf-8 -*-
# version 1.10
# author Nils Christian Ehmke

from kieker.common.record.jvm.AbstractJVMRecord import AbstractJVMRecord

class UptimeRecord (AbstractJVMRecord):
	def __init__(self, timestamp, hostname, vm_name, uptime_ms):
		super().__init__(timestamp, hostname, vm_name)
		self.uptime_ms = uptime_ms

	def serialize(self, serializer):
		super().serialize(serializer)
		serializer.put_long(self.uptime_ms) 
	
	
