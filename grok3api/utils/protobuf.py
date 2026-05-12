import struct
from typing import Optional, Dict, List, Tuple


def _varint(n: int) -> bytes:
    out = []
    while True:
        bits = n & 0x7F
        n >>= 7
        out.append(bits | 0x80 if n else bits)
        if not n:
            return bytes(out)


def _read_varint(buf: bytes, pos: int) -> Tuple[int, int]:
    result = 0
    shift = 0
    while pos < len(buf):
        b = buf[pos]
        pos += 1
        result |= (b & 0x7F) << shift
        shift += 7
        if not (b & 0x80):
            return result, pos
    raise ValueError("truncated varint")

def grpc_frame(pb: bytes) -> bytes:
    return b"\x00" + struct.pack(">I", len(pb)) + pb

def pb_parse(buf: bytes) -> Dict[int, List]:
    out: Dict[int, List] = {}
    pos = 0
    while pos < len(buf):
        tag, pos = _read_varint(buf, pos)
        field, wire = tag >> 3, tag & 7
        if wire == 0:
            val, pos = _read_varint(buf, pos)
        elif wire == 1:
            val, pos = buf[pos:pos + 8], pos + 8
        elif wire == 2:
            ln, pos = _read_varint(buf, pos)
            val, pos = buf[pos:pos + ln], pos + ln
        elif wire == 5:
            val, pos = buf[pos:pos + 4], pos + 4
        else:
            raise ValueError(f"unsupported wire type {wire}")
        out.setdefault(field, []).append(val)
    return out


def pb_bool(field: int, v: bool) -> bytes:
    return _varint((field << 3) | 0) + _varint(int(v))


def pb_int32(field: int, n: int) -> bytes:
    return _varint((field << 3) | 0) + _varint(n)


def pb_double(field: int, v: float) -> bytes:
    return _varint((field << 3) | 1) + struct.pack("<d", v)


def pb_float(field: int, v: float) -> bytes:
    return _varint((field << 3) | 5) + struct.pack("<f", v)


def pb_bytes(field: int, d: bytes) -> bytes:
    return _varint((field << 3) | 2) + _varint(len(d)) + d


def pb_str(field: int, s: str) -> bytes:
    return pb_bytes(field, s.encode())


def pb_opt_bool(field: int, v: Optional[bool]) -> bytes:
    return pb_bool(field, v) if v is not None else b""