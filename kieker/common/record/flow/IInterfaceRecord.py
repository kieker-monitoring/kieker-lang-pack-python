# since 1.10
# author Florian Fittkau

# Modified by Natalie Kaufhold, 2026
from common.record.flow.IFlowRecord import IFlowRecord


class IInterfaceRecord (IFlowRecord):
    def __init__(self, interface):
        self.interface = (""
            if interface is None
            else interface)
