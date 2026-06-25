from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import Any, Optional, Type


class WireType(Enum):
    BOOL = auto()
    OPT_BOOL = auto()
    INT32 = auto()
    INT64 = auto()
    FLOAT = auto()
    DOUBLE = auto()
    STRING = auto()
    BYTES_FIELD = auto()
    TIMESTAMP = auto()
    MESSAGE = auto()
    REPEATED_STRING = auto()
    REPEATED_MESSAGE = auto()
    EMPTY_MESSAGE = auto()
    JSON_STRUCT = auto()
    JSON_VALUE = auto()
    FIELD_MASK = auto()
    MAP_FIELD = auto()

    @property
    def is_repeated(self) -> bool:
        return self in (WireType.REPEATED_STRING, WireType.REPEATED_MESSAGE)

    @property
    def is_message(self) -> bool:
        return self in (WireType.MESSAGE, WireType.REPEATED_MESSAGE)

    @property
    def python_type(self) -> Type[Any]:
        _map: dict = {
            WireType.BOOL: bool,
            WireType.OPT_BOOL: bool,
            WireType.INT32: int,
            WireType.INT64: int,
            WireType.FLOAT: float,
            WireType.DOUBLE: float,
            WireType.STRING: str,
            WireType.BYTES_FIELD: bytes,
            WireType.REPEATED_STRING: list,
            WireType.REPEATED_MESSAGE: list,
            WireType.EMPTY_MESSAGE: bool,
            WireType.JSON_STRUCT: dict,
            WireType.JSON_VALUE: object,
            WireType.FIELD_MASK: list,
            WireType.MAP_FIELD: dict,
        }
        if self == WireType.TIMESTAMP:
            return datetime
        return _map.get(self, object)

@dataclass(frozen=True)
class ProtoField:
    tag: int
    wire: WireType
    cls: Optional[Type[Any]] = None
    oneof_group: Optional[str] = None
    map_key_type: Optional[str] = None
    map_value_type: Optional[str] = None




