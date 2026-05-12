from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field
from typing_extensions import Annotated


from grok3api.types.pb_meta import ProtoField, WireType
from grok3api.utils.pb_serializer import decode_message

class _GrokResponseModel(BaseModel):
    def __str__(self) -> str:
        return self.model_dump_json(
            indent=2,
            exclude_none=True,
        )

    def __repr__(self) -> str:
        return self.__str__()


class _PbModel(_GrokResponseModel):
    @classmethod
    def from_pb(cls, buf: bytes) -> "_PbModel":
        return decode_message(cls, buf)


class StreamingMetadata(_PbModel):
    stream_key: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    msg_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GenerateTitleResponse(_PbModel):
    new_title: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class FollowUpSuggestionProperties(_PbModel):
    message_type: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    follow_up_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ToolOverridesResponse(_PbModel):
    image_gen: Annotated[Optional[bool], ProtoField(tag=1, wire=WireType.OPT_BOOL)] = None
    trends_search: Annotated[Optional[bool], ProtoField(tag=5, wire=WireType.OPT_BOOL)] = None
    video_gen: Annotated[Optional[bool], ProtoField(tag=7, wire=WireType.OPT_BOOL)] = None
    audio_gen: Annotated[Optional[bool], ProtoField(tag=8, wire=WireType.OPT_BOOL)] = None
    gmail_search: Annotated[Optional[bool], ProtoField(tag=9, wire=WireType.OPT_BOOL)] = None
    google_calendar_search: Annotated[Optional[bool], ProtoField(tag=10, wire=WireType.OPT_BOOL)] = None
    google_drive_search: Annotated[Optional[bool], ProtoField(tag=11, wire=WireType.OPT_BOOL)] = None
    outlook_search: Annotated[Optional[bool], ProtoField(tag=12, wire=WireType.OPT_BOOL)] = None
    outlook_calendar_search: Annotated[Optional[bool], ProtoField(tag=13, wire=WireType.OPT_BOOL)] = None
    document_search: Annotated[Optional[bool], ProtoField(tag=14, wire=WireType.OPT_BOOL)] = None


class FollowUpSuggestion(_PbModel):
    properties: Annotated[
        Optional[FollowUpSuggestionProperties],
        ProtoField(tag=1, wire=WireType.MESSAGE, cls=FollowUpSuggestionProperties),
    ] = None
    label: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    tool_overrides: Annotated[
        Optional[ToolOverridesResponse],
        ProtoField(tag=3, wire=WireType.MESSAGE, cls=ToolOverridesResponse),
    ] = None


class FeedbackLabel(_PbModel):
    id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    label_en: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    icon: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class FinalMetadata(_PbModel):
    follow_up_suggestions: Annotated[
        List[FollowUpSuggestion],
        ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=FollowUpSuggestion),
    ] = Field(default_factory=list)
    feedback_labels: Annotated[
        List[FeedbackLabel],
        ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=FeedbackLabel),
    ] = Field(default_factory=list)
    tools_used: Annotated[
        Optional[ToolOverridesResponse],
        ProtoField(tag=3, wire=WireType.MESSAGE, cls=ToolOverridesResponse),
    ] = None
    disclaimer: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class WebSearchResult(_PbModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    preview: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    search_engine_text: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    site_name: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    metadata_title: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    creator: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    image: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    favicon: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    citation_id: Annotated[str, ProtoField(tag=12, wire=WireType.STRING)] = ""


class WebSearchResults(_PbModel):
    results: Annotated[
        List[WebSearchResult],
        ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=WebSearchResult),
    ] = Field(default_factory=list)


class XPost(_PbModel):
    username: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    text: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    create_time: Annotated[Optional[datetime], ProtoField(tag=4, wire=WireType.TIMESTAMP)] = None
    profile_image_url: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    post_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    citation_id: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    parent_post_id: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    quote_post_id: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    view_count: Annotated[int, ProtoField(tag=13, wire=WireType.INT32)] = 0
    community_note: Annotated[str, ProtoField(tag=14, wire=WireType.STRING)] = ""
    verified_type: Annotated[str, ProtoField(tag=15, wire=WireType.STRING)] = ""
    text_markdown: Annotated[str, ProtoField(tag=18, wire=WireType.STRING)] = ""


class XSearchResults(_PbModel):
    results: Annotated[List[XPost], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=XPost)] = Field(default_factory=list)


class RagResult(_PbModel):
    connector_type: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    query: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    chunk_content: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    document_type: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    document_title: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    document_source_url: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class RagResults(_PbModel):
    results: Annotated[List[RagResult], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=RagResult)] = Field(default_factory=list)


class ConnectorSearchResultItem(_PbModel):
    file_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    connector_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    query: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    document_type: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    document_title: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    document_source_url: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    chunk_content: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    chunk_id: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""


class ConnectorSearchResults(_PbModel):
    results: Annotated[
        List[ConnectorSearchResultItem],
        ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=ConnectorSearchResultItem),
    ] = Field(default_factory=list)


class CollectionSearchResultItem(_PbModel):
    file_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    size_bytes: Annotated[int, ProtoField(tag=3, wire=WireType.INT64)] = 0
    content_type: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    created_at: Annotated[Optional[datetime], ProtoField(tag=5, wire=WireType.TIMESTAMP)] = None
    expires_at: Annotated[Optional[datetime], ProtoField(tag=6, wire=WireType.TIMESTAMP)] = None
    upload_status: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    upload_error_message: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    processing_status: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    file_path: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    url: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    query: Annotated[str, ProtoField(tag=12, wire=WireType.STRING)] = ""
    chunk_content: Annotated[str, ProtoField(tag=13, wire=WireType.STRING)] = ""
    chunk_id: Annotated[str, ProtoField(tag=14, wire=WireType.STRING)] = ""


class CollectionSearchResults(_PbModel):
    results: Annotated[
        List[CollectionSearchResultItem],
        ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=CollectionSearchResultItem),
    ] = Field(default_factory=list)


class MemoryV2UpdateResult(_PbModel):
    old_memory_substring: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    new_memory_substring: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    operation_type: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    expires_at_timestamp: Annotated[Optional[datetime], ProtoField(tag=4, wire=WireType.TIMESTAMP)] = None


class CodeExecutionResult(_PbModel):
    stdout: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    stderr: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    exit_code: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    command_timed_out: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False


class ToolUsageResult(_PbModel):
    tool_usage_card_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    web_search_results: Annotated[
        Optional[WebSearchResults],
        ProtoField(tag=2, wire=WireType.MESSAGE, cls=WebSearchResults),
    ] = None
    x_search_results: Annotated[
        Optional[XSearchResults],
        ProtoField(tag=3, wire=WireType.MESSAGE, cls=XSearchResults),
    ] = None
    rag_results: Annotated[Optional[RagResults], ProtoField(tag=4, wire=WireType.MESSAGE, cls=RagResults)] = None
    connector_search_results: Annotated[
        Optional[ConnectorSearchResults],
        ProtoField(tag=5, wire=WireType.MESSAGE, cls=ConnectorSearchResults),
    ] = None
    collection_search_results: Annotated[
        Optional[CollectionSearchResults],
        ProtoField(tag=6, wire=WireType.MESSAGE, cls=CollectionSearchResults),
    ] = None
    memory_v2_update_result: Annotated[
        Optional[MemoryV2UpdateResult],
        ProtoField(tag=7, wire=WireType.MESSAGE, cls=MemoryV2UpdateResult),
    ] = None
    code_execution_result: Annotated[
        Optional[CodeExecutionResult],
        ProtoField(tag=8, wire=WireType.MESSAGE, cls=CodeExecutionResult),
    ] = None


class ResponseStep(_PbModel):
    text: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    tags: Annotated[List[str], ProtoField(tag=2, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    xpost_ids: Annotated[List[str], ProtoField(tag=4, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    web_search_results: Annotated[
        List[WebSearchResult],
        ProtoField(tag=6, wire=WireType.REPEATED_MESSAGE, cls=WebSearchResult),
    ] = Field(default_factory=list)
    tool_usage_results: Annotated[
        List[ToolUsageResult],
        ProtoField(tag=8, wire=WireType.REPEATED_MESSAGE, cls=ToolUsageResult),
    ] = Field(default_factory=list)
    rag_results: Annotated[List[RagResult], ProtoField(tag=9, wire=WireType.REPEATED_MESSAGE, cls=RagResult)] = Field(default_factory=list)
    connector_search_results: Annotated[
        List[ConnectorSearchResultItem],
        ProtoField(tag=10, wire=WireType.REPEATED_MESSAGE, cls=ConnectorSearchResultItem),
    ] = Field(default_factory=list)
    collection_search_results: Annotated[
        List[CollectionSearchResultItem],
        ProtoField(tag=11, wire=WireType.REPEATED_MESSAGE, cls=CollectionSearchResultItem),
    ] = Field(default_factory=list)


class FileMetadata(_PbModel):
    file_metadata_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    file_mime_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    file_name: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    file_uri: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    parsed_file_uri: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    create_time: Annotated[Optional[datetime], ProtoField(tag=6, wire=WireType.TIMESTAMP)] = None
    file_source: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    third_party_file_id: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    third_party_file_mime_type: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""


class StreamError(_PbModel):
    message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    global_rate_limit: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    model_not_available: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    system_kill_switch: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    beyond_context_length: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False
    user_prompt_too_long: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    attachment_moderated: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False
    attachment_image_too_large: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False
    attachment_file_too_large: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = False
    attachment_too_many_pages: Annotated[bool, ProtoField(tag=10, wire=WireType.BOOL)] = False
    attachment_load_failed: Annotated[bool, ProtoField(tag=11, wire=WireType.BOOL)] = False
    internal_error: Annotated[bool, ProtoField(tag=12, wire=WireType.BOOL)] = False
    request_cancelled: Annotated[bool, ProtoField(tag=13, wire=WireType.BOOL)] = False
    render_tool_failed: Annotated[bool, ProtoField(tag=14, wire=WireType.BOOL)] = False
    render_tool_rate_limited: Annotated[bool, ProtoField(tag=15, wire=WireType.BOOL)] = False
    tool_call_failed: Annotated[bool, ProtoField(tag=16, wire=WireType.BOOL)] = False
    severity: Annotated[str, ProtoField(tag=17, wire=WireType.STRING)] = ""


class RequestMetadata(_PbModel):
    model: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    mode: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class FastToolResponse(_PbModel):
    title: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    subtitle: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    body: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class UiLayout(_PbModel):
    reasoning_ui_layout: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    will_think_long: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    effort: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    steer_model_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    rollout_ids: Annotated[List[str], ProtoField(tag=5, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class StreamingMetadataFull(_PbModel):
    stream_key: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    msg_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class LlmInfo(_PbModel):
    model_hash: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class EffortDecision(_PbModel):
    effort: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    steer_model_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class SideBySideConfig(_PbModel):
    single_thinking_different_summary: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    enable_prefer_button_trigger: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    stream_final_answers_together: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    hide_thinking_trace: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    use_length_control_container: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False


class QueryAction(_PbModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ImageGenerationResponse(_PbModel):
    generated_image_bytes: Annotated[Optional[bytes], ProtoField(tag=1, wire=WireType.BYTES_FIELD)] = None
    content_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class StreamingImageGenerationResponse(_PbModel):
    image_url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    seq: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    progress: Annotated[float, ProtoField(tag=3, wire=WireType.FLOAT)] = 0.0
    moderated: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    image_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    image_index: Annotated[int, ProtoField(tag=6, wire=WireType.INT32)] = 0
    asset_id: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    image_model: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    r_rated: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = False
    side_by_side_index: Annotated[int, ProtoField(tag=10, wire=WireType.INT32)] = 0
    has_watermark: Annotated[bool, ProtoField(tag=11, wire=WireType.BOOL)] = False
    is_root_user_uploaded: Annotated[bool, ProtoField(tag=13, wire=WireType.BOOL)] = False


class StreamingVideoGenerationResponse(_PbModel):
    video_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    progress: Annotated[float, ProtoField(tag=2, wire=WireType.FLOAT)] = 0.0
    asset_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    video_url: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    audio_urls: Annotated[List[str], ProtoField(tag=5, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    video_prompt: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    image_reference: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    audio_transcripts: Annotated[List[str], ProtoField(tag=8, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    moderated: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = False
    mode: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    model_name: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    thumbnail_image_url: Annotated[str, ProtoField(tag=12, wire=WireType.STRING)] = ""
    parent_post_id: Annotated[str, ProtoField(tag=13, wire=WireType.STRING)] = ""
    video_post_id: Annotated[str, ProtoField(tag=14, wire=WireType.STRING)] = ""
    side_by_side_index: Annotated[int, ProtoField(tag=15, wire=WireType.INT32)] = 0
    r_rated: Annotated[bool, ProtoField(tag=16, wire=WireType.BOOL)] = False
    video_streaming_index: Annotated[int, ProtoField(tag=17, wire=WireType.INT32)] = 0
    height: Annotated[int, ProtoField(tag=18, wire=WireType.INT32)] = 0
    width: Annotated[int, ProtoField(tag=19, wire=WireType.INT32)] = 0
    video_streaming_duration: Annotated[int, ProtoField(tag=20, wire=WireType.INT32)] = 0
    resolution_name: Annotated[str, ProtoField(tag=21, wire=WireType.STRING)] = ""
    has_watermark: Annotated[bool, ProtoField(tag=22, wire=WireType.BOOL)] = False
    is_root_user_uploaded: Annotated[bool, ProtoField(tag=24, wire=WireType.BOOL)] = False


class StreamingAudioGenerationResponse(_PbModel):
    video_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    audio_urls: Annotated[List[str], ProtoField(tag=2, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class ImageDimensions(_PbModel):
    width: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    height: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class CardAttachment(_PbModel):
    json_data: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class BannerMessage(_PbModel):
    message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class Disclaimer(_PbModel):
    message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ImageAttachmentInfo(_PbModel):
    image_attachment_count: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0


class ProgressReport(_PbModel):
    category: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    state: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    message: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    percentage: Annotated[float, ProtoField(tag=4, wire=WireType.FLOAT)] = 0.0


class SurveyValue(_PbModel):
    value_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    label: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class Survey(_PbModel):
    survey_title: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    statsig_survey_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class AuthNotification(_PbModel):
    providers: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class FollowUpSuggestions(_PbModel):
    suggestions: Annotated[
        List[FollowUpSuggestion],
        ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=FollowUpSuggestion),
    ] = Field(default_factory=list)


class FollowUpSuggestedMode(_PbModel):
    mode: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ModelResponse(_PbModel):
    response_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    message: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    sender: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    create_time: Annotated[Optional[datetime], ProtoField(tag=4, wire=WireType.TIMESTAMP)] = None
    parent_response_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    manual: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    partial: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False
    shared: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False
    query: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    query_type: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    web_search_results: Annotated[
        List[WebSearchResult],
        ProtoField(tag=11, wire=WireType.REPEATED_MESSAGE, cls=WebSearchResult),
    ] = Field(default_factory=list)
    xpost_ids: Annotated[List[str], ProtoField(tag=12, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    xposts: Annotated[List[XPost], ProtoField(tag=13, wire=WireType.REPEATED_MESSAGE, cls=XPost)] = Field(default_factory=list)
    generated_image_urls: Annotated[List[str], ProtoField(tag=14, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    image_attachments: Annotated[List[str], ProtoField(tag=15, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    file_attachments: Annotated[List[str], ProtoField(tag=16, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    file_uris: Annotated[List[str], ProtoField(tag=19, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    file_attachments_metadata: Annotated[
        List[FileMetadata],
        ProtoField(tag=20, wire=WireType.REPEATED_MESSAGE, cls=FileMetadata),
    ] = Field(default_factory=list)
    is_control: Annotated[bool, ProtoField(tag=21, wire=WireType.BOOL)] = False
    thinking_trace: Annotated[str, ProtoField(tag=22, wire=WireType.STRING)] = ""
    steps: Annotated[List[ResponseStep], ProtoField(tag=23, wire=WireType.REPEATED_MESSAGE, cls=ResponseStep)] = Field(default_factory=list)
    image_edit_uri: Annotated[str, ProtoField(tag=24, wire=WireType.STRING)] = ""
    error: Annotated[str, ProtoField(tag=25, wire=WireType.STRING)] = ""
    media_types: Annotated[List[str], ProtoField(tag=26, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    webpage_urls: Annotated[List[str], ProtoField(tag=27, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    metadata: Annotated[Dict[str, Any], ProtoField(tag=28, wire=WireType.MAP_IGNORED)] = Field(default_factory=dict)
    image_edit_uris: Annotated[List[str], ProtoField(tag=29, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    generated_image_height: Annotated[int, ProtoField(tag=30, wire=WireType.INT32)] = 0
    generated_image_width: Annotated[int, ProtoField(tag=31, wire=WireType.INT32)] = 0
    ui_layout: Annotated[Optional[UiLayout], ProtoField(tag=32, wire=WireType.MESSAGE, cls=UiLayout)] = None
    thinking_start_time: Annotated[Optional[datetime], ProtoField(tag=33, wire=WireType.TIMESTAMP)] = None
    thinking_end_time: Annotated[Optional[datetime], ProtoField(tag=34, wire=WireType.TIMESTAMP)] = None
    cited_web_search_results: Annotated[
        List[WebSearchResult],
        ProtoField(tag=35, wire=WireType.REPEATED_MESSAGE, cls=WebSearchResult),
    ] = Field(default_factory=list)
    selected_file_text_content: Annotated[str, ProtoField(tag=36, wire=WireType.STRING)] = ""
    selected_file_text_content_start: Annotated[int, ProtoField(tag=37, wire=WireType.INT32)] = 0
    selected_file_text_content_end: Annotated[int, ProtoField(tag=38, wire=WireType.INT32)] = 0
    thread_parent_id: Annotated[str, ProtoField(tag=40, wire=WireType.STRING)] = ""
    parent_quoted_text: Annotated[str, ProtoField(tag=41, wire=WireType.STRING)] = ""
    model: Annotated[str, ProtoField(tag=42, wire=WireType.STRING)] = ""
    fast_tool_response: Annotated[Optional[FastToolResponse], ProtoField(tag=44, wire=WireType.MESSAGE, cls=FastToolResponse)] = None
    request_metadata: Annotated[Optional[RequestMetadata], ProtoField(tag=45, wire=WireType.MESSAGE, cls=RequestMetadata)] = None
    rag_results: Annotated[List[RagResult], ProtoField(tag=46, wire=WireType.REPEATED_MESSAGE, cls=RagResult)] = Field(default_factory=list)
    cited_rag_results: Annotated[List[RagResult], ProtoField(tag=47, wire=WireType.REPEATED_MESSAGE, cls=RagResult)] = Field(default_factory=list)
    collection_search_results: Annotated[
        List[CollectionSearchResultItem],
        ProtoField(tag=50, wire=WireType.REPEATED_MESSAGE, cls=CollectionSearchResultItem),
    ] = Field(default_factory=list)
    stream_errors: Annotated[List[StreamError], ProtoField(tag=52, wire=WireType.REPEATED_MESSAGE, cls=StreamError)] = Field(default_factory=list)


class Conversation(_PbModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    create_time: Annotated[Optional[datetime], ProtoField(tag=3, wire=WireType.TIMESTAMP)] = None
    modify_time: Annotated[Optional[datetime], ProtoField(tag=4, wire=WireType.TIMESTAMP)] = None
    starred: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    system_prompt_name: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    temporary: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False
    media_types: Annotated[List[str], ProtoField(tag=10, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    team_id: Annotated[str, ProtoField(tag=13, wire=WireType.STRING)] = ""
    x_user_id: Annotated[str, ProtoField(tag=14, wire=WireType.STRING)] = ""
    template_id: Annotated[str, ProtoField(tag=15, wire=WireType.STRING)] = ""
    voice_chat_asset_url: Annotated[str, ProtoField(tag=16, wire=WireType.STRING)] = ""
    voice_chat_alignment_info: Annotated[str, ProtoField(tag=17, wire=WireType.STRING)] = ""
    voice_chat_session_metadata: Annotated[str, ProtoField(tag=18, wire=WireType.STRING)] = ""


class AskResponse(_GrokResponseModel):
    text: str
    model_response: Optional[ModelResponse] = None
    final_metadata: Optional[FinalMetadata] = None
    conversation: Optional[Conversation] = None
    title: Optional[str] = None
    survey: Optional[Survey] = None
