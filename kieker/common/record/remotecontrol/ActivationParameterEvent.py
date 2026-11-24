# since 1.14
# author Marc Adolf

# Modified by Natalie Kaufhold, 2026
from common.record.remotecontrol.IRemoteParameterControlEvent import (
    IRemoteParameterControlEvent,
)


class ActivationParameterEvent (IRemoteParameterControlEvent):
    def __init__(self, pattern, name, values):
        self.pattern = (""
            if pattern is None
            else pattern)
        self.name = (""
            if name is None
            else name)
        self.values = values

    def serialize(self, serializer):
        serializer.put_string(self.pattern)
        serializer.put_string(self.name)
        serializer.put_string(self.values)

