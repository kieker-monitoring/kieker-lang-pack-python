# since 1.12
# author Teerat Pitakrat



class DiskUsageRecord:
    def __init__(self, timestamp, hostname, device_name, queue, read_bytes_per_second, reads_per_second, service_time, write_bytes_per_second, writes_per_second):
        self.timestamp = timestamp
        self.hostname = (self.HOSTNAME
            if hostname is None 
            else hostname)
        self.device_name = (self.DEVICE_NAME
            if device_name is None 
            else device_name)
        self.queue = queue
        self.read_bytes_per_second = read_bytes_per_second
        self.reads_per_second = reads_per_second
        self.service_time = service_time
        self.write_bytes_per_second = write_bytes_per_second
        self.writes_per_second = writes_per_second

    def serialize(self, serializer):
        serializer.put_long(self.timestamp)
        serializer.put_string(self.hostname)
        serializer.put_string(self.device_name)
        serializer.put_double(self.queue)
        serializer.put_double(self.read_bytes_per_second)
        serializer.put_double(self.reads_per_second)
        serializer.put_double(self.service_time)
        serializer.put_double(self.write_bytes_per_second)
        serializer.put_double(self.writes_per_second) 

