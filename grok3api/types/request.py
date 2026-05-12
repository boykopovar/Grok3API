from typing import List, Optional

from typing_extensions import Annotated
from pydantic import BaseModel, Field


from grok3api.utils.pb_serializer import encode_message

from grok3api.types.pb_meta import ProtoField, WireType


class DeviceEnvInfo(BaseModel):
    dark_mode_enabled: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    device_pixel_ratio: Annotated[float, ProtoField(tag=2, wire=WireType.DOUBLE)] = 1.100000023841858
    screen_width: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 1280
    screen_height: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 1024
    viewport_width: Annotated[int, ProtoField(tag=5, wire=WireType.INT32)] = 413
    viewport_height: Annotated[int, ProtoField(tag=6, wire=WireType.INT32)] = 785

    def encode(self) -> bytes:
        return encode_message(self)


class GeoLocation(BaseModel):
    latitude: Annotated[float, ProtoField(tag=1, wire=WireType.FLOAT)] = 0.0
    longitude: Annotated[float, ProtoField(tag=2, wire=WireType.FLOAT)] = 0.0
    accuracy: Annotated[float, ProtoField(tag=3, wire=WireType.FLOAT)] = 0.0

    def encode(self) -> bytes:
        return encode_message(self)


class ToolOverrides(BaseModel):
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

    def encode(self) -> bytes:
        return encode_message(self)


class SupportedFastTools(BaseModel):
    calculator_tool: Annotated[Optional[str], ProtoField(tag=1, wire=WireType.STRING)] = None
    unit_conversion_tool: Annotated[Optional[str], ProtoField(tag=2, wire=WireType.STRING)] = None

    def encode(self) -> bytes:
        return encode_message(self)


class ImagineCanvasContext(BaseModel):
    image_url: Annotated[Optional[str], ProtoField(tag=1, wire=WireType.STRING)] = None
    mask_url: Annotated[Optional[str], ProtoField(tag=2, wire=WireType.STRING)] = None

    def encode(self) -> bytes:
        return encode_message(self)


class ChatRequest(BaseModel):
    system_prompt_name: Annotated[Optional[str], ProtoField(tag=2, wire=WireType.STRING)] = None
    temporary: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    model_name: Annotated[Optional[str], ProtoField(tag=4, wire=WireType.STRING)] = None
    message: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)]
    file_attachments: Annotated[List[str], ProtoField(tag=6, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    image_attachments: Annotated[List[str], ProtoField(tag=7, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    disable_search: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False
    enable_image_generation: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = True
    return_image_bytes: Annotated[bool, ProtoField(tag=10, wire=WireType.BOOL)] = False
    return_raw_grok_in_xai_request: Annotated[bool, ProtoField(tag=11, wire=WireType.BOOL)] = False
    enable_image_streaming: Annotated[bool, ProtoField(tag=12, wire=WireType.BOOL)] = True
    image_generation_count: Annotated[Optional[int], ProtoField(tag=13, wire=WireType.INT32)] = 2
    force_concise: Annotated[bool, ProtoField(tag=14, wire=WireType.BOOL)] = False
    tool_overrides: Annotated[Optional[ToolOverrides], ProtoField(tag=15, wire=WireType.MESSAGE, cls=ToolOverrides)] = None
    enable_side_by_side: Annotated[bool, ProtoField(tag=16, wire=WireType.BOOL)] = True
    send_final_metadata: Annotated[bool, ProtoField(tag=18, wire=WireType.BOOL)] = True
    custom_instructions: Annotated[Optional[str], ProtoField(tag=19, wire=WireType.STRING)] = None
    custom_personality: Annotated[Optional[str], ProtoField(tag=20, wire=WireType.STRING)] = None
    deepsearch_preset: Annotated[Optional[str], ProtoField(tag=30, wire=WireType.STRING)] = None
    image_edit_uri: Annotated[Optional[str], ProtoField(tag=31, wire=WireType.STRING)] = None
    is_reasoning: Annotated[bool, ProtoField(tag=32, wire=WireType.BOOL)] = False
    webpage_urls: Annotated[List[str], ProtoField(tag=33, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    image_edit_uris: Annotated[List[str], ProtoField(tag=34, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    workspace_ids: Annotated[List[str], ProtoField(tag=35, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    disable_text_follow_ups: Annotated[bool, ProtoField(tag=36, wire=WireType.BOOL)] = False
    disable_artifact: Annotated[bool, ProtoField(tag=37, wire=WireType.BOOL)] = False
    disable_artifact_diff: Annotated[bool, ProtoField(tag=39, wire=WireType.BOOL)] = False
    do_force_trigger_artifact: Annotated[bool, ProtoField(tag=40, wire=WireType.BOOL)] = False
    is_from_grok_files: Annotated[bool, ProtoField(tag=41, wire=WireType.BOOL)] = False
    selected_file_text_content: Annotated[Optional[str], ProtoField(tag=42, wire=WireType.STRING)] = None
    selected_file_text_content_start_position: Annotated[Optional[int], ProtoField(tag=43, wire=WireType.INT32)] = None
    selected_file_text_content_end_position: Annotated[Optional[int], ProtoField(tag=44, wire=WireType.INT32)] = None
    disable_memory: Annotated[bool, ProtoField(tag=45, wire=WireType.BOOL)] = False
    force_side_by_side: Annotated[bool, ProtoField(tag=46, wire=WireType.BOOL)] = False
    models_user_can_use: Annotated[List[str], ProtoField(tag=49, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    skip_response_cache: Annotated[Optional[bool], ProtoField(tag=50, wire=WireType.OPT_BOOL)] = None
    is_async_chat: Annotated[bool, ProtoField(tag=51, wire=WireType.BOOL)] = False
    enable_nsfw: Annotated[Optional[bool], ProtoField(tag=52, wire=WireType.OPT_BOOL)] = None
    is_kids_mode: Annotated[Optional[bool], ProtoField(tag=53, wire=WireType.OPT_BOOL)] = None
    is_regen_request: Annotated[bool, ProtoField(tag=55, wire=WireType.BOOL)] = False
    companion_id: Annotated[Optional[str], ProtoField(tag=59, wire=WireType.STRING)] = None
    template_id: Annotated[Optional[str], ProtoField(tag=60, wire=WireType.STRING)] = None
    disable_self_harm_short_circuit: Annotated[bool, ProtoField(tag=61, wire=WireType.BOOL)] = False
    collection_ids: Annotated[List[str], ProtoField(tag=62, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    connector_ids: Annotated[List[str], ProtoField(tag=63, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    search_all_connectors: Annotated[Optional[bool], ProtoField(tag=64, wire=WireType.OPT_BOOL)] = None
    device_env_info: Annotated[DeviceEnvInfo, ProtoField(tag=65, wire=WireType.MESSAGE, cls=DeviceEnvInfo)] = Field(default_factory=DeviceEnvInfo)
    model_override_key: Annotated[Optional[str], ProtoField(tag=66, wire=WireType.STRING)] = None
    browser_geo_location: Annotated[Optional[GeoLocation], ProtoField(tag=67, wire=WireType.MESSAGE, cls=GeoLocation)] = None
    disable_personalization: Annotated[Optional[bool], ProtoField(tag=69, wire=WireType.OPT_BOOL)] = None
    imagine_project_id: Annotated[Optional[str], ProtoField(tag=71, wire=WireType.STRING)] = None
    mode_id: Annotated[Optional[str], ProtoField(tag=72, wire=WireType.STRING)] = "fast"
    imagine_canvas_context: Annotated[Optional[ImagineCanvasContext], ProtoField(tag=75, wire=WireType.MESSAGE, cls=ImagineCanvasContext)] = None
    disabled_connector_ids: Annotated[List[str], ProtoField(tag=76, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)

    def encode(self) -> bytes:
        return encode_message(self)