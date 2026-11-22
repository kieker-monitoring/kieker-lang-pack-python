# since 1.6
# author Jan Waller

from kieker.common.record.flow.IFlowRecord import IFlowRecord


class IEventRecord (IFlowRecord):
    def __init__(self, timestamp):	
        self.timestamp = timestamp
