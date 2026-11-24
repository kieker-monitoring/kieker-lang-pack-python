# since 1.6
# author Jan Waller

# Modified by Natalie Kaufhold, 2026
from common.record.flow.IFlowRecord import IFlowRecord


class ITraceRecord (IFlowRecord):
    def __init__(self, trace_id, order_index):
        self.trace_id = trace_id
        self.order_index = order_index
