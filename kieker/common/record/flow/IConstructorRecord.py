# since 1.8
# author Jan Waller

# Modified by Natalie Kaufhold, 2026
from common.record.flow.IOperationRecord import IOperationRecord


class IConstructorRecord (IOperationRecord):
    def __init__(self, operation_signature, class_signature):
        self.operation_signature = (self.OPERATION_SIGNATURE
            if operation_signature is None
            else operation_signature)
        self.class_signature = (self.CLASS_SIGNATURE
            if class_signature is None
            else class_signature)
