# since 1.10
# author Nils Christian Ehmke



class AbstractJVMRecord:
    def __init__(self, timestamp, hostname, vm_name):
        self.timestamp = timestamp
        self.hostname = (""
            if hostname is None
            else hostname)
        self.vm_name = (""
            if vm_name is None
            else vm_name)

    def serialize(self, serializer):
        serializer.put_long(self.timestamp)
        serializer.put_string(self.hostname)
        serializer.put_string(self.vm_name)

