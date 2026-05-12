from typing import Any, Dict, List, Optional, Type, TypeVar

from grok3api.types.pb_meta import WireType
from grok3api.utils.pb_serializer import decode_message

T = TypeVar("T")


def get_meta_type(
    d: Dict[int, List[Any]],
    tag: int,
    wire: WireType,
    cls: Optional[Type[T]] = None,
) -> Any:
    values = d.get(tag)

    if not values:
        return None

    raw = values[0]

    if wire == WireType.STRING:
        if isinstance(raw, (bytes, bytearray)):
            return raw.decode("utf-8", errors="replace")
        return str(raw)

    if wire == WireType.BOOL:
        return bool(raw)

    if wire == WireType.OPT_BOOL:
        return bool(raw)

    if wire == WireType.INT32:
        return int(raw)

    if wire == WireType.INT64:
        return int(raw)

    if wire == WireType.FLOAT:
        return float(raw)

    if wire == WireType.DOUBLE:
        return float(raw)

    if wire == WireType.MESSAGE:
        if cls is None:
            raise TypeError("MESSAGE wire requires cls")
        return decode_message(cls, raw)

    if wire == WireType.BYTES_FIELD:
        return bytes(raw)

    return raw