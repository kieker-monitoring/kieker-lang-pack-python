# -*- coding: utf-8 -*-
# version 1.3
# author Andre van Hoorn, Jan Waller


class CPUUtilizationRecord:
	def __init__(self, timestamp, hostname, cpu_id, user, system, wait, nice, irq, total_utilization, idle):
		self.timestamp = timestamp
		self.hostname = (self.HOSTNAME
				      if hostname is None 
				      else hostname)
		self.cpu_id = (self.CPU_ID
				      if cpu_id is None 
				      else cpu_id)
		self.user = user
		self.system = system
		self.wait = wait
		self.nice = nice
		self.irq = irq
		self.total_utilization = total_utilization
		self.idle = idle

	def serialize(self, serializer):
		serializer.put_long(self.timestamp)
		serializer.put_string(self.hostname)
		serializer.put_string(self.cpu_id)
		serializer.put_double(self.user)
		serializer.put_double(self.system)
		serializer.put_double(self.wait)
		serializer.put_double(self.nice)
		serializer.put_double(self.irq)
		serializer.put_double(self.total_utilization)
		serializer.put_double(self.idle) 
	
	
