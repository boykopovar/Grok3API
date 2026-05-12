from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Optional, Type
from enum import IntEnum


class WireType(Enum):
    BOOL = auto()
    OPT_BOOL = auto()
    INT32 = auto()
    INT64 = auto()
    FLOAT = auto()
    DOUBLE = auto()
    STRING = auto()
    MESSAGE = auto()
    REPEATED_STRING = auto()
    REPEATED_MESSAGE = auto()
    BYTES_FIELD = auto()
    TIMESTAMP = auto()
    MAP_IGNORED = auto()

    @property
    def is_repeated(self) -> bool:
        return self in (WireType.REPEATED_STRING, WireType.REPEATED_MESSAGE)

    @property
    def is_message(self) -> bool:
        return self in (WireType.MESSAGE, WireType.REPEATED_MESSAGE)

    @property
    def python_type(self) -> Type[Any]:
        if self in (WireType.BOOL, WireType.OPT_BOOL):
            return bool
        if self == WireType.INT32 or self == WireType.INT64:
            return int
        if self == WireType.FLOAT or self == WireType.DOUBLE:
            return float
        if self == WireType.STRING:
            return str
        if self == WireType.BYTES_FIELD:
            return bytes
        if self == WireType.TIMESTAMP:
            from datetime import datetime
            return datetime
        if self == WireType.MAP_IGNORED:
            return dict
        return object


@dataclass(frozen=True)
class ProtoField:
    tag: int
    wire: WireType
    cls: Optional[Type[Any]] = None


class StreamFrameTag(IntEnum):
    ADD_RESPONSE = 1
    CONVERSATION = 2
    TITLE = 3


class AddResponseTag(IntEnum):
    TOKEN = 2
    MODEL_RESPONSE = 3
    SIDE_BY_SIDE_INDEX = 14
    FINAL_METADATA = 15
    IS_THINKING = 16
    IS_SOFT_STOP = 17
    MESSAGE_TAG = 18
    MESSAGE_STEP_ID = 19
    RESPONSE_ID = 20
    STREAMING_METADATA = 29
    SURVEY = 41



