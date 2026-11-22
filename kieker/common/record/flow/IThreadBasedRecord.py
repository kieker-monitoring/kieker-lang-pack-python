# since 1.13
# author Christian Wulf

from kieker.common.record.flow.IFlowRecord import IFlowRecord


class IThreadBasedRecord (IFlowRecord):
    def __init__(self, thread_id, order_index):	
        self.thread_id = thread_id
        self.order_index = order_index
