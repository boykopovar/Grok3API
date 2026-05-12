from multidict import CIMultiDictProxy


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