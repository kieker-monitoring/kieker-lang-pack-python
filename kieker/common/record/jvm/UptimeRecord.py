class UptimeRecord (AbstractJVMRecord, ) :
	def __init__(self, timestamp, hostname, vm_name, uptime_ms):	
		uptime_ms = uptime_ms

	def serialize(self, serializer):
		serializer.put_long(self.uptime_ms) 
	
	
