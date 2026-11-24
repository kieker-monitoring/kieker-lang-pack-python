# since 1.6
# author Jan Waller

# Modified by Natalie Kaufhold, 2026
from common.record.flow.IFlowRecord import IFlowRecord


class IEventRecord (IFlowRecord):
    def __init__(self, timestamp):
        self.timestamp = timestamp
