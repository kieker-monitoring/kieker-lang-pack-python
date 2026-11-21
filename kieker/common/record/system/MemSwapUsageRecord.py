# -*- coding: utf-8 -*-
# version 1.3
# author Andre van Hoorn, Jan Waller


class MemSwapUsageRecord:
	def __init__(self, timestamp, hostname, mem_total, mem_used, mem_free, swap_total, swap_used, swap_free):
		self.timestamp = timestamp
		self.hostname = (self.HOSTNAME
			if hostname is None 
			else hostname)
		self.mem_total = mem_total
		self.mem_used = mem_used
		self.mem_free = mem_free
		self.swap_total = swap_total
		self.swap_used = swap_used
		self.swap_free = swap_free

	def serialize(self, serializer):
		serializer.put_long(self.timestamp)
		serializer.put_string(self.hostname)
		serializer.put_long(self.mem_total)
		serializer.put_long(self.mem_used)
		serializer.put_long(self.mem_free)
		serializer.put_long(self.swap_total)
		serializer.put_long(self.swap_used)
		serializer.put_long(self.swap_free) 
	
	
