class MemoryRecord (AbstractJVMRecord, ) :
	def __init__(self, timestamp, hostname, vm_name, heap_max_bytes, heap_used_bytes, heap_committed_bytes, heap_init_bytes, non_heap_max_bytes, non_heap_used_bytes, non_heap_committed_bytes, non_heap_init_bytes, object_pending_finalization_count):	
		heap_max_bytes = heap_max_bytes
		heap_used_bytes = heap_used_bytes
		heap_committed_bytes = heap_committed_bytes
		heap_init_bytes = heap_init_bytes
		non_heap_max_bytes = non_heap_max_bytes
		non_heap_used_bytes = non_heap_used_bytes
		non_heap_committed_bytes = non_heap_committed_bytes
		non_heap_init_bytes = non_heap_init_bytes
		object_pending_finalization_count = object_pending_finalization_count

	def serialize(self, serializer):
		serializer.put_long(self.heap_max_bytes)
		serializer.put_long(self.heap_used_bytes)
		serializer.put_long(self.heap_committed_bytes)
		serializer.put_long(self.heap_init_bytes)
		serializer.put_long(self.non_heap_max_bytes)
		serializer.put_long(self.non_heap_used_bytes)
		serializer.put_long(self.non_heap_committed_bytes)
		serializer.put_long(self.non_heap_init_bytes)
		serializer.put_int(self.object_pending_finalization_count) 
	
	
