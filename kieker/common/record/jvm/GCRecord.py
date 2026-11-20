class GCRecord (AbstractJVMRecord, ) :
	def __init__(self, timestamp, hostname, vm_name, gc_name, collection_count, collection_time_ms):	
		gc_name = (""
				      if gc_name is None 
				      else gc_name)
		collection_count = collection_count
		collection_time_ms = collection_time_ms

	def serialize(self, serializer):
		serializer.put_string(self.gc_name)
		serializer.put_long(self.collection_count)
		serializer.put_long(self.collection_time_ms) 
	
	
