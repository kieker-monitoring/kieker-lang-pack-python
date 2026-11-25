# since 1.6
# author Jan Waller

from kieker.common.record.flow.IOperationRecord import IOperationRecord


class ICallRecord (IOperationRecord):
    def __init__(self, operation_signature, class_signature, callee_operation_signature, callee_class_signature):
        self.operation_signature = (self.OPERATION_SIGNATURE
            if operation_signature is None
            else operation_signature)
        self.class_signature = (self.CLASS_SIGNATURE
            if class_signature is None
            else class_signature)
        self.caller_operation_signature = self.operation_signature
        self.caller_class_signature = self.class_signature
        self.callee_operation_signature = (self.CALLEE_OPERATION_SIGNATURE
            if callee_operation_signature is None
            else callee_operation_signature)
        self.callee_class_signature = (self.CALLEE_CLASS_SIGNATURE
            if callee_class_signature is None
            else callee_class_signature)
