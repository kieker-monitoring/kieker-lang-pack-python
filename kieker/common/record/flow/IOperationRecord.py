# since 1.5
# author Jan Waller

from kieker.common.record.flow.IClassSignature import IClassSignature
from kieker.common.record.flow.IFlowRecord import IFlowRecord
from kieker.common.record.flow.IOperationSignature import IOperationSignature


class IOperationRecord (IFlowRecord, IOperationSignature, IClassSignature):
    def __init__(self, operation_signature, class_signature):
        self.operation_signature = (self.OPERATION_SIGNATURE
            if operation_signature is None
            else operation_signature)
        self.class_signature = (self.CLASS_SIGNATURE
            if class_signature is None
            else class_signature)
