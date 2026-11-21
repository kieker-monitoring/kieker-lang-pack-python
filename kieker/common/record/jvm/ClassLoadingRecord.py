# version 1.10
# author Nils Christian Ehmke

from kieker.common.record.jvm.AbstractJVMRecord import AbstractJVMRecord


class ClassLoadingRecord (AbstractJVMRecord):
	def __init__(self, timestamp, hostname, vm_name, total_loaded_class_count, loaded_class_count, unloaded_class_count):
		super().__init__(timestamp, hostname, vm_name)
		self.total_loaded_class_count = total_loaded_class_count
		self.loaded_class_count = loaded_class_count
		self.unloaded_class_count = unloaded_class_count

	def serialize(self, serializer):
		super().serialize(serializer)
		serializer.put_long(self.total_loaded_class_count)
		serializer.put_int(self.loaded_class_count)
		serializer.put_long(self.unloaded_class_count) 
	
	
