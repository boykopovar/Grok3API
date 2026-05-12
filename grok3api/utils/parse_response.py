from typing import List

from grok3api.types import ResponseChunk, TokenChunk, ModelResponseChunk, FinalMetadataChunk, SurveyChunk, \
    ConversationChunk, TitleChunk
from grok3api.types.pb_meta import WireType, AddResponseTag
from grok3api.types.response import StreamingMetadata, ModelResponse, FinalMetadata
from grok3api.types.response import GenerateTitleResponse, Survey, Conversation
from grok3api.utils.meta_utils import get_meta_type
from grok3api.utils.pb_serializer import decode_message
from grok3api.utils.protobuf import pb_parse


def _parse_add_response(buf: bytes) -> List[ResponseChunk]:
    d = pb_parse(buf)

    response_id = get_meta_type(
        d,
        AddResponseTag.RESPONSE_ID,
        WireType.STRING,
    )

    is_thinking = get_meta_type(
        d,
        AddResponseTag.IS_THINKING,
        WireType.BOOL,
    ) or False

    is_soft_stop = get_meta_type(
        d,
        AddResponseTag.IS_SOFT_STOP,
        WireType.BOOL,
    ) or False

    message_tag = get_meta_type(
        d,
        AddResponseTag.MESSAGE_TAG,
        WireType.STRING,
    ) or ""

    message_step_id = get_meta_type(
        d,
        AddResponseTag.MESSAGE_STEP_ID,
        WireType.INT32,
    )

    side_by_side_index = get_meta_type(
        d,
        AddResponseTag.SIDE_BY_SIDE_INDEX,
        WireType.INT32,
    )

    streaming_metadata = get_meta_type(
        d,
        AddResponseTag.STREAMING_METADATA,
        WireType.MESSAGE,
        StreamingMetadata,
    )

    chunks: List[ResponseChunk] = []

    if TokenChunk._TAG in d:
        chunks.append(
            TokenChunk(
                token=get_meta_type(
                    d,
                    TokenChunk._TAG,
                    WireType.STRING,
                ),
                is_thinking=is_thinking,
                is_soft_stop=is_soft_stop,
                message_tag=message_tag,
                message_step_id=message_step_id,
                response_id=response_id,
                side_by_side_index=side_by_side_index,
                streaming_metadata=streaming_metadata,
            ),
        )

    if ModelResponseChunk._TAG in d:
        chunks.append(
            ModelResponseChunk(
                model_response=decode_message(
                    ModelResponse,
                    d[ModelResponseChunk._TAG][0],
                ),
                response_id=response_id,
                is_soft_stop=is_soft_stop,
            ),
        )

    if FinalMetadataChunk._TAG in d:
        chunks.append(
            FinalMetadataChunk(
                final_metadata=decode_message(
                    FinalMetadata,
                    d[FinalMetadataChunk._TAG][0],
                ),
                response_id=response_id,
            ),
        )

    if SurveyChunk._TAG in d:
        chunks.append(
            SurveyChunk(
                survey=decode_message(
                    Survey,
                    d[SurveyChunk._TAG][0],
                ),
                response_id=response_id,
            ),
        )
    return chunks


def parse_chunk(buf: bytes) -> List[ResponseChunk]:
    """Parse a single gRPC frame body into zero or more ResponseChunk objects."""


    d = pb_parse(buf)
    out: List[ResponseChunk] = []
    if 1 in d:
        out.extend(_parse_add_response(d[1][0]))
    if ConversationChunk._TAG in d:
        out.append(
            ConversationChunk(
                conversation=decode_message(Conversation, d[ConversationChunk._TAG][0])
            )
        )
    if TitleChunk._TAG in d:
        out.append(
            TitleChunk(
                new_title=decode_message(GenerateTitleResponse, d[TitleChunk._TAG][0]).new_title
            )
        )
    return out