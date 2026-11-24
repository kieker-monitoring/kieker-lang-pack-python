# since 1.6
# author Jan Waller

# Modified by Natalie Kaufhold, 2026
from common.record.flow.IClassSignature import IClassSignature
from common.record.flow.IFlowRecord import IFlowRecord


class IObjectRecord (IFlowRecord, IClassSignature):
    def __init__(self, class_signature, object_id):
        self.class_signature = (self.CLASS_SIGNATURE
            if class_signature is None
            else class_signature)
        self.object_id = object_id
