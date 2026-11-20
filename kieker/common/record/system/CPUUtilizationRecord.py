class CPUUtilizationRecord :
	def __init__(self, timestamp, hostname, cpu_id, user, system, wait, nice, irq, total_utilization, idle):	
		timestamp = timestamp
		hostname = (self.HOSTNAME
				      if hostname is None 
				      else hostname)
		cpu_id = (self.CPU_ID
				      if cpu_id is None 
				      else cpu_id)
		user = user
		system = system
		wait = wait
		nice = nice
		irq = irq
		total_utilization = total_utilization
		idle = idle

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
	
	
