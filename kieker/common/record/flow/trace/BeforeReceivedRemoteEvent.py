# since 1.14
# author Felix Eichhorst



class BeforeReceivedRemoteEvent:
    def __init__(self, timestamp, caller_trace_id, caller_order_index, trace_id, order_index):
        self.timestamp = timestamp
        self.caller_trace_id = caller_trace_id
        self.caller_order_index = caller_order_index
        self.trace_id = trace_id
        self.order_index = order_index

    def serialize(self, serializer):
        serializer.put_long(self.timestamp)
        serializer.put_long(self.caller_trace_id)
        serializer.put_int(self.caller_order_index)
        serializer.put_long(self.trace_id)
        serializer.put_int(self.order_index) 

