from datetime import datetime, timezone
from typing import Any, Dict, Optional, Type, TypeVar

from pydantic import BaseModel

from grok3api.types.pb_meta import ProtoField, WireType
from grok3api.utils.protobuf import pb_parse, pb_bool, pb_bytes, pb_double, pb_float, pb_int32, pb_str


T = TypeVar("T")


def _encode_varint(value: int) -> bytes:
    value &= (1 << 64) - 1 if value < 0 else value
    out = bytearray()
    while True:
        b = value & 0x7F
        value >>= 7
        if value:
            out.append(b | 0x80)
        else:
            out.append(b)
            return bytes(out)


def _encode_timestamp(value: datetime) -> bytes:
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    value = value.astimezone(timezone.utc)
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
    delta = value - epoch
    seconds = int(delta.total_seconds())
    nanos = value.microsecond * 1000
    out = bytearray()
    out += _encode_varint((1 << 3) | 0)
    out += _encode_varint(seconds)
    out += _encode_varint((2 << 3) | 0)
    out += _encode_varint(nanos)
    return bytes(out)


def _find_proto(field_info: Any) -> Optional[ProtoField]:
    for item in getattr(field_info, "metadata", ()):
        if isinstance(item, ProtoField):
            return item
    return None


def _encode_field(tag: int, wire: WireType, value: Any, cls: Optional[Type[Any]]) -> bytes:
    if wire == WireType.BOOL:
        return pb_bool(tag, bool(value))
    if wire == WireType.OPT_BOOL:
        if value is None:
            return b""
        return pb_bool(tag, bool(value))
    if wire == WireType.INT32 or wire == WireType.INT64:
        return pb_int32(tag, int(value))
    if wire == WireType.FLOAT:
        return pb_float(tag, float(value))
    if wire == WireType.DOUBLE:
        return pb_double(tag, float(value))
    if wire == WireType.STRING:
        if value is None or value == "":
            return b""
        return pb_str(tag, str(value))
    if wire == WireType.BYTES_FIELD:
        if value is None or value == b"":
            return b""
        return pb_bytes(tag, value)
    if wire == WireType.MESSAGE:
        if value is None:
            return b""
        return pb_bytes(tag, encode_message(value))
    if wire == WireType.REPEATED_STRING:
        if not value:
            return b""
        out = bytearray()
        for item in value:
            if item is None:
                continue
            out += pb_str(tag, str(item))
        return bytes(out)
    if wire == WireType.REPEATED_MESSAGE:
        if not value:
            return b""
        out = bytearray()
        for item in value:
            if item is None:
                continue
            out += pb_bytes(tag, encode_message(item))
        return bytes(out)
    if wire == WireType.TIMESTAMP:
        if value is None:
            return b""
        return pb_bytes(tag, _encode_timestamp(value))
    if wire == WireType.MAP_IGNORED:
        return b""
    raise ValueError("unknown wire type: {!r}".format(wire))


def encode_message(model: BaseModel) -> bytes:
    out = bytearray()
    model_cls = model.__class__
    for fname, field_info in model_cls.model_fields.items():
        proto = _find_proto(field_info)
        if proto is None:
            continue
        value = getattr(model, fname)
        if value is None and proto.wire not in (WireType.OPT_BOOL, WireType.MESSAGE, WireType.REPEATED_STRING, WireType.REPEATED_MESSAGE, WireType.TIMESTAMP):
            continue
        out += _encode_field(proto.tag, proto.wire, value, proto.cls)
    return bytes(out)


def _decode_timestamp(raw: bytes) -> Optional[datetime]:
    if not raw:
        return None
    d = pb_parse(raw)
    seconds = int(d.get(1, [0])[0])
    nanos = int(d.get(2, [0])[0]) if 2 in d else 0
    return datetime.fromtimestamp(seconds + nanos / 1e9, tz=timezone.utc)


def _decode_scalar(raw: Any, wire: WireType, cls: Optional[Type[Any]]) -> Any:
    if wire == WireType.STRING:
        if isinstance(raw, (bytes, bytearray)):
            return raw.decode("utf-8", errors="replace")
        return "" if raw is None else str(raw)
    if wire == WireType.BOOL or wire == WireType.OPT_BOOL:
        return bool(raw)
    if wire == WireType.INT32 or wire == WireType.INT64:
        return int(raw)
    if wire == WireType.FLOAT:
        return float(raw)
    if wire == WireType.DOUBLE:
        return float(raw)
    if wire == WireType.BYTES_FIELD:
        return raw
    if wire == WireType.MESSAGE:
        if cls is None:
            raise TypeError("message wire type requires cls")
        return decode_message(cls, raw)
    if wire == WireType.TIMESTAMP:
        return _decode_timestamp(raw)
    if wire == WireType.MAP_IGNORED:
        return {}
    return raw


def decode_message(cls: Type[T], buf: bytes) -> T:
    d = pb_parse(buf)
    kwargs: Dict[str, Any] = {}

    for fname, field_info in cls.model_fields.items():
        proto = _find_proto(field_info)
        if proto is None:
            continue

        raw_list = d.get(proto.tag, [])

        if proto.wire == WireType.REPEATED_MESSAGE:
            if proto.cls is None:
                raise TypeError(f"{cls.__name__}.{fname}: repeated message requires cls")
            items = []
            for item in raw_list:
                if not isinstance(item, (bytes, bytearray, memoryview)):
                    raise TypeError(
                        f"{cls.__name__}.{fname}: expected bytes for nested message, got {type(item).__name__}={item!r}"
                    )
                items.append(decode_message(proto.cls, bytes(item)))
            kwargs[fname] = items
            continue

        if proto.wire == WireType.REPEATED_STRING:
            kwargs[fname] = [
                item.decode("utf-8", errors="replace") if isinstance(item, (bytes, bytearray)) else str(item)
                for item in raw_list
            ]
            continue

        if proto.wire == WireType.MAP_IGNORED:
            kwargs[fname] = {}
            continue

        if not raw_list:
            continue

        kwargs[fname] = _decode_scalar(raw_list[0], proto.wire, proto.cls)

    return cls(**kwargs)