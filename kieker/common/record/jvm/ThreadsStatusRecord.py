class ThreadsStatusRecord (AbstractJVMRecord, ) :
	def __init__(self, timestamp, hostname, vm_name, thread_count, daemon_thread_count, peak_thread_count, total_started_thread_count):	
		thread_count = thread_count
		daemon_thread_count = daemon_thread_count
		peak_thread_count = peak_thread_count
		total_started_thread_count = total_started_thread_count

	def serialize(self, serializer):
		serializer.put_long(self.thread_count)
		serializer.put_long(self.daemon_thread_count)
		serializer.put_long(self.peak_thread_count)
		serializer.put_long(self.total_started_thread_count) 
	
	
