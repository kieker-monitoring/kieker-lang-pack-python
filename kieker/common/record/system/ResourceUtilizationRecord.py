# since 1.3
# author Andre van Hoorn, Jan Waller



class ResourceUtilizationRecord:
    def __init__(self, timestamp, hostname, resource_name, utilization):
        self.timestamp = timestamp
        self.hostname = (self.HOSTNAME
            if hostname is None
            else hostname)
        self.resource_name = (self.RESOURCE_NAME
            if resource_name is None
            else resource_name)
        self.utilization = utilization

    def serialize(self, serializer):
        serializer.put_long(self.timestamp)
        serializer.put_string(self.hostname)
        serializer.put_string(self.resource_name)
        serializer.put_double(self.utilization)

