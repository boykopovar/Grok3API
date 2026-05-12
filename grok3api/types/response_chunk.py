from __future__ import annotations

from typing import Optional, Union, ClassVar

from pydantic import BaseModel

from grok3api.types.response import StreamingMetadata, ModelResponse, FinalMetadata, Survey, Conversation


class TokenChunk(BaseModel):
    _TAG: ClassVar[int] = 2

    token: str
    is_thinking: bool
    is_soft_stop: bool
    message_tag: str
    message_step_id: Optional[int]
    response_id: Optional[str]
    side_by_side_index: Optional[int]
    streaming_metadata: Optional[StreamingMetadata]

    @property
    def is_final(self) -> bool:
        return self.message_tag == "final"


class ModelResponseChunk(BaseModel):
    _TAG: ClassVar[int] = 3

    model_response: ModelResponse
    response_id: Optional[str]
    is_soft_stop: bool


class FinalMetadataChunk(BaseModel):
    _TAG: ClassVar[int] = 15

    final_metadata: FinalMetadata
    response_id: Optional[str]


class SurveyChunk(BaseModel):
    _TAG: ClassVar[int] = 41

    survey: Survey
    response_id: Optional[str]


class ConversationChunk(BaseModel):
    _TAG: ClassVar[int] = 2

    conversation: Conversation


class TitleChunk(BaseModel):
    _TAG: ClassVar[int] = 3

    new_title: str


ResponseChunk = Union[
    TokenChunk,
    ModelResponseChunk,
    FinalMetadataChunk,
    SurveyChunk,
    ConversationChunk,
    TitleChunk,
]