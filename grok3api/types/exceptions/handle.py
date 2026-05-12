from typing import Type, Optional

from aiohttp import ClientResponse

from grok3api.types.exceptions import *

_UNAVAILABLE_REGION_TEXT = 'This service is not available in your region.'

async def raise_for_rest(response: ClientResponse) -> None:
    if response.status != 200:
        raw = await response.text()
        error_type: Type[GrokRestError] = GrokRestError

        if _UNAVAILABLE_REGION_TEXT in raw:
            error_type = GrokUnavailableRegionError
            raw = _UNAVAILABLE_REGION_TEXT

        error_msg: str = f"HTTP {response.status}: {raw}"

        error = error_type(error_msg)
        error.status_code = response.status
        error.headers = response.headers

        raise error


def raise_for_grpc(response: ClientResponse) -> None:
    grpc_status = response.headers.get("grpc-status", "0")

    if grpc_status == "0":
        return

    message = str(response.headers.get("grpc-message", "?"))
    message = message.replace('%20', ' ')

    msg_lower = message.lower()
    error_msg = f"gRPC {grpc_status}: {message}"
    error_type: Type[GrokGrpcError] = GrokGrpcError

    if grpc_status == "8":
        error_type = GrokRateLimitError
        if 'under heavy usage' in msg_lower:
            error_type = GrokUnderHeavyUsageError

    error = error_type(error_msg)
    error.status_code = grpc_status
    error.message = message

    raise error