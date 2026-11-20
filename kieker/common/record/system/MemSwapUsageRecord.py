class MemSwapUsageRecord :
	def __init__(self, timestamp, hostname, mem_total, mem_used, mem_free, swap_total, swap_used, swap_free):	
		timestamp = timestamp
		hostname = (self.HOSTNAME
				      if hostname is None 
				      else hostname)
		mem_total = mem_total
		mem_used = mem_used
		mem_free = mem_free
		swap_total = swap_total
		swap_used = swap_used
		swap_free = swap_free

	def serialize(self, serializer):
		serializer.put_long(self.timestamp)
		serializer.put_string(self.hostname)
		serializer.put_long(self.mem_total)
		serializer.put_long(self.mem_used)
		serializer.put_long(self.mem_free)
		serializer.put_long(self.swap_total)
		serializer.put_long(self.swap_used)
		serializer.put_long(self.swap_free) 
	
	
