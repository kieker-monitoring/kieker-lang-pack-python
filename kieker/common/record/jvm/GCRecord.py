# -*- coding: utf-8 -*-
# version 1.10
# author Nils Christian Ehmke

from kieker.common.record.jvm.AbstractJVMRecord import AbstractJVMRecord

class GCRecord (AbstractJVMRecord):
	def __init__(self, timestamp, hostname, vm_name, gc_name, collection_count, collection_time_ms):
		super().__init__(timestamp, hostname, vm_name)
		self.gc_name = (""
				      if gc_name is None 
				      else gc_name)
		self.collection_count = collection_count
		self.collection_time_ms = collection_time_ms

	def serialize(self, serializer):
		super().serialize(serializer)
		serializer.put_string(self.gc_name)
		serializer.put_long(self.collection_count)
		serializer.put_long(self.collection_time_ms) 
	
	
