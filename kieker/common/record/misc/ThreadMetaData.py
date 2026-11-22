# since 1.13
# author Christian Wulf



class ThreadMetaData:
    def __init__(self, hostname, thread_id):
        self.hostname = (""
            if hostname is None 
            else hostname)
        self.thread_id = thread_id

    def serialize(self, serializer):
        serializer.put_string(self.hostname)
        serializer.put_long(self.thread_id) 

