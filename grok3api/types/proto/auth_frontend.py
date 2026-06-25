from typing import Annotated, List, Optional

from enum import IntEnum
from pydantic import BaseModel, Field

from grok3api.types.pb_meta import ProtoField, WireType
from grok3api.types.proto.shared import *


class CreateAnonUserRequest(BaseModel):
    user_public_key: Annotated[bytes, ProtoField(tag=1, wire=WireType.BYTES_FIELD)] = b""


class CreateSessionRequest(BaseModel):
    credentials: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    session_id: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    prompt_on_duplicate_email: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False
    castle_request_token: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""

