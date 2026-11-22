# since 1.5
# author Jan Waller

from kieker.common.record.flow.IFlowRecord import IFlowRecord


class TraceMetadata (IFlowRecord):
    NO_PARENT_TRACEID = -1
    NO_PARENT_ORDER_INDEX = -1
    NO_SESSION_ID = "<no-session-id>"
    NO_HOSTNAME = "<default-host>"
    def __init__(self, trace_id, thread_id, session_id, hostname, parent_trace_id, parent_order_id):
        self.trace_id = trace_id
        self.thread_id = thread_id
        self.session_id = (self.NO_SESSION_ID
            if session_id is None 
            else session_id)
        self.hostname = (self.NO_HOSTNAME
            if hostname is None 
            else hostname)
        self.parent_trace_id = parent_trace_id
        self.parent_order_id = parent_order_id
        self.next_order_id = 0

    def serialize(self, serializer):
        serializer.put_long(self.trace_id)
        serializer.put_long(self.thread_id)
        serializer.put_string(self.session_id)
        serializer.put_string(self.hostname)
        serializer.put_long(self.parent_trace_id)
        serializer.put_int(self.parent_order_id) 

    def get_next_order_id(self):
        self.next_order_id +=1
        return self.next_order_id
