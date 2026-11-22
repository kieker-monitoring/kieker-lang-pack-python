# since 2.0.0
# author Reiner Jung

from kieker.common.record.flow.IEventRecord import IEventRecord
from kieker.common.record.session.ISessionEvent import ISessionEvent


class SessionEndEvent (IEventRecord, ISessionEvent):
    def __init__(self, timestamp, hostname, session_id):
        self.timestamp = timestamp
        self.hostname = (""
            if hostname is None 
            else hostname)
        self.session_id = (""
            if session_id is None 
            else session_id)

    def serialize(self, serializer):
        serializer.put_long(self.timestamp)
        serializer.put_string(self.hostname)
        serializer.put_string(self.session_id) 

