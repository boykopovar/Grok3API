import base64
import random
import time
from typing import List, Tuple

_PUBLISHABLE_KEY: str = "pk_AkuAxjNpHK138D2yUio6J5BAJHpoN5xX"
_APP_VERSION: str = "10.38.0"
_BUILD_ID: str = "UQ1A.240105.004"
_ANDROID_VERSION: str = "14"
_API_LEVEL: int = 34
_DEVICE_TYPE: int = 3
_LOCALE: str = "en-US"
_LOCALE_LIST: str = "en-US"
_LOCALE_TAGS: str = "en-US"
_DEVICE_NAME: str = "sdk_gphone64_x86_64"
_APP_LABEL: str = "Grok"
_DEVICE_ID: str = "f8a3c2d1e4b50967"
_DEVICE_ID2: str = "a1b2c3d4e5f60718"
_SCREEN_WIDTH_PX: int = 1080
_SCREEN_HEIGHT_PX: int = 1920
_SCREEN_DENSITY: float = 2.0
_RAM_MB: float = 3900.0
_CPU_CORES: int = 8
_TOUCH_PRESSURE: int = 0
_CAPABILITIES: int = 0b1000000001
_BATTERY_LEVEL: int = 50
_BATTERY_CHARGING: int = 0
_FONT_SCALE: float = 1.0
_SENSOR_EVENT_COUNT: int = 0

_TS_OFFSET: int = 0x5B7E3DC0
_TS_CLAMP: int = 0x0FFFFFFF

_HEX: List[str] = list("0123456789abcdef")


def _h(i: int) -> str:
    return "%02x" % (i & 0xFF)


def _i(i: int, width: int) -> str:
    return ("%0" + str(width * 2) + "x") % (i & ((1 << (width * 8)) - 1))


def _j(s: str) -> str:
    return "".join(_h(ord(c)) for c in s)


def _g(c: str) -> int:
    if "0" <= c <= "9":
        return ord(c) - ord("0")
    if "a" <= c <= "f":
        return ord(c) - ord("a") + 10
    if "A" <= c <= "F":
        return ord(c) - ord("A") + 10
    return -1


def _compute_k_e(version: str) -> str:
    parts = version.split(".")
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
    val = (patch & 63) | ((major - 1 & 3) << 11) | 0x4000 | ((minor & 31) << 6)
    return _i(val, 2)


_K_B: str = _h(10)
_K_C: str = _h(255)
_K_D: str = _PUBLISHABLE_KEY.replace("-", "")
_K_E: str = _compute_k_e(_APP_VERSION)
_K_D_UPPER_HEX: str = _j(_K_D).upper()


def _encode_screen(width_px: int, height_px: int, density: float) -> str:
    w = int(width_px / density) | 0x8000
    h = int(height_px / density) | 0x8000
    return _h(w >> 8) + _h(w) + _h(h >> 8) + _h(h)


def _encode_capabilities(bitmap: int) -> str:
    return _h(0xA) + _i(bitmap, 2)


def _encode_float_signal(val: float) -> str:
    clamped = max(-(2 ** 31), min(int(val * 1e5), 2 ** 31 - 1))
    return _i(clamped, 4)


def _build_signals() -> List[Tuple[int, str]]:
    boot_offset = int(time.time()) - _TS_OFFSET
    return [
        (0x00, _h(_DEVICE_TYPE)),
        (0x01, _j(_BUILD_ID)),
        (0x02, _j(_LOCALE)),
        (0x03, _encode_float_signal(_RAM_MB)),
        (0x04, _encode_screen(_SCREEN_WIDTH_PX, _SCREEN_HEIGHT_PX, _SCREEN_DENSITY)),
        (0x05, _h(_CPU_CORES)),
        (0x06, _i(_TOUCH_PRESSURE, 2)),
        (0x07, _encode_float_signal(_SCREEN_DENSITY)),
        (0x08, _j(_DEVICE_ID)),
        (0x09, _j(_DEVICE_ID2)),
        (0x0A, _encode_capabilities(_CAPABILITIES)),
        (0x0B, _j(_ANDROID_VERSION)),
        (0x0C, _j("Android")),
        (0x0F, _j(_APP_LABEL)),
        (0x11, _j(_APP_VERSION)),
        (0x12, _h(_BATTERY_LEVEL)),
        (0x13, _h(_BATTERY_CHARGING)),
        (0x18, _encode_float_signal(_FONT_SCALE)),
        (0x19, _h(_API_LEVEL)),
        (0x1A, _j(_DEVICE_ID2)),
        (0x1B, _j(_LOCALE_LIST)),
        (0x1D, _j(_DEVICE_NAME)),
        (0x1E, _j(_LOCALE_TAGS)),
        (0x1F, _i(boot_offset & 0xFFFFFFFF, 4)),
        (0x20, _h(_SENSOR_EVENT_COUNT)),
    ]


def _serialize_signals(signals: List[Tuple[int, str]]) -> str:
    return "".join(_h(tag) + _h(len(val) // 2) + val for tag, val in signals)


def gen_castle_token() -> str:
    ts_raw: int = int(time.time()) - _TS_OFFSET
    ts: int = max(0, min(ts_raw, _TS_CLAMP))

    rand_key_hex: str = _h(random.randint(0, 254))
    rand_nibble: str = _HEX[random.randint(0, 15) & 0xF]

    signals: List[Tuple[int, str]] = _build_signals()
    signals_hex: str = _serialize_signals(signals)

    version_payload: str = _i(len(_K_D), 3) + _j(_K_D)
    payload_body: str = version_payload + _h(len(signals)) + signals_hex

    ts_hex: str = _h(ts >> 24) + _h(ts >> 16) + _h(ts >> 8) + _h(ts)
    ts_nibble: str = ts_hex + rand_nibble

    payload_with_term: str = payload_body + _K_C

    inner_v: str = ts_nibble[:4] + ts_nibble[3] + payload_with_term

    scrambled: str = _K_D_UPPER_HEX[:8] + _K_D_UPPER_HEX[8] + ts_nibble + inner_v

    pre_assembly: str = _h(0x30) + scrambled

    assembly: str = _K_B + signals_hex + _K_E + _K_D + pre_assembly

    final_plain: str = (assembly + _h(len(assembly) & 0xFF)).lower()

    key_len: int = len(rand_key_hex)
    encrypted: str = "".join(
        _HEX[_g(final_plain[idx]) ^ _g(rand_key_hex[idx % key_len])]
        for idx in range(len(final_plain))
    )

    token_raw: str = rand_key_hex + encrypted
    return base64.b64encode(token_raw.encode(), altchars=b"-_").decode().rstrip("=")


if __name__ == "__main__":
    print(gen_castle_token())
