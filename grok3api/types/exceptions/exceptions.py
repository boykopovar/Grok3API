from typing import List

from multidict import CIMultiDictProxy

from grok3api.types.response import StreamError


class GrokApiError(Exception):
    pass

class GrokRestError(GrokApiError):
    status_code: int
    headers: CIMultiDictProxy[str]

class GrokUnavailableRegionError(GrokRestError):
    pass

class GrokGrpcError(GrokApiError):
    status_code: str

class GrokRateLimitError(GrokGrpcError):
    pass

class GrokUnderHeavyUsageError(GrokRateLimitError):
    message: str


class GrokStreamError(GrokApiError):
    def __init__(self, error: StreamError):
        self.error = error
        data = error.model_dump()

        for key, value in data.items():
            setattr(self, key, value)

        super().__init__(error.message)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.error!r})"