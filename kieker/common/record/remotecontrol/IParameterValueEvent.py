# since 1.15
# author Reiner Jung

# Modified by Natalie Kaufhold, 2026
from common.record.remotecontrol.IRemoteControlEvent import (
    IRemoteControlEvent,
)


class IParameterValueEvent (IRemoteControlEvent):
    def __init__(self, pattern, name, value):
        self.pattern = (""
            if pattern is None
            else pattern)
        self.name = (""
            if name is None
            else name)
        self.value = (""
            if value is None
            else value)
