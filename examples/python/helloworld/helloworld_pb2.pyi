from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HelloRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class Number(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class Number2(_message.Message):
    __slots__ = ["value1", "value2"]
    VALUE1_FIELD_NUMBER: _ClassVar[int]
    VALUE2_FIELD_NUMBER: _ClassVar[int]
    value1: float
    value2: float
    def __init__(self, value1: _Optional[float] = ..., value2: _Optional[float] = ...) -> None: ...

class CalcResult(_message.Message):
    __slots__ = ["valueIn1", "valueIn2", "Result"]
    VALUEIN1_FIELD_NUMBER: _ClassVar[int]
    VALUEIN2_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    valueIn1: float
    valueIn2: float
    Result: float
    def __init__(self, valueIn1: _Optional[float] = ..., valueIn2: _Optional[float] = ..., Result: _Optional[float] = ...) -> None: ...
