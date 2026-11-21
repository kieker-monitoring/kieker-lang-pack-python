# -*- coding: utf-8 -*-
# version 1.10
# author Nils Christian Ehmke

from kieker.common.record.jvm.AbstractJVMRecord import AbstractJVMRecord

class ThreadsStatusRecord (AbstractJVMRecord):
	def __init__(self, timestamp, hostname, vm_name, thread_count, daemon_thread_count, peak_thread_count, total_started_thread_count):
		super().__init__(timestamp, hostname, vm_name)
		self.thread_count = thread_count
		self.daemon_thread_count = daemon_thread_count
		self.peak_thread_count = peak_thread_count
		self.total_started_thread_count = total_started_thread_count

	def serialize(self, serializer):
		super().serialize(serializer)
		serializer.put_long(self.thread_count)
		serializer.put_long(self.daemon_thread_count)
		serializer.put_long(self.peak_thread_count)
		serializer.put_long(self.total_started_thread_count) 
	
	
