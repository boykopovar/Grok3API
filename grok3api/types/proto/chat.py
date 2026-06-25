from __future__ import annotations

from typing import Annotated, List, Optional

from enum import IntEnum
from pydantic import BaseModel, Field

from grok3api.types.pb_meta import ProtoField, WireType
from grok3api.types.proto.shared import *


class Channel(IntEnum):
    CHANNEL_UNSPECIFIED = 0
    CHANNEL_ASSISTANT_RESPONSE = 1
    CHANNEL_ASSISTANT_THINKING = 2
    CHANNEL_ASSISTANT_NOTETAKER_HEADER = 3
    CHANNEL_ASSISTANT_NOTETAKER_SUMMARY = 4


class ImageChunkSystemErrors(IntEnum):
    ERR_CODE_UNSPECIFIED = 0
    ERR_CHECK_IMAGE_PROMPT = 1001
    ERR_SUGGEST_MOD_RULES = 1002
    ERR_CHECK_FINAL_IMAGE = 1003
    ERR_CHECK_IMAGE = 1004
    ERR_CHECK_VIDEO = 1005
    ERR_RATE_LIMITED = 1006
    ERR_GENERATION_FAILED = 1007
    ERR_RENDER_PER_MESSAGE_LIMIT_EXCEEDED = 1008


class ToolCallStatus(IntEnum):
    TOOL_CALL_STATUS_IN_PROGRESS = 0
    TOOL_CALL_STATUS_COMPLETED = 1
    TOOL_CALL_STATUS_INCOMPLETE = 2
    TOOL_CALL_STATUS_FAILED = 3


class FileSource(IntEnum):
    FILE_SOURCE_UNSPECIFIED = 0
    FILE_SOURCE_GROK = 1


class Layout(IntEnum):
    LAYOUT_UNSPECIFIED = 0
    LAYOUT_BLOCK = 1
    LAYOUT_INLINE = 2


class Orientation(IntEnum):
    ORIENTATION_UNSPECIFIED = 0
    ORIENTATION_PORTRAIT = 1
    ORIENTATION_LANDSCAPE = 2


class Outcome(IntEnum):
    OUTCOME_UNSPECIFIED = 0
    OUTCOME_APPROVE = 1
    OUTCOME_REJECT = 2
    OUTCOME_ALWAYS_APPROVE = 3
    OUTCOME_ALWAYS_REJECT = 4


class FileType(IntEnum):
    FILE_TYPE_UNSPECIFIED = 0
    FILE_TYPE_FILE = 1
    FILE_TYPE_SKILL = 2


class CitationKind(IntEnum):
    CITATION_KIND_UNSPECIFIED = 0
    CITATION_KIND_WEB_PAGE = 1
    CITATION_KIND_X_POST = 2
    CITATION_KIND_X_USER = 3
    CITATION_KIND_X_THREAD = 4
    CITATION_KIND_CONNECTOR_DOCUMENT = 5
    CITATION_KIND_COLLECTION_DOCUMENT = 6


class Size(IntEnum):
    SIZE_UNSPECIFIED = 0
    SIZE_SMALL = 1
    SIZE_LARGE = 2


class Scope(IntEnum):
    SCOPE_UNSPECIFIED = 0
    SCOPE_READ = 1
    SCOPE_WRITE = 2


class EditContextKind(IntEnum):
    KIND_UNSPECIFIED = 0
    KIND_SEARCH_REPLACE = 1
    KIND_WRITE_NEW = 2
    KIND_WRITE_OVERWRITE = 3
    KIND_APPLY_PATCH = 4
    KIND_DELETE = 5


class FileMentionFileSource(IntEnum):
    FILE_SOURCE_UNSPECIFIED = 0
    FILE_SOURCE_GROK = 1


class GeneratedImageStartLayout(IntEnum):
    LAYOUT_UNSPECIFIED = 0
    LAYOUT_BLOCK = 1
    LAYOUT_INLINE = 2


class GeneratedImageStartOrientation(IntEnum):
    ORIENTATION_UNSPECIFIED = 0
    ORIENTATION_PORTRAIT = 1
    ORIENTATION_LANDSCAPE = 2


class PermissionAnswerOutcome(IntEnum):
    OUTCOME_UNSPECIFIED = 0
    OUTCOME_APPROVE = 1
    OUTCOME_REJECT = 2
    OUTCOME_ALWAYS_APPROVE = 3
    OUTCOME_ALWAYS_REJECT = 4


class ReadFileToolFileType(IntEnum):
    FILE_TYPE_UNSPECIFIED = 0
    FILE_TYPE_FILE = 1
    FILE_TYPE_SKILL = 2


class RenderCitationCitationKind(IntEnum):
    CITATION_KIND_UNSPECIFIED = 0
    CITATION_KIND_WEB_PAGE = 1
    CITATION_KIND_X_POST = 2
    CITATION_KIND_X_USER = 3
    CITATION_KIND_X_THREAD = 4
    CITATION_KIND_CONNECTOR_DOCUMENT = 5
    CITATION_KIND_COLLECTION_DOCUMENT = 6


class RenderSearchedImageSize(IntEnum):
    SIZE_UNSPECIFIED = 0
    SIZE_SMALL = 1
    SIZE_LARGE = 2


class UserQuestionMode(IntEnum):
    MODE_UNSPECIFIED = 0
    MODE_DEFAULT = 1
    MODE_PLAN = 2


class AddMemoryToolArgs(BaseModel):
    memory: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class Args(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class AddMemoryTool(BaseModel):
    args: Annotated[Optional[AddMemoryToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=AddMemoryToolArgs)] = None


class AnswerAnnotation(BaseModel):
    preview: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    notes: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class AnswerValues(BaseModel):
    values: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class ArticleInnerResult(BaseModel):
    rest_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    plain_text: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class ArticleResults(BaseModel):
    result: Annotated[Optional[ArticleInnerResult], ProtoField(tag=1, wire=WireType.MESSAGE, cls=ArticleInnerResult)] = None


class Article(BaseModel):
    article_results: Annotated[Optional[ArticleResults], ProtoField(tag=1, wire=WireType.MESSAGE, cls=ArticleResults)] = None


class Avatar(BaseModel):
    image_url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class BashContext(BaseModel):
    full_command: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class BashPartialResult(BaseModel):
    output: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class BashToolArgs(BaseModel):
    command: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    timeout: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class BashTool(BaseModel):
    args: Annotated[Optional[BashToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=BashToolArgs)] = None


class PollValue(BaseModel):
    string_value: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    boolean_value: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    type_f: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class BindingValues(BaseModel):
    key: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    value__f: Annotated[Optional[PollValue], ProtoField(tag=2, wire=WireType.MESSAGE, cls=PollValue)] = None


class BindingValuesList(BaseModel):
    binding_values: Annotated[List[BindingValues], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=BindingValues)] = Field(default_factory=list)


class BirdWatchPivotSubtitle(BaseModel):
    text: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class BirdWatchPivot(BaseModel):
    subtitle: Annotated[Optional[BirdWatchPivotSubtitle], ProtoField(tag=1, wire=WireType.MESSAGE, cls=BirdWatchPivotSubtitle)] = None


class BrowsePageToolArgs(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    instructions: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class BrowsePageTool(BaseModel):
    args: Annotated[Optional[BrowsePageToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=BrowsePageToolArgs)] = None


class BrowserNetworkDetailsToolArgs(BaseModel):
    tab_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    request_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class BrowserNetworkDetailsTool(BaseModel):
    args: Annotated[Optional[BrowserNetworkDetailsToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=BrowserNetworkDetailsToolArgs)] = None


class BrowserTabToolArgs(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    tab_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    js_code: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class BrowserTabTool(BaseModel):
    args: Annotated[Optional[BrowserTabToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=BrowserTabToolArgs)] = None


class CallFinanceApiTool(BaseModel):
    pass


class CallPlacesApiTool(BaseModel):
    pass


class CallSportsApiTool(BaseModel):
    pass


class CallWeatherApiTool(BaseModel):
    pass


class Card(BaseModel):
    rest_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    legacy: Annotated[Optional[BindingValuesList], ProtoField(tag=2, wire=WireType.MESSAGE, cls=BindingValuesList)] = None


class ChatroomSendToolArgs(BaseModel):
    message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    to: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ChatroomSendTool(BaseModel):
    args: Annotated[Optional[ChatroomSendToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=ChatroomSendToolArgs)] = None


class CodeExecutionToolArgs(BaseModel):
    code: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    language: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class CodeExecutionTool(BaseModel):
    args: Annotated[Optional[CodeExecutionToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=CodeExecutionToolArgs)] = None


class CollectionsSearchToolArgs(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class CollectionsSearchTool(BaseModel):
    args: Annotated[Optional[CollectionsSearchToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=CollectionsSearchToolArgs)] = None


class ConversationSearchTool(BaseModel):
    pass


class DeleteMemoryToolArgs(BaseModel):
    memory: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class DeleteMemoryTool(BaseModel):
    args: Annotated[Optional[DeleteMemoryToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=DeleteMemoryToolArgs)] = None


class DocumentSearchResult(BaseModel):
    connector_results: Annotated[List[ConnectorSearchResultItem], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=ConnectorSearchResultItem)] = Field(default_factory=list)
    collection_results: Annotated[List[CollectionSearchResultItem], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=CollectionSearchResultItem)] = Field(default_factory=list)


class DocumentSearchToolArgs(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class DocumentSearchTool(BaseModel):
    args: Annotated[Optional[DocumentSearchToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=DocumentSearchToolArgs)] = None


class EditContext(BaseModel):
    file_paths: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    kind: Annotated[EditContextKind, ProtoField(tag=2, wire=WireType.INT32)] = EditContextKind.KIND_UNSPECIFIED


class EditFileToolArgs(BaseModel):
    file_path: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    old_string: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    new_string: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    replace_all: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False


class EditFileTool(BaseModel):
    args: Annotated[Optional[EditFileToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=EditFileToolArgs)] = None


class EditImageToolArgs(BaseModel):
    prompt: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    image_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    file_path: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class EditImageTool(BaseModel):
    args: Annotated[Optional[EditImageToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=EditImageToolArgs)] = None


class EditMemoryToolArgs(BaseModel):
    memory: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class EditMemoryTool(BaseModel):
    args: Annotated[Optional[EditMemoryToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=EditMemoryToolArgs)] = None


class EditSpreadsheetTool(BaseModel):
    pass


class FileMention(BaseModel):
    file_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    file_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    label: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    source: Annotated[FileMentionFileSource, ProtoField(tag=4, wire=WireType.INT32)] = FileMentionFileSource.FILE_SOURCE_UNSPECIFIED
    source_url: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class FilePreviewStart(BaseModel):
    file_name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    mime_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class FunctionCall(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    arguments: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GenerateImageToolArgs(BaseModel):
    prompt: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    orientation: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GenerateImageTool(BaseModel):
    args: Annotated[Optional[GenerateImageToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=GenerateImageToolArgs)] = None


class GeneratedImageStart(BaseModel):
    prompt: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    orientation: Annotated[GeneratedImageStartOrientation, ProtoField(tag=2, wire=WireType.INT32)] = GeneratedImageStartOrientation.ORIENTATION_UNSPECIFIED
    layout: Annotated[GeneratedImageStartLayout, ProtoField(tag=3, wire=WireType.INT32)] = GeneratedImageStartLayout.LAYOUT_UNSPECIFIED


class GeneratedVideoStart(BaseModel):
    prompt: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    aspect_ratio: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GmailSearchTool(BaseModel):
    pass


class GoogleCalendarSearchTool(BaseModel):
    pass


class GoogleDriveReadFileTool(BaseModel):
    pass


class GoogleDriveSearchTool(BaseModel):
    pass


class ImagePrompt(BaseModel):
    modelName: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    prompt: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    upsampledPrompt: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class ImageChunk(BaseModel):
    imageUuid: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    imageUrl: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    seq: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    progress: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    moderated: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False
    imagePrompt: Annotated[Optional[ImagePrompt], ProtoField(tag=6, wire=WireType.MESSAGE, cls=ImagePrompt)] = None
    mediaId: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    imageScore: Annotated[int, ProtoField(tag=8, wire=WireType.INT32)] = 0
    imageTitle: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    imageIndex: Annotated[int, ProtoField(tag=10, wire=WireType.INT32)] = 0
    imageModel: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    imageReference: Annotated[str, ProtoField(tag=12, wire=WireType.STRING)] = ""
    rRated: Annotated[bool, ProtoField(tag=13, wire=WireType.BOOL)] = False
    sideBySideIndex: Annotated[int, ProtoField(tag=14, wire=WireType.INT32)] = 0
    resolution: Annotated[Optional[Resolution], ProtoField(tag=15, wire=WireType.MESSAGE, cls=Resolution)] = None
    isRootRRated: Annotated[bool, ProtoField(tag=16, wire=WireType.BOOL)] = False
    isRootUserUploaded: Annotated[bool, ProtoField(tag=17, wire=WireType.BOOL)] = False
    isRootCelebrity: Annotated[bool, ProtoField(tag=18, wire=WireType.BOOL)] = False
    isRootChild: Annotated[bool, ProtoField(tag=19, wire=WireType.BOOL)] = False
    imageReferences: Annotated[List[str], ProtoField(tag=20, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    hasWatermark: Annotated[bool, ProtoField(tag=21, wire=WireType.BOOL)] = False
    applied_moderation_rule: Annotated[str, ProtoField(tag=22, wire=WireType.STRING)] = ""
    systemErrCode: Annotated[ImageChunkSystemErrors, ProtoField(tag=23, wire=WireType.INT32)] = ImageChunkSystemErrors.ERR_CODE_UNSPECIFIED
    isShadow: Annotated[bool, ProtoField(tag=24, wire=WireType.BOOL)] = False
    rejection_reason: Annotated[MediaRejectionReason, ProtoField(tag=25, wire=WireType.INT32)] = MediaRejectionReason.MEDIA_REJECTION_REASON_UNSPECIFIED


class ImageResult(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    thumbnail: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    source: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    link: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    original: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    original_width: Annotated[int, ProtoField(tag=7, wire=WireType.INT64)] = 0
    original_height: Annotated[int, ProtoField(tag=8, wire=WireType.INT64)] = 0
    description: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    disallow_editing: Annotated[bool, ProtoField(tag=10, wire=WireType.BOOL)] = False
    source_x_post_id: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    file_path: Annotated[str, ProtoField(tag=12, wire=WireType.STRING)] = ""


class ImageSearchToolArgs(BaseModel):
    image_description: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ImageSearchTool(BaseModel):
    args: Annotated[Optional[ImageSearchToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=ImageSearchToolArgs)] = None


class NoteTweetText(BaseModel):
    text: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class InnerNoteTweet(BaseModel):
    result: Annotated[Optional[NoteTweetText], ProtoField(tag=1, wire=WireType.MESSAGE, cls=NoteTweetText)] = None


class InputChunkMetadata(BaseModel):
    pass


class UserText(BaseModel):
    text: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class SkillMention(BaseModel):
    skill_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    skill_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    label: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class Mention(BaseModel):
    file_mention: Annotated[Optional[FileMention], ProtoField(tag=1, wire=WireType.MESSAGE, cls=FileMention)] = None
    skill_mention: Annotated[Optional[SkillMention], ProtoField(tag=2, wire=WireType.MESSAGE, cls=SkillMention)] = None


class PermissionAnswer(BaseModel):
    outcome: Annotated[PermissionAnswerOutcome, ProtoField(tag=1, wire=WireType.INT32)] = PermissionAnswerOutcome.OUTCOME_UNSPECIFIED
    followup_message: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    tool_scope: Annotated[bool, ProtoField(tag=3, wire=WireType.EMPTY_MESSAGE)] = False
    bash_command: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    server_prefix: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    domain: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class QuestionAnswers(BaseModel):
    answers: Annotated[Optional[AnswerValues], ProtoField(tag=1, wire=WireType.MESSAGE, cls=AnswerValues)] = None
    annotations: Annotated[Optional[AnswerAnnotation], ProtoField(tag=2, wire=WireType.MESSAGE, cls=AnswerAnnotation)] = None


class QuestionAnswer(BaseModel):
    accepted: Annotated[Optional[QuestionAnswers], ProtoField(tag=1, wire=WireType.MESSAGE, cls=QuestionAnswers)] = None
    chat_about_this: Annotated[Optional[QuestionAnswers], ProtoField(tag=2, wire=WireType.MESSAGE, cls=QuestionAnswers)] = None
    skip_interview: Annotated[Optional[QuestionAnswers], ProtoField(tag=3, wire=WireType.MESSAGE, cls=QuestionAnswers)] = None
    cancelled: Annotated[bool, ProtoField(tag=4, wire=WireType.EMPTY_MESSAGE)] = False


class UserInputResponse(BaseModel):
    tool_call_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    permission_answer: Annotated[Optional[PermissionAnswer], ProtoField(tag=2, wire=WireType.MESSAGE, cls=PermissionAnswer)] = None
    question_answer: Annotated[Optional[QuestionAnswer], ProtoField(tag=3, wire=WireType.MESSAGE, cls=QuestionAnswer)] = None


class InputChunk(BaseModel):
    metadata: Annotated[Optional[InputChunkMetadata], ProtoField(tag=1, wire=WireType.MESSAGE, cls=InputChunkMetadata)] = None
    text: Annotated[Optional[UserText], ProtoField(tag=2, wire=WireType.MESSAGE, cls=UserText)] = None
    mention: Annotated[Optional[Mention], ProtoField(tag=3, wire=WireType.MESSAGE, cls=Mention)] = None
    user_input_response: Annotated[Optional[UserInputResponse], ProtoField(tag=4, wire=WireType.MESSAGE, cls=UserInputResponse)] = None


class LegacyPostInfo(BaseModel):
    reply_count: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    retweet_count: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    quote_count: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    bookmark_count: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    quoted_status_id_str: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    display_text_range: Annotated[List[int], ProtoField(tag=6, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    conversation_id: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""


class McpTool(BaseModel):
    tool_name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    tool_args_json: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    connector_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    connector_name: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    connector_catalog_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    read_only_hint: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    destructive_hint: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False
    idempotent_hint: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False
    open_world_hint: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = False
    meta: Annotated[dict, ProtoField(tag=10, wire=WireType.JSON_STRUCT)] = Field(default_factory=dict)
    tool_result_json: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    connector_icon_url: Annotated[str, ProtoField(tag=12, wire=WireType.STRING)] = ""


class Variant(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    bitrate: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class VideoInfo(BaseModel):
    aspect_ratio: Annotated[List[int], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    variants: Annotated[List[Variant], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=Variant)] = Field(default_factory=list)
    duration_millis: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0


class MediaEntity(BaseModel):
    type_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    media_url_https: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    video_info: Annotated[Optional[VideoInfo], ProtoField(tag=3, wire=WireType.MESSAGE, cls=VideoInfo)] = None


class NoteTweet(BaseModel):
    note_tweet_results: Annotated[Optional[InnerNoteTweet], ProtoField(tag=1, wire=WireType.MESSAGE, cls=InnerNoteTweet)] = None


class OpenPageToolArgs(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    start_line: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    pattern: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class OpenPageTool(BaseModel):
    args: Annotated[Optional[OpenPageToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=OpenPageToolArgs)] = None


class OutputChunkMetadata(BaseModel):
    rollout_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    step_id: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class Text(BaseModel):
    text: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    channel: Annotated[Channel, ProtoField(tag=2, wire=WireType.INT32)] = Channel.CHANNEL_UNSPECIFIED


class ToolPermission(BaseModel):
    scope: Annotated[ToolPermissionScope, ProtoField(tag=1, wire=WireType.INT32)] = ToolPermissionScope.TOOL_PERMISSION_SCOPE_UNSPECIFIED
    bash_context: Annotated[Optional[BashContext], ProtoField(tag=2, wire=WireType.MESSAGE, cls=BashContext)] = None
    edit_context: Annotated[Optional[EditContext], ProtoField(tag=3, wire=WireType.MESSAGE, cls=EditContext)] = None


class QuestionOption(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    label: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    preview: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class Question(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    text: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    options: Annotated[List[QuestionOption], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=QuestionOption)] = Field(default_factory=list)
    multi_select: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False


class UserQuestion(BaseModel):
    questions: Annotated[List[Question], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=Question)] = Field(default_factory=list)
    mode: Annotated[UserQuestionMode, ProtoField(tag=2, wire=WireType.INT32)] = UserQuestionMode.MODE_UNSPECIFIED


class UserInputRequest(BaseModel):
    tool_call_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    tool_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    tool_permission: Annotated[Optional[ToolPermission], ProtoField(tag=4, wire=WireType.MESSAGE, cls=ToolPermission)] = None
    user_question: Annotated[Optional[UserQuestion], ProtoField(tag=5, wire=WireType.MESSAGE, cls=UserQuestion)] = None


class UILayout(BaseModel):
    reasoning_ui_layout: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    will_think_long: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    effort: Annotated[Effort, ProtoField(tag=3, wire=WireType.INT32)] = Effort.UNSPECIFIED
    steer_model_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    rollout_ids: Annotated[List[str], ProtoField(tag=5, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class WebSearchToolArgs(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class WebSearchTool(BaseModel):
    args: Annotated[Optional[WebSearchToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=WebSearchToolArgs)] = None


class XSearchToolArgs(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class XSearchTool(BaseModel):
    args: Annotated[Optional[XSearchToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=XSearchToolArgs)] = None


class XThreadFetchToolArgs(BaseModel):
    post_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class XThreadFetchTool(BaseModel):
    args: Annotated[Optional[XThreadFetchToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=XThreadFetchToolArgs)] = None


class ViewImageTool(BaseModel):
    pass


class ViewXVideoTool(BaseModel):
    pass


class RenderGeneratedImageTool(BaseModel):
    pass


class RenderEditedImageTool(BaseModel):
    pass


class RenderSearchedImageTool(BaseModel):
    pass


class RenderFileTool(BaseModel):
    pass


class RenderInlineCitationTool(BaseModel):
    pass


class PdfSearchTool(BaseModel):
    pass


class PdfBrowseTool(BaseModel):
    pass


class WaitTool(BaseModel):
    pass


class XUserSearchToolArgs(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class XUserSearchTool(BaseModel):
    args: Annotated[Optional[XUserSearchToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=XUserSearchToolArgs)] = None


class RenderEditedImagesTool(BaseModel):
    pass


class ReadFileToolArgs(BaseModel):
    file_path: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    offset: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    limit: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    file_type: Annotated[ReadFileToolFileType, ProtoField(tag=4, wire=WireType.INT32)] = ReadFileToolFileType.FILE_TYPE_UNSPECIFIED
    display_name: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class ReadFileTool(BaseModel):
    args: Annotated[Optional[ReadFileToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=ReadFileToolArgs)] = None


class WriteFileToolArgs(BaseModel):
    file_path: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    content: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class WriteFileTool(BaseModel):
    args: Annotated[Optional[WriteFileToolArgs], ProtoField(tag=1, wire=WireType.MESSAGE, cls=WriteFileToolArgs)] = None


class ToolUsageCard(BaseModel):
    tool_usage_card_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    web_search: Annotated[Optional[WebSearchTool], ProtoField(tag=2, wire=WireType.MESSAGE, cls=WebSearchTool)] = None
    x_search: Annotated[Optional[XSearchTool], ProtoField(tag=3, wire=WireType.MESSAGE, cls=XSearchTool)] = None
    document_search: Annotated[Optional[DocumentSearchTool], ProtoField(tag=4, wire=WireType.MESSAGE, cls=DocumentSearchTool)] = None
    collections_search: Annotated[Optional[CollectionsSearchTool], ProtoField(tag=5, wire=WireType.MESSAGE, cls=CollectionsSearchTool)] = None
    image_search: Annotated[Optional[ImageSearchTool], ProtoField(tag=6, wire=WireType.MESSAGE, cls=ImageSearchTool)] = None
    browse_page: Annotated[Optional[BrowsePageTool], ProtoField(tag=7, wire=WireType.MESSAGE, cls=BrowsePageTool)] = None
    x_thread_fetch: Annotated[Optional[XThreadFetchTool], ProtoField(tag=8, wire=WireType.MESSAGE, cls=XThreadFetchTool)] = None
    code_execution: Annotated[Optional[CodeExecutionTool], ProtoField(tag=9, wire=WireType.MESSAGE, cls=CodeExecutionTool)] = None
    view_image: Annotated[Optional[ViewImageTool], ProtoField(tag=10, wire=WireType.MESSAGE, cls=ViewImageTool)] = None
    view_x_video: Annotated[Optional[ViewXVideoTool], ProtoField(tag=11, wire=WireType.MESSAGE, cls=ViewXVideoTool)] = None
    render_generated_image: Annotated[Optional[RenderGeneratedImageTool], ProtoField(tag=12, wire=WireType.MESSAGE, cls=RenderGeneratedImageTool)] = None
    render_edited_image: Annotated[Optional[RenderEditedImageTool], ProtoField(tag=13, wire=WireType.MESSAGE, cls=RenderEditedImageTool)] = None
    render_searched_image: Annotated[Optional[RenderSearchedImageTool], ProtoField(tag=14, wire=WireType.MESSAGE, cls=RenderSearchedImageTool)] = None
    render_file: Annotated[Optional[RenderFileTool], ProtoField(tag=15, wire=WireType.MESSAGE, cls=RenderFileTool)] = None
    render_inline_citation: Annotated[Optional[RenderInlineCitationTool], ProtoField(tag=16, wire=WireType.MESSAGE, cls=RenderInlineCitationTool)] = None
    pdf_search: Annotated[Optional[PdfSearchTool], ProtoField(tag=17, wire=WireType.MESSAGE, cls=PdfSearchTool)] = None
    pdf_browse: Annotated[Optional[PdfBrowseTool], ProtoField(tag=18, wire=WireType.MESSAGE, cls=PdfBrowseTool)] = None
    add_memory: Annotated[Optional[AddMemoryTool], ProtoField(tag=19, wire=WireType.MESSAGE, cls=AddMemoryTool)] = None
    edit_memory: Annotated[Optional[EditMemoryTool], ProtoField(tag=20, wire=WireType.MESSAGE, cls=EditMemoryTool)] = None
    delete_memory: Annotated[Optional[DeleteMemoryTool], ProtoField(tag=21, wire=WireType.MESSAGE, cls=DeleteMemoryTool)] = None
    conversation_search: Annotated[Optional[ConversationSearchTool], ProtoField(tag=22, wire=WireType.MESSAGE, cls=ConversationSearchTool)] = None
    chatroom_send: Annotated[Optional[ChatroomSendTool], ProtoField(tag=23, wire=WireType.MESSAGE, cls=ChatroomSendTool)] = None
    wait: Annotated[Optional[WaitTool], ProtoField(tag=24, wire=WireType.MESSAGE, cls=WaitTool)] = None
    gmail_search: Annotated[Optional[GmailSearchTool], ProtoField(tag=25, wire=WireType.MESSAGE, cls=GmailSearchTool)] = None
    google_calendar_search: Annotated[Optional[GoogleCalendarSearchTool], ProtoField(tag=26, wire=WireType.MESSAGE, cls=GoogleCalendarSearchTool)] = None
    call_finance_api: Annotated[Optional[CallFinanceApiTool], ProtoField(tag=27, wire=WireType.MESSAGE, cls=CallFinanceApiTool)] = None
    call_sports_api: Annotated[Optional[CallSportsApiTool], ProtoField(tag=28, wire=WireType.MESSAGE, cls=CallSportsApiTool)] = None
    call_weather_api: Annotated[Optional[CallWeatherApiTool], ProtoField(tag=29, wire=WireType.MESSAGE, cls=CallWeatherApiTool)] = None
    call_places_api: Annotated[Optional[CallPlacesApiTool], ProtoField(tag=30, wire=WireType.MESSAGE, cls=CallPlacesApiTool)] = None
    edit_spreadsheet: Annotated[Optional[EditSpreadsheetTool], ProtoField(tag=31, wire=WireType.MESSAGE, cls=EditSpreadsheetTool)] = None
    mcp: Annotated[Optional[McpTool], ProtoField(tag=32, wire=WireType.MESSAGE, cls=McpTool)] = None
    x_user_search: Annotated[Optional[XUserSearchTool], ProtoField(tag=33, wire=WireType.MESSAGE, cls=XUserSearchTool)] = None
    render_edited_images: Annotated[Optional[RenderEditedImagesTool], ProtoField(tag=34, wire=WireType.MESSAGE, cls=RenderEditedImagesTool)] = None
    intent: Annotated[str, ProtoField(tag=35, wire=WireType.STRING)] = ""
    bash: Annotated[Optional[BashTool], ProtoField(tag=36, wire=WireType.MESSAGE, cls=BashTool)] = None
    read_file: Annotated[Optional[ReadFileTool], ProtoField(tag=37, wire=WireType.MESSAGE, cls=ReadFileTool)] = None
    write_file: Annotated[Optional[WriteFileTool], ProtoField(tag=38, wire=WireType.MESSAGE, cls=WriteFileTool)] = None
    edit_file: Annotated[Optional[EditFileTool], ProtoField(tag=39, wire=WireType.MESSAGE, cls=EditFileTool)] = None
    browser_tab: Annotated[Optional[BrowserTabTool], ProtoField(tag=40, wire=WireType.MESSAGE, cls=BrowserTabTool)] = None
    browser_network_details: Annotated[Optional[BrowserNetworkDetailsTool], ProtoField(tag=41, wire=WireType.MESSAGE, cls=BrowserNetworkDetailsTool)] = None
    google_drive_search: Annotated[Optional[GoogleDriveSearchTool], ProtoField(tag=42, wire=WireType.MESSAGE, cls=GoogleDriveSearchTool)] = None
    google_drive_read_file: Annotated[Optional[GoogleDriveReadFileTool], ProtoField(tag=43, wire=WireType.MESSAGE, cls=GoogleDriveReadFileTool)] = None
    generate_image: Annotated[Optional[GenerateImageTool], ProtoField(tag=44, wire=WireType.MESSAGE, cls=GenerateImageTool)] = None
    edit_image: Annotated[Optional[EditImageTool], ProtoField(tag=45, wire=WireType.MESSAGE, cls=EditImageTool)] = None
    open_page: Annotated[Optional[OpenPageTool], ProtoField(tag=46, wire=WireType.MESSAGE, cls=OpenPageTool)] = None


class XPostResult(BaseModel):
    posts: Annotated[List[XPost], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=XPost)] = Field(default_factory=list)


class UserLegacyInfo(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    screen_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ProfileBio(BaseModel):
    description: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class UserData(BaseModel):
    core: Annotated[Optional[UserLegacyInfo], ProtoField(tag=1, wire=WireType.MESSAGE, cls=UserLegacyInfo)] = None
    avatar: Annotated[Optional[Avatar], ProtoField(tag=2, wire=WireType.MESSAGE, cls=Avatar)] = None
    profile_bio: Annotated[Optional[ProfileBio], ProtoField(tag=3, wire=WireType.MESSAGE, cls=ProfileBio)] = None
    tweep_cred: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0


class UserInnerResult(BaseModel):
    result: Annotated[Optional[UserData], ProtoField(tag=1, wire=WireType.MESSAGE, cls=UserData)] = None


class UserResult(BaseModel):
    user_result: Annotated[Optional[UserInnerResult], ProtoField(tag=1, wire=WireType.MESSAGE, cls=UserInnerResult)] = None


class PostInfo(BaseModel):
    created_at: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    full_text: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ViewCount(BaseModel):
    count: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0


class QuotedTweetResults(BaseModel):
    rest_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    result: Annotated[Optional[PostInnerResult], ProtoField(tag=2, wire=WireType.MESSAGE, cls=PostInnerResult)] = None


class ReplyToResults(BaseModel):
    rest_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    result: Annotated[Optional[PostInnerResult], ProtoField(tag=2, wire=WireType.MESSAGE, cls=PostInnerResult)] = None


class XPostUrls(BaseModel):
    shortened_url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    unwound_url: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class PostInnerResult(BaseModel):
    rest_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    author_info: Annotated[Optional[UserResult], ProtoField(tag=2, wire=WireType.MESSAGE, cls=UserResult)] = None
    data__f: Annotated[Optional[PostInfo], ProtoField(tag=3, wire=WireType.MESSAGE, cls=PostInfo)] = None
    extended_data: Annotated[Optional[LegacyPostInfo], ProtoField(tag=4, wire=WireType.MESSAGE, cls=LegacyPostInfo)] = None
    favorite_count: Annotated[int, ProtoField(tag=5, wire=WireType.INT32)] = 0
    views: Annotated[Optional[ViewCount], ProtoField(tag=6, wire=WireType.MESSAGE, cls=ViewCount)] = None
    media: Annotated[List[MediaEntity], ProtoField(tag=7, wire=WireType.REPEATED_MESSAGE, cls=MediaEntity)] = Field(default_factory=list)
    article: Annotated[Optional[Article], ProtoField(tag=8, wire=WireType.MESSAGE, cls=Article)] = None
    card: Annotated[Optional[Card], ProtoField(tag=9, wire=WireType.MESSAGE, cls=Card)] = None
    media_entities2: Annotated[List[MediaEntity], ProtoField(tag=10, wire=WireType.REPEATED_MESSAGE, cls=MediaEntity)] = Field(default_factory=list)
    birdwatch_pivot: Annotated[Optional[BirdWatchPivot], ProtoField(tag=11, wire=WireType.MESSAGE, cls=BirdWatchPivot)] = None
    quoted_tweet_results: Annotated[Optional[QuotedTweetResults], ProtoField(tag=12, wire=WireType.MESSAGE, cls=QuotedTweetResults)] = None
    legacy: Annotated[Optional[LegacyPostInfo], ProtoField(tag=13, wire=WireType.MESSAGE, cls=LegacyPostInfo)] = None
    reply_to_results: Annotated[Optional[ReplyToResults], ProtoField(tag=14, wire=WireType.MESSAGE, cls=ReplyToResults)] = None
    note_tweet: Annotated[Optional[NoteTweet], ProtoField(tag=15, wire=WireType.MESSAGE, cls=NoteTweet)] = None
    is_target_post: Annotated[bool, ProtoField(tag=16, wire=WireType.BOOL)] = False
    urls: Annotated[List[XPostUrls], ProtoField(tag=17, wire=WireType.REPEATED_MESSAGE, cls=XPostUrls)] = Field(default_factory=list)
    created_at: Annotated[str, ProtoField(tag=18, wire=WireType.STRING)] = ""


class XThread(BaseModel):
    root: Annotated[Optional[XPost], ProtoField(tag=1, wire=WireType.MESSAGE, cls=XPost)] = None
    target_post_inner_result: Annotated[Optional[PostInnerResult], ProtoField(tag=2, wire=WireType.MESSAGE, cls=PostInnerResult)] = None
    children: Annotated[List[XThread], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=XThread)] = Field(default_factory=list)


class XThreadResult(BaseModel):
    thread: Annotated[Optional[XThread], ProtoField(tag=1, wire=WireType.MESSAGE, cls=XThread)] = None


class ToolResult(BaseModel):
    tool_call_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    web_search: Annotated[Optional[WebSearchResult], ProtoField(tag=2, wire=WireType.MESSAGE, cls=WebSearchResult)] = None
    x_post: Annotated[Optional[XPostResult], ProtoField(tag=3, wire=WireType.MESSAGE, cls=XPostResult)] = None
    code_execution: Annotated[Optional[CodeExecutionResult], ProtoField(tag=4, wire=WireType.MESSAGE, cls=CodeExecutionResult)] = None
    x_thread: Annotated[Optional[XThreadResult], ProtoField(tag=5, wire=WireType.MESSAGE, cls=XThreadResult)] = None
    document_search: Annotated[Optional[DocumentSearchResult], ProtoField(tag=6, wire=WireType.MESSAGE, cls=DocumentSearchResult)] = None


class WriteFilePartialResult(BaseModel):
    content: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ToolPartialResult(BaseModel):
    tool_call_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    bash: Annotated[Optional[BashPartialResult], ProtoField(tag=2, wire=WireType.MESSAGE, cls=BashPartialResult)] = None
    write_file: Annotated[Optional[WriteFilePartialResult], ProtoField(tag=3, wire=WireType.MESSAGE, cls=WriteFilePartialResult)] = None


class ToolCall(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    status: Annotated[ToolCallStatus, ProtoField(tag=2, wire=WireType.INT32)] = ToolCallStatus.TOOL_CALL_STATUS_IN_PROGRESS
    error_message: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    function: Annotated[Optional[FunctionCall], ProtoField(tag=10, wire=WireType.MESSAGE, cls=FunctionCall)] = None


class RenderStart(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    generated_image: Annotated[Optional[GeneratedImageStart], ProtoField(tag=2, wire=WireType.MESSAGE, cls=GeneratedImageStart)] = None
    generated_video: Annotated[Optional[GeneratedVideoStart], ProtoField(tag=3, wire=WireType.MESSAGE, cls=GeneratedVideoStart)] = None
    file_preview: Annotated[Optional[FilePreviewStart], ProtoField(tag=4, wire=WireType.MESSAGE, cls=FilePreviewStart)] = None


class RenderCitation(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    kind: Annotated[RenderCitationCitationKind, ProtoField(tag=2, wire=WireType.INT32)] = RenderCitationCitationKind.CITATION_KIND_UNSPECIFIED
    url: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    citation_id: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0


class RenderSearchedImage(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    image: Annotated[Optional[ImageResult], ProtoField(tag=2, wire=WireType.MESSAGE, cls=ImageResult)] = None
    size: Annotated[RenderSearchedImageSize, ProtoField(tag=3, wire=WireType.INT32)] = RenderSearchedImageSize.SIZE_UNSPECIFIED


class RenderGeneratedImage(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    query: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    image_chunk: Annotated[Optional[ImageChunk], ProtoField(tag=3, wire=WireType.MESSAGE, cls=ImageChunk)] = None
    tool_call_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class RenderEditedImage(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    query: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    image_chunk: Annotated[Optional[ImageChunk], ProtoField(tag=3, wire=WireType.MESSAGE, cls=ImageChunk)] = None
    tool_call_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    image_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class VideoChunk(BaseModel):
    videoUuid: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    progress: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    videoData: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    audioUuids: Annotated[List[str], ProtoField(tag=4, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    audioData: Annotated[List[str], ProtoField(tag=5, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    videoPrompt: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    imageReference: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    audioTranscripts: Annotated[List[str], ProtoField(tag=8, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    moderated: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = False
    originalPrompt: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    mode: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    resolution: Annotated[Optional[Resolution], ProtoField(tag=12, wire=WireType.MESSAGE, cls=Resolution)] = None
    r_rated: Annotated[bool, ProtoField(tag=13, wire=WireType.BOOL)] = False
    modelName: Annotated[str, ProtoField(tag=14, wire=WireType.STRING)] = ""
    video_reference_id: Annotated[str, ProtoField(tag=15, wire=WireType.STRING)] = ""
    shot_summary: Annotated[str, ProtoField(tag=16, wire=WireType.STRING)] = ""
    duration: Annotated[float, ProtoField(tag=17, wire=WireType.FLOAT)] = 0.0
    extended_from_media_id: Annotated[str, ProtoField(tag=18, wire=WireType.STRING)] = ""
    suggested_moderation_rule: Annotated[int, ProtoField(tag=19, wire=WireType.INT32)] = 0
    side_by_side_index: Annotated[int, ProtoField(tag=20, wire=WireType.INT32)] = 0
    video_streaming_index: Annotated[int, ProtoField(tag=21, wire=WireType.INT32)] = 0
    video_streaming_duration: Annotated[float, ProtoField(tag=22, wire=WireType.FLOAT)] = 0.0
    isRootRRated: Annotated[bool, ProtoField(tag=23, wire=WireType.BOOL)] = False
    isRootUserUploaded: Annotated[bool, ProtoField(tag=24, wire=WireType.BOOL)] = False
    isRootCelebrity: Annotated[bool, ProtoField(tag=25, wire=WireType.BOOL)] = False
    isRootChild: Annotated[bool, ProtoField(tag=26, wire=WireType.BOOL)] = False
    resolution_name: Annotated[str, ProtoField(tag=27, wire=WireType.STRING)] = ""
    upsampled_prompt: Annotated[str, ProtoField(tag=28, wire=WireType.STRING)] = ""
    applied_moderation_rule: Annotated[str, ProtoField(tag=29, wire=WireType.STRING)] = ""
    video_url: Annotated[str, ProtoField(tag=30, wire=WireType.STRING)] = ""
    rejection_reason: Annotated[MediaRejectionReason, ProtoField(tag=31, wire=WireType.INT32)] = MediaRejectionReason.MEDIA_REJECTION_REASON_UNSPECIFIED


class RenderGeneratedVideo(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    prompt: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    aspect_ratio: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    video_chunk: Annotated[Optional[VideoChunk], ProtoField(tag=4, wire=WireType.MESSAGE, cls=VideoChunk)] = None
    tool_call_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class RenderFilePreview(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    file_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    content_type: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    mime_type: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    file_size: Annotated[int, ProtoField(tag=5, wire=WireType.INT64)] = 0
    url: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    preview_data_url: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    preview_doc_url: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    thumbnail_url: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    thumbnail_dark_url: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    file_path: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""


class RenderImagineMediaBoard(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    layout: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    asset_ids: Annotated[List[str], ProtoField(tag=4, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class OutputChunk(BaseModel):
    metadata: Annotated[Optional[OutputChunkMetadata], ProtoField(tag=1, wire=WireType.MESSAGE, cls=OutputChunkMetadata)] = None
    text: Annotated[Optional[Text], ProtoField(tag=2, wire=WireType.MESSAGE, cls=Text)] = None
    user_input_request: Annotated[Optional[UserInputRequest], ProtoField(tag=3, wire=WireType.MESSAGE, cls=UserInputRequest)] = None
    follow_up_suggestions: Annotated[Optional[FollowUpSuggestions], ProtoField(tag=4, wire=WireType.MESSAGE, cls=FollowUpSuggestions)] = None
    ui_layout: Annotated[Optional[UILayout], ProtoField(tag=5, wire=WireType.MESSAGE, cls=UILayout)] = None
    progress_report: Annotated[Optional[ProgressReport], ProtoField(tag=6, wire=WireType.MESSAGE, cls=ProgressReport)] = None
    tool_usage_card: Annotated[Optional[ToolUsageCard], ProtoField(tag=100, wire=WireType.MESSAGE, cls=ToolUsageCard)] = None
    tool_result: Annotated[Optional[ToolResult], ProtoField(tag=101, wire=WireType.MESSAGE, cls=ToolResult)] = None
    tool_partial_result: Annotated[Optional[ToolPartialResult], ProtoField(tag=102, wire=WireType.MESSAGE, cls=ToolPartialResult)] = None
    client_tool_call: Annotated[Optional[ToolCall], ProtoField(tag=103, wire=WireType.MESSAGE, cls=ToolCall)] = None
    render_start: Annotated[Optional[RenderStart], ProtoField(tag=200, wire=WireType.MESSAGE, cls=RenderStart)] = None
    render_citation: Annotated[Optional[RenderCitation], ProtoField(tag=201, wire=WireType.MESSAGE, cls=RenderCitation)] = None
    render_searched_image: Annotated[Optional[RenderSearchedImage], ProtoField(tag=202, wire=WireType.MESSAGE, cls=RenderSearchedImage)] = None
    render_generated_image: Annotated[Optional[RenderGeneratedImage], ProtoField(tag=203, wire=WireType.MESSAGE, cls=RenderGeneratedImage)] = None
    render_edited_image: Annotated[Optional[RenderEditedImage], ProtoField(tag=204, wire=WireType.MESSAGE, cls=RenderEditedImage)] = None
    render_generated_video: Annotated[Optional[RenderGeneratedVideo], ProtoField(tag=205, wire=WireType.MESSAGE, cls=RenderGeneratedVideo)] = None
    render_file_preview: Annotated[Optional[RenderFilePreview], ProtoField(tag=206, wire=WireType.MESSAGE, cls=RenderFilePreview)] = None
    render_imagine_media_board: Annotated[Optional[RenderImagineMediaBoard], ProtoField(tag=207, wire=WireType.MESSAGE, cls=RenderImagineMediaBoard)] = None


class Webpage(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    snippet: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    extra_snippets: Annotated[List[str], ProtoField(tag=4, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    date_published: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    date_last_crawled: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    humanized_date: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    language: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    cached_page_url: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    parsed_text: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    time_accessed: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=12, wire=WireType.STRING)] = ""
    site_name: Annotated[str, ProtoField(tag=13, wire=WireType.STRING)] = ""
    creator: Annotated[str, ProtoField(tag=14, wire=WireType.STRING)] = ""
    image: Annotated[str, ProtoField(tag=15, wire=WireType.STRING)] = ""
    images: Annotated[str, ProtoField(tag=16, wire=WireType.STRING)] = ""
    breaking: Annotated[bool, ProtoField(tag=17, wire=WireType.BOOL)] = False
    favicon: Annotated[str, ProtoField(tag=18, wire=WireType.STRING)] = ""
    favicon_base64: Annotated[str, ProtoField(tag=19, wire=WireType.STRING)] = ""


class XPostMediaEntity(BaseModel):
    media_key: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    type_f: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    url: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    width: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    height: Annotated[int, ProtoField(tag=5, wire=WireType.INT32)] = 0
    preview_image_url: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class XPostUrlEntity(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    expanded_url: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    display_url: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    start: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    end: Annotated[int, ProtoField(tag=5, wire=WireType.INT32)] = 0


class XPostHashtagEntity(BaseModel):
    tag: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    start: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    end: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0


class XPostMentionEntity(BaseModel):
    username: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    start: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    end: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0


class XPostEntitiesEntity(BaseModel):
    media: Annotated[List[XPostMediaEntity], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=XPostMediaEntity)] = Field(default_factory=list)
    urls: Annotated[List[XPostUrlEntity], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=XPostUrlEntity)] = Field(default_factory=list)
    hashtags: Annotated[List[XPostHashtagEntity], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=XPostHashtagEntity)] = Field(default_factory=list)
    mentions: Annotated[List[XPostMentionEntity], ProtoField(tag=4, wire=WireType.REPEATED_MESSAGE, cls=XPostMentionEntity)] = Field(default_factory=list)


class XPostMediaImage(BaseModel):
    type_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    base64: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class XPostMediaVideo(BaseModel):
    type_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    base64_frames: Annotated[List[str], ProtoField(tag=2, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    subtitle_buckets: Annotated[List[str], ProtoField(tag=3, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    max_frames: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    duration: Annotated[float, ProtoField(tag=5, wire=WireType.FLOAT)] = 0.0
    bucket_duration: Annotated[float, ProtoField(tag=6, wire=WireType.FLOAT)] = 0.0
    fallback_image_base64: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""

