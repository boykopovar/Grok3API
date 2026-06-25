from __future__ import annotations

from typing import Annotated, List, Optional

from enum import IntEnum
from pydantic import BaseModel, Field

from grok3api.types.pb_meta import ProtoField, WireType
from grok3api.types.proto.chat import ToolUsageCard
from grok3api.types.proto.connectors_manager import ConnectorAttribute


class Effort(IntEnum):
    UNSPECIFIED = 0
    LOW = 1
    HIGH = 2
    AUTO = 3


class EnablePreferButtonTrigger(IntEnum):
    ENABLE_PREFER_BUTTON_TRIGGER_ALWAYS = 0
    ENABLE_PREFER_BUTTON_TRIGGER_ONE_RESPONSE_FINISHED = 1
    ENABLE_PREFER_BUTTON_TRIGGER_ALL_RESPONSES_FINISHED = 2


class MediaRejectionReason(IntEnum):
    MEDIA_REJECTION_REASON_UNSPECIFIED = 0
    MEDIA_REJECTION_REASON_IP = 1
    MEDIA_REJECTION_REASON_SAFETY = 2


class ProgressReportCategory(IntEnum):
    PROGRESS_REPORT_CATEGORY_UNKNOWN = 0
    PROGRESS_REPORT_CATEGORY_ATTACHMENTS_PREPROCESSING = 1
    PROGRESS_REPORT_CATEGORY_HISTORY_ATTACHMENTS_PREPROCESSING = 2
    PROGRESS_REPORT_CATEGORY_WEBPAGE_ATTACHMENTS_PREPROCESSING = 3
    PROGRESS_REPORT_CATEGORY_HISTORY_WEBPAGE_ATTACHMENTS_PREPROCESSING = 4
    TOOL_PROCESSING = 5
    HEAVY_ROLLOUT = 6


class ProgressReportState(IntEnum):
    PROGRESS_REPORT_STATUS_UNKNOWN = 0
    PROGRESS_REPORT_STATUS_PENDING = 1
    PROGRESS_REPORT_STATUS_SUCCESS = 2
    PROGRESS_REPORT_STATUS_FAILURE = 3


class Kind(IntEnum):
    KIND_UNKNOWN = 0
    KIND_SINGLE_THINKING_DIFFERENT_SUMMARY = 1


class Mode(IntEnum):
    MODE_UNSPECIFIED = 0
    MODE_DEFAULT = 1
    MODE_PLAN = 2


class SingleThinkingDifferentSummaryKind(IntEnum):
    KIND_UNKNOWN = 0
    KIND_SINGLE_THINKING_DIFFERENT_SUMMARY = 1


class ToolPermissionScope(IntEnum):
    TOOL_PERMISSION_SCOPE_UNSPECIFIED = 0
    TOOL_PERMISSION_SCOPE_CONVERSATION = 1
    TOOL_PERMISSION_SCOPE_GLOBAL = 2


class ConnectorType(IntEnum):
    CONNECTOR_TYPE_UNKNOWN = 0
    CONNECTOR_TYPE_GOOGLE_DRIVE = 1
    CONNECTOR_TYPE_NOTION = 2
    CONNECTOR_TYPE_SLACK = 3
    CONNECTOR_TYPE_GMAIL = 4
    CONNECTOR_TYPE_GOOGLE_CALENDAR = 5
    CONNECTOR_TYPE_SHAREPOINT = 6
    CONNECTOR_TYPE_OUTLOOK = 7
    CONNECTOR_TYPE_MICROSOFT_TEAMS = 8


class AlignmentProvider(IntEnum):
    ALIGNMENT_PROVIDER_UNSPECIFIED = 0
    ALIGNMENT_PROVIDER_FORCED = 1
    ALIGNMENT_PROVIDER_WHISPER = 2
    ALIGNMENT_PROVIDER_HYBRID_FORCED_EN = 3


class ImportedMemoryStatus(IntEnum):
    IMPORTED_MEMORY_STATUS_UNSPECIFIED = 0
    IMPORTED_MEMORY_STATUS_NONE = 1
    IMPORTED_MEMORY_STATUS_PENDING = 2
    IMPORTED_MEMORY_STATUS_COMPLETE = 3


class ListConversationsMatchType(IntEnum):
    UNKNOWN = 0
    MATCH_TITLE = 1
    MATCH_MESSAGE = 2


class ListShareLinksOrderBy(IntEnum):
    LIST_SHARE_LINKS_ORDER_BY_INVALID = 0
    LIST_SHARE_LINKS_ORDER_BY_CREATE_TIME = 1
    LIST_SHARE_LINKS_ORDER_BY_VIEW_COUNT = 2


class MediaPostActionType(IntEnum):
    MEDIA_POST_ACTION_TYPE_INVALID = 0
    MEDIA_POST_ACTION_TYPE_LIKE = 1
    MEDIA_POST_ACTION_TYPE_SHARE = 2
    MEDIA_POST_ACTION_TYPE_DOWNLOAD = 3
    MEDIA_POST_ACTION_TYPE_DELETE = 4
    MEDIA_POST_ACTION_TYPE_UPSCALE_VIDEO = 5


class MediaPostGenerateType(IntEnum):
    MEDIA_POST_GENERATE_TYPE_UNSPECIFIED = 0
    MEDIA_POST_GENERATE_TYPE_IMAGE_GEN = 1
    MEDIA_POST_GENERATE_TYPE_IMAGE_EDIT = 2


class MediaPostMediaStatus(IntEnum):
    MEDIA_POST_MEDIA_STATUS_INVALID = 0
    MEDIA_POST_MEDIA_STATUS_DRAFT_STARTED = 1
    MEDIA_POST_MEDIA_STATUS_DRAFT_COMPLETE = 2
    MEDIA_POST_MEDIA_STATUS_DRAFT_FAILED = 3
    MEDIA_POST_MEDIA_STATUS_PUBLISHED = 4


class MediaPostPlatform(IntEnum):
    MEDIA_POST_PLATFORM_INVALID = 0
    MEDIA_POST_PLATFORM_GROK = 1
    MEDIA_POST_PLATFORM_X = 2


class MediaPostSource(IntEnum):
    MEDIA_POST_SOURCE_INVALID = 0
    MEDIA_POST_SOURCE_PUBLIC = 1
    MEDIA_POST_SOURCE_LIKED = 2
    MEDIA_POST_SOURCE_OWNED = 3
    MEDIA_POST_SOURCE_CHARACTER_MENTIONED = 4


class MediaPostType(IntEnum):
    MEDIA_POST_TYPE_INVALID = 0
    MEDIA_POST_TYPE_IMAGE = 1
    MEDIA_POST_TYPE_VIDEO = 2
    MEDIA_POST_TYPE_TEMPLATE = 3


class MediaPostVisibility(IntEnum):
    MEDIA_POST_VISIBILITY_INVALID = 0
    MEDIA_POST_VISIBILITY_PUBLIC = 1
    MEDIA_POST_VISIBILITY_PRIVATE = 2


class MediaSearchIndexStatus(IntEnum):
    MEDIA_SEARCH_INDEX_STATUS_NOT_ELIGIBLE = 0
    MEDIA_SEARCH_INDEX_STATUS_INDEXING = 1
    MEDIA_SEARCH_INDEX_STATUS_READY = 2


class MediaSearchResultType(IntEnum):
    MEDIA_SEARCH_RESULT_TYPE_MEDIA_POST = 0
    MEDIA_SEARCH_RESULT_TYPE_CANVAS_NODE = 1


class MemoryV2OperationType(IntEnum):
    MEMORY_V2_OPERATION_TYPE_ADD = 0
    MEMORY_V2_OPERATION_TYPE_EDIT = 1
    MEMORY_V2_OPERATION_TYPE_DELETE = 2


class ModeSubscriptionTier(IntEnum):
    TIER_UNSPECIFIED = 0
    TIER_SUPERGROK = 1
    TIER_SUPERGROK_HEAVY = 2
    TIER_SUPERGROK_LITE = 3


class ModeTag(IntEnum):
    TAG_UNSPECIFIED = 0
    TAG_SECONDARY = 1
    TAG_MCP = 2
    TAG_PLANE = 3
    TAG_PRIMARY = 4


class OriginalRefType(IntEnum):
    ORIGINAL_REF_TYPE_INVALID = 0
    ORIGINAL_REF_TYPE_VIDEO_EXTENSION = 1
    ORIGINAL_REF_TYPE_VIDEO_EDIT = 2
    ORIGINAL_REF_TYPE_IMAGE_EDIT = 3
    ORIGINAL_REF_TYPE_MULTI_REF_IMAGE_EDIT = 4
    ORIGINAL_REF_TYPE_DOODLE_IMAGE_EDIT = 5
    ORIGINAL_REF_TYPE_TEMPLATE = 6
    ORIGINAL_REF_TYPE_VIDEO_REMIX = 7


class PipelineStepStatus(IntEnum):
    PIPELINE_STEP_STATUS_PENDING = 0
    PIPELINE_STEP_STATUS_RUNNING = 1
    PIPELINE_STEP_STATUS_COMPLETED = 2
    PIPELINE_STEP_STATUS_FAILED = 3


class PipelineTemplateListFilter(IntEnum):
    PIPELINE_TEMPLATE_LIST_FILTER_FEATURED = 0
    PIPELINE_TEMPLATE_LIST_FILTER_MY_TEMPLATES = 1
    PIPELINE_TEMPLATE_LIST_FILTER_ALL_PUBLISHED = 2


class PipelineTemplateVisibility(IntEnum):
    PIPELINE_TEMPLATE_VISIBILITY_PRIVATE = 0
    PIPELINE_TEMPLATE_VISIBILITY_PUBLISHED = 1


class ProductAvailability(IntEnum):
    IN_STOCK = 0
    AVAILABLE_FOR_ORDER = 1
    OUT_OF_STOCK = 2
    DISCONTINUED = 3
    PREORDER = 4


class ProductCondition(IntEnum):
    NEW = 0
    REFURBISHED = 1
    USED = 2


class ReasoningUiLayout(IntEnum):
    UNSPECIFIED = 0
    UNIFIED = 1
    SPLIT = 2
    HEAVY = 3
    FUNCTION_CALL = 4


class RefinementLevel(IntEnum):
    REFINEMENT_LEVEL_UNSPECIFIED = 0
    REFINEMENT_LEVEL_LEGACY_ENHANCE = 1
    REFINEMENT_LEVEL_POLISH = 2
    REFINEMENT_LEVEL_ENRICH = 3


class RequestKind(IntEnum):
    DEFAULT = 0
    REASONING = 1
    DEEPSEARCH = 2
    DEEPERSEARCH = 3


class ResponseStatus(IntEnum):
    RESPONSE_STATUS_UNKNOWN = 0
    RESPONSE_STATUS_ACTIVE = 1
    RESPONSE_STATUS_FINISHED = 2
    RESPONSE_STATUS_ERROR = 3


class StreamErrorSeverity(IntEnum):
    STREAM_ERROR_SEVERITY_UNKNOWN = 0
    STREAM_ERROR_SEVERITY_NORMAL = 1
    STREAM_ERROR_SEVERITY_FATAL = 2


class SuggestionType(IntEnum):
    SUGGESTION_TYPE_UNSPECIFIED = 0
    SUGGESTION_TYPE_SEARCH_COMPLETION = 1
    SUGGESTION_TYPE_STOCK = 2
    SUGGESTION_TYPE_QUICK_ANSWER = 3
    SUGGESTION_TYPE_GROK_COMPLETION = 4


class TextBoxSize(IntEnum):
    TEXT_BOX_SIZE_UNSPECIFIED = 0
    TEXT_BOX_SIZE_SM = 1
    TEXT_BOX_SIZE_MD = 2
    TEXT_BOX_SIZE_LG = 3


class UploadJobStatus(IntEnum):
    UNSET = 0
    INITIALIZED = 1
    UPLOADING = 2
    UPLOADED = 3
    PROCESSING = 4
    ERROR = 5
    SUCCESS = 6
    ABORTED = 7
    EXPIRED = 8
    RETRYING = 9


class UploadMethod(IntEnum):
    UPLOAD_METHOD_UNSPECIFIED = 0
    UPLOAD_METHOD_SINGLE_PUT = 1
    UPLOAD_METHOD_RESUMABLE = 2
    UPLOAD_METHOD_MULTIPART = 3


class UpscaleTargetResolution(IntEnum):
    UPSCALE_TARGET_RESOLUTION_HD = 0
    UPSCALE_TARGET_RESOLUTION_1080P = 1


class UsagePeriodType(IntEnum):
    USAGE_PERIOD_TYPE_UNSPECIFIED = 0
    USAGE_PERIOD_TYPE_MONTHLY = 1
    USAGE_PERIOD_TYPE_WEEKLY = 2


class UsageUpgradeTier(IntEnum):
    USAGE_UPGRADE_TIER_UNSPECIFIED = 0
    USAGE_UPGRADE_TIER_SUPER_GROK_LITE = 1
    USAGE_UPGRADE_TIER_SUPER_GROK = 2
    USAGE_UPGRADE_TIER_SUPER_GROK_HEAVY = 3


class UserFeedbackType(IntEnum):
    general_feedback = 0
    issue_report = 1
    child_safety = 2
    response_feedback = 3
    non_consensual_intimate_content = 4


class VoiceAdminSortBy(IntEnum):
    VOICE_ADMIN_SORT_BY_UNSPECIFIED = 0
    VOICE_ADMIN_SORT_BY_CREATED_AT_ASC = 1
    VOICE_ADMIN_SORT_BY_SAVE_COUNT = 2


class VoiceVisibility(IntEnum):
    VOICE_VISIBILITY_UNSPECIFIED = 0
    VOICE_VISIBILITY_PRIVATE = 1
    VOICE_VISIBILITY_UNLISTED = 2
    VOICE_VISIBILITY_PUBLIC = 3


class DeviceType(IntEnum):
    UNKNOWN = 0
    IOS = 1
    ANDROID = 2


class Gender(IntEnum):
    FEMALE = 0
    MALE = 1
    UNISEX = 2


class AddMobileDeviceNotificationTokenRequestDeviceType(IntEnum):
    UNKNOWN = 0
    IOS = 1
    ANDROID = 2


class EffortDecisionEffort(IntEnum):
    UNSPECIFIED = 0
    LOW = 1
    HIGH = 2


class GenderAttributeGender(IntEnum):
    FEMALE = 0
    MALE = 1
    UNISEX = 2


class UiLayoutEffort(IntEnum):
    UNSPECIFIED = 0
    LOW = 1
    HIGH = 2
    AUTO = 3


class ActiveOfferType(IntEnum):
    ACTIVE_OFFER_TYPE_UNSPECIFIED = 0
    ACTIVE_OFFER_FREE_TRIAL = 1
    ACTIVE_OFFER_DISCOUNT = 2
    ACTIVE_OFFER_PAY_UPFRONT = 3


class AfterCompletionType(IntEnum):
    hosted_confirmation = 0
    portal_homepage = 1
    redirect_to_url = 2


class ArtifactInlineStatusType(IntEnum):
    DEFAULT_ARTIFACT_INLINE_STATUS = 0
    SHOW_INLINE_ARTIFACT_INLINE_STATUS = 1
    SHOW_SIDEBAR_ARTIFACT_INLINE_STATUS = 2


class AssetSource(IntEnum):
    SOURCE_ANY = 0
    SOURCE_UPLOADED = 1
    SOURCE_GENERATED = 2


class BillingInterval(IntEnum):
    BILLING_INTERVAL_UNKNOWN = 0
    BILLING_INTERVAL_MONTHLY = 1
    BILLING_INTERVAL_YEARLY = 2


class BillingPortalFlowType(IntEnum):
    payment_method_update = 0
    subscription_cancel = 1
    subscription_update = 2


class ModelMode(IntEnum):
    BASE = 0
    THINK = 1
    DEEPSEARCH = 2
    IMAGEGEN = 3


class NotificationUiOption(IntEnum):
    DEFAULT = 0
    EMAIL_ONLY = 1
    APP_ONLY = 2
    OFF = 3


class OfferPurpose(IntEnum):
    OFFER_PURPOSE_UNSPECIFIED = 0
    OFFER_PURPOSE_ACQUISITION = 1
    OFFER_PURPOSE_RETENTION = 2
    OFFER_PURPOSE_WINBACK = 3


class ScheduledChangeType(IntEnum):
    SCHEDULED_CHANGE_TYPE_UNSPECIFIED = 0
    SCHEDULED_CHANGE_TYPE_UPGRADE = 1
    SCHEDULED_CHANGE_TYPE_DOWNGRADE = 2
    SCHEDULED_CHANGE_TYPE_INTERVAL_SWITCH = 3


class StripeSubscriptionStatus(IntEnum):
    STRIPE_SUBSCRIPTION_STATUS_UNKNOWN = 0
    STRIPE_SUBSCRIPTION_STATUS_ACTIVE = 1
    STRIPE_SUBSCRIPTION_STATUS_INCOMPLETE = 2
    STRIPE_SUBSCRIPTION_STATUS_INCOMPLETE_EXPIRED = 3
    STRIPE_SUBSCRIPTION_STATUS_TRIALING = 4
    STRIPE_SUBSCRIPTION_STATUS_PAST_DUE = 5
    STRIPE_SUBSCRIPTION_STATUS_CANCELED = 6
    STRIPE_SUBSCRIPTION_STATUS_UNPAID = 7
    STRIPE_SUBSCRIPTION_STATUS_PAUSED = 8
    STRIPE_SUBSCRIPTION_STATUS_UPDATE_IN_PROGRESS = 9


class SubscriptionProvider(IntEnum):
    SUBSCRIPTION_PROVIDER_INVALID = 0
    SUBSCRIPTION_PROVIDER_GOOGLE = 1
    SUBSCRIPTION_PROVIDER_APPLE = 2
    SUBSCRIPTION_PROVIDER_STRIPE = 3
    SUBSCRIPTION_PROVIDER_X = 4
    SUBSCRIPTION_PROVIDER_ENTERPRISE = 5
    SUBSCRIPTION_PROVIDER_ADHOC = 6
    SUBSCRIPTION_PROVIDER_EAPI = 7
    SUBSCRIPTION_PROVIDER_PAYPAL = 8
    SUBSCRIPTION_PROVIDER_BRAINTREE = 9


class SubscriptionStatus(IntEnum):
    SUBSCRIPTION_STATUS_INVALID = 0
    SUBSCRIPTION_STATUS_ACTIVE = 1
    SUBSCRIPTION_STATUS_INACTIVE = 2


class SubscriptionTier(IntEnum):
    SUBSCRIPTION_TIER_INVALID = 0
    SUBSCRIPTION_TIER_GROK_PRO = 1
    SUBSCRIPTION_TIER_X_BASIC = 2
    SUBSCRIPTION_TIER_X_PREMIUM = 3
    SUBSCRIPTION_TIER_X_PREMIUM_PLUS = 4
    SUBSCRIPTION_TIER_SUPER_GROK_PRO = 5
    SUBSCRIPTION_TIER_SUPER_GROK_LITE = 6


class SubscriptionType(IntEnum):
    MONTHLY = 0
    YEARLY = 1


class TaskCadence(IntEnum):
    TASK_CADENCE_ONCE = 0
    TASK_CADENCE_ONCE_DAILY = 1
    TASK_CADENCE_ONCE_WEEKLY = 2
    TASK_CADENCE_ONCE_WEEKDAY = 3
    TASK_CADENCE_ONCE_MONTHLY = 4
    TASK_CADENCE_ONCE_ANNUALLY = 5
    TASK_CADENCE_ONCE_INSTANT = 6


class TaskNotificationDecision(IntEnum):
    DISABLED = 0
    YES = 1
    NO = 2


class TaskResultStatus(IntEnum):
    TASK_RESULT_PENDING = 0
    TASK_RESULT_SUCCESS = 1
    TASK_RESULT_ERROR = 2


class UploadedFileSourceType(IntEnum):
    SELF_UPLOAD_FILE_SOURCE = 0
    GOOGLE_DRIVE_FILE_SOURCE = 1
    ONE_DRIVE_FILE_SOURCE = 2
    IMAGINE_SELF_UPLOAD_FILE_SOURCE = 3
    IMAGINE_GENERATED_FILE_SOURCE = 4


class UserActivity(IntEnum):
    USER_ACTIVITY_UNKNOWN = 0
    USER_ACTIVITY_SUBSCRIBE = 1
    USER_ACTIVITY_CANCEL = 2
    USER_ACTIVITY_RESUME = 3
    USER_ACTIVITY_UPGRADE = 4


class OrderBy(IntEnum):
    ORDER_BY_INVALID = 0
    ORDER_BY_RELEVANCY = 1
    ORDER_BY_CREATE_TIME = 2
    ORDER_BY_LAST_USE_TIME = 3
    ORDER_BY_NAME = 4


class ChangeOrigin(IntEnum):
    INVALID_ORIGIN = 0
    PURCHASE = 1
    SPEND = 2
    REFUND = 3
    MANUAL = 4
    AUTO_PURCHASE = 5


class TopUpStatus(IntEnum):
    INVALID = 0
    TO_GENERATE_INVOICE = 1
    FAILED_TO_GENERATE_INVOICE = 2
    TO_CHARGE = 3
    FAILED_TO_CHARGE = 4
    SUCCEEDED = 5


class ListAssetMetadataRequestOrderBy(IntEnum):
    ORDER_BY_INVALID = 0
    ORDER_BY_RELEVANCY = 1
    ORDER_BY_CREATE_TIME = 2
    ORDER_BY_LAST_USE_TIME = 3
    ORDER_BY_NAME = 4
    ORDER_BY_MIME_TYPE = 5
    ORDER_BY_CONTENT_SIZE = 9


class ListSystemPromptsRequestOrderBy(IntEnum):
    ORDER_BY_INVALID = 0
    ORDER_BY_RELEVANCY = 1
    ORDER_BY_CREATE_TIME = 2
    ORDER_BY_LAST_USE_TIME = 3
    ORDER_BY_NAME = 4


class ListWorkspacesRequestOrderBy(IntEnum):
    ORDER_BY_INVALID = 0
    ORDER_BY_RELEVANCY = 1
    ORDER_BY_CREATE_TIME = 2
    ORDER_BY_LAST_USE_TIME = 3
    ORDER_BY_NAME = 4


class PrepaidBalanceChangeChangeOrigin(IntEnum):
    INVALID_ORIGIN = 0
    PURCHASE = 1
    SPEND = 2
    REFUND = 3
    MANUAL = 4
    AUTO_PURCHASE = 5


class PrepaidBalanceChangeTopUpStatus(IntEnum):
    INVALID = 0
    TO_GENERATE_INVOICE = 1
    FAILED_TO_GENERATE_INVOICE = 2
    TO_CHARGE = 3
    FAILED_TO_CHARGE = 4
    SUCCEEDED = 5


class CodeExecutionResult(BaseModel):
    stdout: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    stderr: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    exit_code: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    command_timed_out: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False


class CollectionSearchResultItem(BaseModel):
    file_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    size_bytes: Annotated[int, ProtoField(tag=3, wire=WireType.INT64)] = 0
    content_type: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    created_at: Annotated[str, ProtoField(tag=5, wire=WireType.TIMESTAMP)] = ""
    expires_at: Annotated[str, ProtoField(tag=6, wire=WireType.TIMESTAMP)] = ""
    upload_status: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    upload_error_message: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    processing_status: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    file_path: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    url: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    query: Annotated[str, ProtoField(tag=12, wire=WireType.STRING)] = ""
    chunk_content: Annotated[str, ProtoField(tag=13, wire=WireType.STRING)] = ""
    chunk_id: Annotated[str, ProtoField(tag=14, wire=WireType.STRING)] = ""


class ConnectorSearchResultItem(BaseModel):
    file_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    connector_type: Annotated[ConnectorType, ProtoField(tag=2, wire=WireType.INT32)] = ConnectorType.CONNECTOR_TYPE_UNKNOWN
    query: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    document_type: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    document_title: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    document_source_url: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    chunk_content: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    chunk_id: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""


class FollowUpSuggestionProperties(BaseModel):
    message_type: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    follow_up_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ToolOverrides(BaseModel):
    image_gen: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    web_search: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    x_search: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    x_media_search: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    trends_search: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False
    x_post_analyze: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    video_gen: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False
    audio_gen: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False
    gmail_search: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = False
    google_calendar_search: Annotated[bool, ProtoField(tag=10, wire=WireType.BOOL)] = False
    google_drive_search: Annotated[bool, ProtoField(tag=11, wire=WireType.BOOL)] = False
    outlook_search: Annotated[bool, ProtoField(tag=12, wire=WireType.BOOL)] = False
    outlook_calendar_search: Annotated[bool, ProtoField(tag=13, wire=WireType.BOOL)] = False
    document_search: Annotated[bool, ProtoField(tag=14, wire=WireType.BOOL)] = False


class FollowUpSuggestion(BaseModel):
    properties: Annotated[Optional[FollowUpSuggestionProperties], ProtoField(tag=1, wire=WireType.MESSAGE, cls=FollowUpSuggestionProperties)] = None
    label: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    tool_overrides: Annotated[Optional[ToolOverrides], ProtoField(tag=3, wire=WireType.MESSAGE, cls=ToolOverrides)] = None


class FollowUpSuggestions(BaseModel):
    suggestions: Annotated[List[FollowUpSuggestion], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=FollowUpSuggestion)] = Field(default_factory=list)


class ProgressReport(BaseModel):
    category: Annotated[ProgressReportCategory, ProtoField(tag=1, wire=WireType.INT32)] = ProgressReportCategory.PROGRESS_REPORT_CATEGORY_UNKNOWN
    state: Annotated[ProgressReportState, ProtoField(tag=2, wire=WireType.INT32)] = ProgressReportState.PROGRESS_REPORT_STATUS_UNKNOWN
    message: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    percentage: Annotated[float, ProtoField(tag=4, wire=WireType.FLOAT)] = 0.0


class Resolution(BaseModel):
    width: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    height: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class SingleThinkingDifferentSummary(BaseModel):
    kind: Annotated[SingleThinkingDifferentSummaryKind, ProtoField(tag=1, wire=WireType.INT32)] = SingleThinkingDifferentSummaryKind.KIND_UNKNOWN
    side_by_side_single_think_index: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    enable_prefer_button_trigger: Annotated[EnablePreferButtonTrigger, ProtoField(tag=3, wire=WireType.INT32)] = EnablePreferButtonTrigger.ENABLE_PREFER_BUTTON_TRIGGER_ALWAYS


class WebSearchResult(BaseModel):
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


class XPostPublicMetrics(BaseModel):
    view_count: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    like_count: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    reply_count: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    retweet_count: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    quote_count: Annotated[int, ProtoField(tag=5, wire=WireType.INT32)] = 0


class XPostMediaVariant(BaseModel):
    bit_rate: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    content_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    url: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class XPostMedia(BaseModel):
    media_key: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    type_f: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    url: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    width: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    height: Annotated[int, ProtoField(tag=5, wire=WireType.INT32)] = 0
    preview_image_url: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    variants: Annotated[List[XPostMediaVariant], ProtoField(tag=7, wire=WireType.REPEATED_MESSAGE, cls=XPostMediaVariant)] = Field(default_factory=list)


class XPostUrl(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    expanded_url: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    display_url: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    start: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    end: Annotated[int, ProtoField(tag=5, wire=WireType.INT32)] = 0


class XPostHashtag(BaseModel):
    tag: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    start: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    end: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0


class XPostMention(BaseModel):
    username: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    start: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    end: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0


class XPostEntities(BaseModel):
    media: Annotated[List[XPostMedia], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=XPostMedia)] = Field(default_factory=list)
    urls: Annotated[List[XPostUrl], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=XPostUrl)] = Field(default_factory=list)
    hashtags: Annotated[List[XPostHashtag], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=XPostHashtag)] = Field(default_factory=list)
    mentions: Annotated[List[XPostMention], ProtoField(tag=4, wire=WireType.REPEATED_MESSAGE, cls=XPostMention)] = Field(default_factory=list)


class XPost(BaseModel):
    username: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    text: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=4, wire=WireType.TIMESTAMP)] = ""
    profile_image_url: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    post_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    citation_id: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    parent: Annotated[Optional[XPost], ProtoField(tag=9, wire=WireType.MESSAGE, cls=XPost)] = None
    parent_post_id: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    quote_post_id: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    quote: Annotated[Optional[XPost], ProtoField(tag=12, wire=WireType.MESSAGE, cls=XPost)] = None
    view_count: Annotated[int, ProtoField(tag=13, wire=WireType.INT32)] = 0
    community_note: Annotated[str, ProtoField(tag=14, wire=WireType.STRING)] = ""
    verified_type: Annotated[str, ProtoField(tag=15, wire=WireType.STRING)] = ""
    public_metrics: Annotated[Optional[XPostPublicMetrics], ProtoField(tag=16, wire=WireType.MESSAGE, cls=XPostPublicMetrics)] = None
    entities: Annotated[Optional[XPostEntities], ProtoField(tag=17, wire=WireType.MESSAGE, cls=XPostEntities)] = None
    text_markdown: Annotated[str, ProtoField(tag=18, wire=WireType.STRING)] = ""


class Connector(BaseModel):
    connector_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    attributes: Annotated[List[ConnectorAttribute], ProtoField(tag=2, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class AcceptedSuggestionType(BaseModel):
    type_f: Annotated[SuggestionType, ProtoField(tag=1, wire=WireType.INT32)] = SuggestionType.SUGGESTION_TYPE_UNSPECIFIED
    max_items: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class AddMobileDeviceNotificationTokenRequest(BaseModel):
    token: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    device_type: Annotated[AddMobileDeviceNotificationTokenRequestDeviceType, ProtoField(tag=2, wire=WireType.INT32)] = AddMobileDeviceNotificationTokenRequestDeviceType.UNKNOWN


class WebSearchResults(BaseModel):
    results: Annotated[List[WebSearchResult], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=WebSearchResult)] = Field(default_factory=list)


class XSearchResults(BaseModel):
    results: Annotated[List[XPost], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=XPost)] = Field(default_factory=list)


class RagResult(BaseModel):
    connector_type: Annotated[ConnectorType, ProtoField(tag=1, wire=WireType.INT32)] = ConnectorType.CONNECTOR_TYPE_UNKNOWN
    query: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    chunk_content: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    document_type: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    document_title: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    document_source_url: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class RagResults(BaseModel):
    results: Annotated[List[RagResult], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=RagResult)] = Field(default_factory=list)


class ConnectorSearchResults(BaseModel):
    results: Annotated[List[ConnectorSearchResultItem], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=ConnectorSearchResultItem)] = Field(default_factory=list)


class CollectionSearchResults(BaseModel):
    results: Annotated[List[CollectionSearchResultItem], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=CollectionSearchResultItem)] = Field(default_factory=list)


class MemoryV2UpdateResult(BaseModel):
    old_memory_substring: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    new_memory_substring: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    operation_type: Annotated[MemoryV2OperationType, ProtoField(tag=3, wire=WireType.INT32)] = MemoryV2OperationType.MEMORY_V2_OPERATION_TYPE_ADD
    expires_at_timestamp: Annotated[float, ProtoField(tag=4, wire=WireType.DOUBLE)] = 0.0


class ToolUsageResult(BaseModel):
    tool_usage_card_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    web_search_results: Annotated[Optional[WebSearchResults], ProtoField(tag=2, wire=WireType.MESSAGE, cls=WebSearchResults)] = None
    x_search_results: Annotated[Optional[XSearchResults], ProtoField(tag=3, wire=WireType.MESSAGE, cls=XSearchResults)] = None
    rag_results: Annotated[Optional[RagResults], ProtoField(tag=4, wire=WireType.MESSAGE, cls=RagResults)] = None
    connector_search_results: Annotated[Optional[ConnectorSearchResults], ProtoField(tag=5, wire=WireType.MESSAGE, cls=ConnectorSearchResults)] = None
    collection_search_results: Annotated[Optional[CollectionSearchResults], ProtoField(tag=6, wire=WireType.MESSAGE, cls=CollectionSearchResults)] = None
    memory_v2_update_result: Annotated[Optional[MemoryV2UpdateResult], ProtoField(tag=7, wire=WireType.MESSAGE, cls=MemoryV2UpdateResult)] = None
    code_execution_result: Annotated[Optional[CodeExecutionResult], ProtoField(tag=8, wire=WireType.MESSAGE, cls=CodeExecutionResult)] = None


class ResponseStep(BaseModel):
    text: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    tags: Annotated[List[str], ProtoField(tag=2, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    web_search_results: Annotated[List[WebSearchResult], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=WebSearchResult)] = Field(default_factory=list)
    xpost_ids: Annotated[List[str], ProtoField(tag=4, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    xposts: Annotated[List[XPost], ProtoField(tag=5, wire=WireType.REPEATED_MESSAGE, cls=XPost)] = Field(default_factory=list)
    tool_usage_results: Annotated[List[ToolUsageResult], ProtoField(tag=6, wire=WireType.REPEATED_MESSAGE, cls=ToolUsageResult)] = Field(default_factory=list)
    rollout_id: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    rag_results: Annotated[List[RagResult], ProtoField(tag=8, wire=WireType.REPEATED_MESSAGE, cls=RagResult)] = Field(default_factory=list)
    connector_search_results: Annotated[List[ConnectorSearchResultItem], ProtoField(tag=9, wire=WireType.REPEATED_MESSAGE, cls=ConnectorSearchResultItem)] = Field(default_factory=list)
    collection_search_results: Annotated[List[CollectionSearchResultItem], ProtoField(tag=10, wire=WireType.REPEATED_MESSAGE, cls=CollectionSearchResultItem)] = Field(default_factory=list)
    tool_usage_cards: Annotated[List[ToolUsageCard], ProtoField(tag=11, wire=WireType.REPEATED_MESSAGE, cls=ToolUsageCard)] = Field(default_factory=list)


class AddModelResponseRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    message: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    partial: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    parent_response_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    web_search_results: Annotated[List[WebSearchResult], ProtoField(tag=5, wire=WireType.REPEATED_MESSAGE, cls=WebSearchResult)] = Field(default_factory=list)
    xpost_ids: Annotated[List[str], ProtoField(tag=6, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    card_attachments_json: Annotated[List[str], ProtoField(tag=7, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    thinking_trace: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    steps: Annotated[List[ResponseStep], ProtoField(tag=9, wire=WireType.REPEATED_MESSAGE, cls=ResponseStep)] = Field(default_factory=list)
    banner_message: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    disclaimer: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""


class SupportedFastTools(BaseModel):
    calculator_tool: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    unit_conversion_tool: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class DeviceEnvInfo(BaseModel):
    dark_mode_enabled: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    device_pixel_ratio: Annotated[float, ProtoField(tag=2, wire=WireType.DOUBLE)] = 0.0
    screen_width: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    screen_height: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    viewport_width: Annotated[int, ProtoField(tag=5, wire=WireType.INT32)] = 0
    viewport_height: Annotated[int, ProtoField(tag=6, wire=WireType.INT32)] = 0


class GeoLocation(BaseModel):
    latitude: Annotated[float, ProtoField(tag=1, wire=WireType.FLOAT)] = 0.0
    longitude: Annotated[float, ProtoField(tag=2, wire=WireType.FLOAT)] = 0.0
    accuracy: Annotated[float, ProtoField(tag=3, wire=WireType.FLOAT)] = 0.0


class ImagineCanvasContext(BaseModel):
    target_canvas_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class AddResponseRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    message: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    model_name: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    parent_response_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    parent_quoted_text: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    disable_search: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False
    enable_image_generation: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = False
    image_attachments: Annotated[List[str], ProtoField(tag=16, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    return_image_bytes: Annotated[bool, ProtoField(tag=17, wire=WireType.BOOL)] = False
    return_raw_grok_in_xai_request: Annotated[bool, ProtoField(tag=19, wire=WireType.BOOL)] = False
    file_attachments: Annotated[List[str], ProtoField(tag=20, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    enable_image_streaming: Annotated[bool, ProtoField(tag=21, wire=WireType.BOOL)] = False
    image_generation_count: Annotated[int, ProtoField(tag=22, wire=WireType.INT32)] = 0
    force_concise: Annotated[bool, ProtoField(tag=23, wire=WireType.BOOL)] = False
    tool_overrides: Annotated[Optional[ToolOverrides], ProtoField(tag=24, wire=WireType.MESSAGE, cls=ToolOverrides)] = None
    enable_side_by_side: Annotated[bool, ProtoField(tag=25, wire=WireType.BOOL)] = False
    send_final_metadata: Annotated[bool, ProtoField(tag=27, wire=WireType.BOOL)] = False
    custom_instructions: Annotated[str, ProtoField(tag=28, wire=WireType.STRING)] = ""
    custom_personality: Annotated[str, ProtoField(tag=29, wire=WireType.STRING)] = ""
    deepsearch_preset: Annotated[str, ProtoField(tag=30, wire=WireType.STRING)] = ""
    image_edit_uri: Annotated[str, ProtoField(tag=31, wire=WireType.STRING)] = ""
    is_reasoning: Annotated[bool, ProtoField(tag=32, wire=WireType.BOOL)] = False
    system_prompt_name: Annotated[str, ProtoField(tag=33, wire=WireType.STRING)] = ""
    webpage_urls: Annotated[List[str], ProtoField(tag=34, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    metadata: Annotated[dict, ProtoField(tag=35, wire=WireType.JSON_STRUCT)] = Field(default_factory=dict)
    image_edit_uris: Annotated[List[str], ProtoField(tag=36, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    disable_text_follow_ups: Annotated[bool, ProtoField(tag=37, wire=WireType.BOOL)] = False
    disable_artifact: Annotated[bool, ProtoField(tag=38, wire=WireType.BOOL)] = False
    follow_up_type: Annotated[str, ProtoField(tag=39, wire=WireType.STRING)] = ""
    disable_artifact_diff: Annotated[bool, ProtoField(tag=40, wire=WireType.BOOL)] = False
    do_force_trigger_artifact: Annotated[bool, ProtoField(tag=41, wire=WireType.BOOL)] = False
    is_from_grok_files: Annotated[bool, ProtoField(tag=42, wire=WireType.BOOL)] = False
    resume_response_id: Annotated[str, ProtoField(tag=43, wire=WireType.STRING)] = ""
    selected_file_text_content: Annotated[str, ProtoField(tag=44, wire=WireType.STRING)] = ""
    selected_file_text_content_start_position: Annotated[int, ProtoField(tag=45, wire=WireType.INT32)] = 0
    selected_file_text_content_end_position: Annotated[int, ProtoField(tag=46, wire=WireType.INT32)] = 0
    disable_memory: Annotated[bool, ProtoField(tag=47, wire=WireType.BOOL)] = False
    force_side_by_side: Annotated[bool, ProtoField(tag=48, wire=WireType.BOOL)] = False
    thread_parent_id: Annotated[str, ProtoField(tag=49, wire=WireType.STRING)] = ""
    model_mode: Annotated[ModelMode, ProtoField(tag=50, wire=WireType.INT32)] = ModelMode.BASE
    models_user_can_use: Annotated[List[str], ProtoField(tag=51, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    skip_response_cache: Annotated[bool, ProtoField(tag=52, wire=WireType.BOOL)] = False
    is_async_chat: Annotated[bool, ProtoField(tag=53, wire=WireType.BOOL)] = False
    skip_cancel_current_inflight_requests: Annotated[bool, ProtoField(tag=54, wire=WireType.BOOL)] = False
    enable_nsfw: Annotated[bool, ProtoField(tag=55, wire=WireType.BOOL)] = False
    is_kids_mode: Annotated[bool, ProtoField(tag=56, wire=WireType.BOOL)] = False
    supported_fast_tools: Annotated[Optional[SupportedFastTools], ProtoField(tag=57, wire=WireType.MESSAGE, cls=SupportedFastTools)] = None
    is_regen_request: Annotated[bool, ProtoField(tag=58, wire=WireType.BOOL)] = False
    companion_id: Annotated[str, ProtoField(tag=59, wire=WireType.STRING)] = ""
    disable_self_harm_short_circuit: Annotated[bool, ProtoField(tag=61, wire=WireType.BOOL)] = False
    collection_ids: Annotated[List[str], ProtoField(tag=62, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    connector_ids: Annotated[List[str], ProtoField(tag=63, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    search_all_connectors: Annotated[bool, ProtoField(tag=64, wire=WireType.BOOL)] = False
    device_env_info: Annotated[Optional[DeviceEnvInfo], ProtoField(tag=65, wire=WireType.MESSAGE, cls=DeviceEnvInfo)] = None
    model_override_key: Annotated[str, ProtoField(tag=66, wire=WireType.STRING)] = ""
    browser_geo_location: Annotated[Optional[GeoLocation], ProtoField(tag=67, wire=WireType.MESSAGE, cls=GeoLocation)] = None
    disable_personalization: Annotated[bool, ProtoField(tag=69, wire=WireType.BOOL)] = False
    connectors: Annotated[List[Connector], ProtoField(tag=70, wire=WireType.REPEATED_MESSAGE, cls=Connector)] = Field(default_factory=list)
    imagine_project_id: Annotated[str, ProtoField(tag=71, wire=WireType.STRING)] = ""
    mode_id: Annotated[str, ProtoField(tag=72, wire=WireType.STRING)] = ""
    imagine_canvas_context: Annotated[Optional[ImagineCanvasContext], ProtoField(tag=75, wire=WireType.MESSAGE, cls=ImagineCanvasContext)] = None
    disabled_connector_ids: Annotated[List[str], ProtoField(tag=76, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class FileMetadata(BaseModel):
    file_metadata_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    file_mime_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    file_name: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    file_uri: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    parsed_file_uri: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=6, wire=WireType.TIMESTAMP)] = ""
    file_source: Annotated[UploadedFileSourceType, ProtoField(tag=7, wire=WireType.INT32)] = UploadedFileSourceType.SELF_UPLOAD_FILE_SOURCE
    third_party_file_id: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    third_party_file_mime_type: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""


class UiLayout(BaseModel):
    reasoning_ui_layout: Annotated[ReasoningUiLayout, ProtoField(tag=1, wire=WireType.INT32)] = ReasoningUiLayout.UNSPECIFIED
    will_think_long: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    effort: Annotated[UiLayoutEffort, ProtoField(tag=3, wire=WireType.INT32)] = UiLayoutEffort.UNSPECIFIED
    steer_model_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    rollout_ids: Annotated[List[str], ProtoField(tag=5, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class SideBySideConfig(BaseModel):
    single_thinking_different_summary: Annotated[Optional[SingleThinkingDifferentSummary], ProtoField(tag=1, wire=WireType.MESSAGE, cls=SingleThinkingDifferentSummary)] = None
    enable_prefer_button_trigger: Annotated[EnablePreferButtonTrigger, ProtoField(tag=2, wire=WireType.INT32)] = EnablePreferButtonTrigger.ENABLE_PREFER_BUTTON_TRIGGER_ALWAYS
    stream_final_answers_together: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    hide_thinking_trace: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    use_length_control_container: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False


class CalculatorTool(BaseModel):
    kind: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    expression: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    result: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class UnitConversionTool(BaseModel):
    kind: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    source_unit: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    source_value: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    target_unit: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    target_value: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    unit_type: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class FastToolResponse(BaseModel):
    title: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    subtitle: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    body: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    calculator_tool: Annotated[Optional[CalculatorTool], ProtoField(tag=4, wire=WireType.MESSAGE, cls=CalculatorTool)] = None
    unit_conversion_tool: Annotated[Optional[UnitConversionTool], ProtoField(tag=5, wire=WireType.MESSAGE, cls=UnitConversionTool)] = None


class RequestMetadata(BaseModel):
    model: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    mode: Annotated[ModelMode, ProtoField(tag=2, wire=WireType.INT32)] = ModelMode.BASE
    effort: Annotated[UiLayoutEffort, ProtoField(tag=3, wire=WireType.INT32)] = UiLayoutEffort.UNSPECIFIED


class ProductSource(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    source_product_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GenderAttribute(BaseModel):
    value__f: Annotated[GenderAttributeGender, ProtoField(tag=1, wire=WireType.INT32)] = GenderAttributeGender.FEMALE


class CustomAttribute(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    value__f: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ProductAttribute(BaseModel):
    gender: Annotated[Optional[GenderAttribute], ProtoField(tag=1, wire=WireType.MESSAGE, cls=GenderAttribute)] = None
    custom: Annotated[Optional[CustomAttribute], ProtoField(tag=2, wire=WireType.MESSAGE, cls=CustomAttribute)] = None


class Image(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    height: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    width: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0


class Video(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    height: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    width: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    duration_seconds: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    thumbnail: Annotated[Optional[Image], ProtoField(tag=5, wire=WireType.MESSAGE, cls=Image)] = None


class MediaItem(BaseModel):
    image: Annotated[Optional[Image], ProtoField(tag=1, wire=WireType.MESSAGE, cls=Image)] = None
    video: Annotated[Optional[Video], ProtoField(tag=2, wire=WireType.MESSAGE, cls=Video)] = None


class Brand(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    icon_url: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class RatingsBreakdown(BaseModel):
    average_rating: Annotated[float, ProtoField(tag=1, wire=WireType.DOUBLE)] = 0.0
    total_reviews: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class Merchant(BaseModel):
    merchant_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    icon_url: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class Price(BaseModel):
    currency_code: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    amount: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class OfferingActionLink(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class OfferingAction(BaseModel):
    link: Annotated[Optional[OfferingActionLink], ProtoField(tag=1, wire=WireType.MESSAGE, cls=OfferingActionLink)] = None


class Offering(BaseModel):
    merchant: Annotated[Optional[Merchant], ProtoField(tag=1, wire=WireType.MESSAGE, cls=Merchant)] = None
    availability: Annotated[ProductAvailability, ProtoField(tag=2, wire=WireType.INT32)] = ProductAvailability.IN_STOCK
    url: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    condition: Annotated[ProductCondition, ProtoField(tag=4, wire=WireType.INT32)] = ProductCondition.NEW
    price: Annotated[Optional[Price], ProtoField(tag=5, wire=WireType.MESSAGE, cls=Price)] = None
    action: Annotated[Optional[OfferingAction], ProtoField(tag=6, wire=WireType.MESSAGE, cls=OfferingAction)] = None


class Product(BaseModel):
    product_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    identifiers: Annotated[List[ProductSource], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=ProductSource)] = Field(default_factory=list)
    title: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    attributes: Annotated[List[ProductAttribute], ProtoField(tag=5, wire=WireType.REPEATED_MESSAGE, cls=ProductAttribute)] = Field(default_factory=list)
    media_items: Annotated[List[MediaItem], ProtoField(tag=6, wire=WireType.REPEATED_MESSAGE, cls=MediaItem)] = Field(default_factory=list)
    brand: Annotated[Optional[Brand], ProtoField(tag=7, wire=WireType.MESSAGE, cls=Brand)] = None
    ratings_breakdown: Annotated[Optional[RatingsBreakdown], ProtoField(tag=8, wire=WireType.MESSAGE, cls=RatingsBreakdown)] = None
    variants: Annotated[List[Product], ProtoField(tag=10, wire=WireType.REPEATED_MESSAGE, cls=Product)] = Field(default_factory=list)
    offerings: Annotated[List[Offering], ProtoField(tag=11, wire=WireType.REPEATED_MESSAGE, cls=Offering)] = Field(default_factory=list)


class SearchProductResult(BaseModel):
    search_product_result_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    product: Annotated[Optional[Product], ProtoField(tag=2, wire=WireType.MESSAGE, cls=Product)] = None


class GlobalRateLimitDetails(BaseModel):
    pass


class ModelNotAvailableDetails(BaseModel):
    pass


class SystemKillSwitchDetails(BaseModel):
    feature_name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class BeyondContextLengthDetails(BaseModel):
    pass


class UserPromptTooLongDetails(BaseModel):
    pass


class AttachmentModeratedDetails(BaseModel):
    pass


class AttachmentImageTooLargeDetails(BaseModel):
    max_size_bytes: Annotated[int, ProtoField(tag=1, wire=WireType.INT64)] = 0
    file_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class AttachmentFileTooLargeDetails(BaseModel):
    file_name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class AttachmentTooManyPagesDetails(BaseModel):
    max_pages: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0


class AttachmentLoadFailedDetails(BaseModel):
    pass


class InternalErrorDetails(BaseModel):
    pass


class RequestCancelledDetails(BaseModel):
    pass


class RenderToolFailedDetails(BaseModel):
    failed_count: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0


class RenderToolRateLimitedDetails(BaseModel):
    rate_limited_count: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0


class ToolCallFailedDetails(BaseModel):
    tool_usage_card_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    tool_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ContentModeratedDetails(BaseModel):
    pass


class UsagePoolExhaustedDetails(BaseModel):
    pass


class UsageLimitReachedDetails(BaseModel):
    pass


class RenderPerMessageLimitExceededDetails(BaseModel):
    dropped_count: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0


class ConcurrencyLimitDetails(BaseModel):
    pass


class StreamError(BaseModel):
    message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    global_rate_limit: Annotated[Optional[GlobalRateLimitDetails], ProtoField(tag=2, wire=WireType.MESSAGE, cls=GlobalRateLimitDetails)] = None
    model_not_available: Annotated[Optional[ModelNotAvailableDetails], ProtoField(tag=3, wire=WireType.MESSAGE, cls=ModelNotAvailableDetails)] = None
    system_kill_switch: Annotated[Optional[SystemKillSwitchDetails], ProtoField(tag=4, wire=WireType.MESSAGE, cls=SystemKillSwitchDetails)] = None
    beyond_context_length: Annotated[Optional[BeyondContextLengthDetails], ProtoField(tag=5, wire=WireType.MESSAGE, cls=BeyondContextLengthDetails)] = None
    user_prompt_too_long: Annotated[Optional[UserPromptTooLongDetails], ProtoField(tag=6, wire=WireType.MESSAGE, cls=UserPromptTooLongDetails)] = None
    attachment_moderated: Annotated[Optional[AttachmentModeratedDetails], ProtoField(tag=7, wire=WireType.MESSAGE, cls=AttachmentModeratedDetails)] = None
    attachment_image_too_large: Annotated[Optional[AttachmentImageTooLargeDetails], ProtoField(tag=8, wire=WireType.MESSAGE, cls=AttachmentImageTooLargeDetails)] = None
    attachment_file_too_large: Annotated[Optional[AttachmentFileTooLargeDetails], ProtoField(tag=9, wire=WireType.MESSAGE, cls=AttachmentFileTooLargeDetails)] = None
    attachment_too_many_pages: Annotated[Optional[AttachmentTooManyPagesDetails], ProtoField(tag=10, wire=WireType.MESSAGE, cls=AttachmentTooManyPagesDetails)] = None
    attachment_load_failed: Annotated[Optional[AttachmentLoadFailedDetails], ProtoField(tag=11, wire=WireType.MESSAGE, cls=AttachmentLoadFailedDetails)] = None
    internal_error: Annotated[Optional[InternalErrorDetails], ProtoField(tag=12, wire=WireType.MESSAGE, cls=InternalErrorDetails)] = None
    request_cancelled: Annotated[Optional[RequestCancelledDetails], ProtoField(tag=13, wire=WireType.MESSAGE, cls=RequestCancelledDetails)] = None
    render_tool_failed: Annotated[Optional[RenderToolFailedDetails], ProtoField(tag=14, wire=WireType.MESSAGE, cls=RenderToolFailedDetails)] = None
    render_tool_rate_limited: Annotated[Optional[RenderToolRateLimitedDetails], ProtoField(tag=15, wire=WireType.MESSAGE, cls=RenderToolRateLimitedDetails)] = None
    tool_call_failed: Annotated[Optional[ToolCallFailedDetails], ProtoField(tag=16, wire=WireType.MESSAGE, cls=ToolCallFailedDetails)] = None
    severity: Annotated[StreamErrorSeverity, ProtoField(tag=17, wire=WireType.INT32)] = StreamErrorSeverity.STREAM_ERROR_SEVERITY_UNKNOWN
    content_moderated: Annotated[Optional[ContentModeratedDetails], ProtoField(tag=18, wire=WireType.MESSAGE, cls=ContentModeratedDetails)] = None
    usage_pool_exhausted: Annotated[Optional[UsagePoolExhaustedDetails], ProtoField(tag=19, wire=WireType.MESSAGE, cls=UsagePoolExhaustedDetails)] = None
    usage_limit_reached: Annotated[Optional[UsageLimitReachedDetails], ProtoField(tag=20, wire=WireType.MESSAGE, cls=UsageLimitReachedDetails)] = None
    render_per_message_limit_exceeded: Annotated[Optional[RenderPerMessageLimitExceededDetails], ProtoField(tag=21, wire=WireType.MESSAGE, cls=RenderPerMessageLimitExceededDetails)] = None
    concurrency_limit: Annotated[Optional[ConcurrencyLimitDetails], ProtoField(tag=22, wire=WireType.MESSAGE, cls=ConcurrencyLimitDetails)] = None


class Response(BaseModel):
    response_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    message: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    sender: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=4, wire=WireType.TIMESTAMP)] = ""
    parent_response_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    manual: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    partial: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False
    shared: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False
    query: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    query_type: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    web_search_results: Annotated[List[WebSearchResult], ProtoField(tag=11, wire=WireType.REPEATED_MESSAGE, cls=WebSearchResult)] = Field(default_factory=list)
    xpost_ids: Annotated[List[str], ProtoField(tag=12, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    xposts: Annotated[List[XPost], ProtoField(tag=13, wire=WireType.REPEATED_MESSAGE, cls=XPost)] = Field(default_factory=list)
    generated_image_urls: Annotated[List[str], ProtoField(tag=14, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    image_attachments: Annotated[List[str], ProtoField(tag=15, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    file_attachments: Annotated[List[str], ProtoField(tag=16, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    card_attachments_json: Annotated[List[str], ProtoField(tag=18, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    file_uris: Annotated[List[str], ProtoField(tag=19, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    file_attachments_metadata: Annotated[List[FileMetadata], ProtoField(tag=20, wire=WireType.REPEATED_MESSAGE, cls=FileMetadata)] = Field(default_factory=list)
    is_control: Annotated[bool, ProtoField(tag=21, wire=WireType.BOOL)] = False
    thinking_trace: Annotated[str, ProtoField(tag=22, wire=WireType.STRING)] = ""
    steps: Annotated[List[ResponseStep], ProtoField(tag=23, wire=WireType.REPEATED_MESSAGE, cls=ResponseStep)] = Field(default_factory=list)
    image_edit_uri: Annotated[str, ProtoField(tag=24, wire=WireType.STRING)] = ""
    error: Annotated[str, ProtoField(tag=25, wire=WireType.STRING)] = ""
    media_types: Annotated[List[str], ProtoField(tag=26, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    webpage_urls: Annotated[List[str], ProtoField(tag=27, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    metadata: Annotated[dict, ProtoField(tag=28, wire=WireType.JSON_STRUCT)] = Field(default_factory=dict)
    image_edit_uris: Annotated[List[str], ProtoField(tag=29, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    generated_image_height: Annotated[int, ProtoField(tag=30, wire=WireType.INT32)] = 0
    generated_image_width: Annotated[int, ProtoField(tag=31, wire=WireType.INT32)] = 0
    ui_layout: Annotated[Optional[UiLayout], ProtoField(tag=32, wire=WireType.MESSAGE, cls=UiLayout)] = None
    thinking_start_time: Annotated[str, ProtoField(tag=33, wire=WireType.TIMESTAMP)] = ""
    thinking_end_time: Annotated[str, ProtoField(tag=34, wire=WireType.TIMESTAMP)] = ""
    cited_web_search_results: Annotated[List[WebSearchResult], ProtoField(tag=35, wire=WireType.REPEATED_MESSAGE, cls=WebSearchResult)] = Field(default_factory=list)
    selected_file_text_content: Annotated[str, ProtoField(tag=36, wire=WireType.STRING)] = ""
    selected_file_text_content_start_position: Annotated[int, ProtoField(tag=37, wire=WireType.INT32)] = 0
    selected_file_text_content_end_position: Annotated[int, ProtoField(tag=38, wire=WireType.INT32)] = 0
    tool_responses: Annotated[List[dict], ProtoField(tag=39, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    thread_parent_id: Annotated[str, ProtoField(tag=40, wire=WireType.STRING)] = ""
    parent_quoted_text: Annotated[str, ProtoField(tag=41, wire=WireType.STRING)] = ""
    model: Annotated[str, ProtoField(tag=42, wire=WireType.STRING)] = ""
    side_by_side_config: Annotated[Optional[SideBySideConfig], ProtoField(tag=43, wire=WireType.MESSAGE, cls=SideBySideConfig)] = None
    fast_tool_response: Annotated[Optional[FastToolResponse], ProtoField(tag=44, wire=WireType.MESSAGE, cls=FastToolResponse)] = None
    request_metadata: Annotated[Optional[RequestMetadata], ProtoField(tag=45, wire=WireType.MESSAGE, cls=RequestMetadata)] = None
    rag_results: Annotated[List[RagResult], ProtoField(tag=46, wire=WireType.REPEATED_MESSAGE, cls=RagResult)] = Field(default_factory=list)
    cited_rag_results: Annotated[List[RagResult], ProtoField(tag=47, wire=WireType.REPEATED_MESSAGE, cls=RagResult)] = Field(default_factory=list)
    search_product_results: Annotated[List[SearchProductResult], ProtoField(tag=48, wire=WireType.REPEATED_MESSAGE, cls=SearchProductResult)] = Field(default_factory=list)
    connector_search_results: Annotated[List[ConnectorSearchResultItem], ProtoField(tag=49, wire=WireType.REPEATED_MESSAGE, cls=ConnectorSearchResultItem)] = Field(default_factory=list)
    collection_search_results: Annotated[List[CollectionSearchResultItem], ProtoField(tag=50, wire=WireType.REPEATED_MESSAGE, cls=CollectionSearchResultItem)] = Field(default_factory=list)
    stream_errors: Annotated[List[StreamError], ProtoField(tag=52, wire=WireType.REPEATED_MESSAGE, cls=StreamError)] = Field(default_factory=list)


class QueryAction(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    type_f: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ImageGenerationResponse(BaseModel):
    generated_image_bytes: Annotated[bytes, ProtoField(tag=1, wire=WireType.BYTES_FIELD)] = b""
    content_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class CachedImageGenerationResponse(BaseModel):
    image_url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    moderated: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class GrokInXaiRequest(BaseModel):
    request_json: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class StreamingImageGenerationResponse(BaseModel):
    image_url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    seq: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    progress: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    moderated: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    image_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    image_index: Annotated[int, ProtoField(tag=6, wire=WireType.INT32)] = 0
    asset_id: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    image_model: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    r_rated: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = False
    side_by_side_index: Annotated[int, ProtoField(tag=10, wire=WireType.INT32)] = 0
    has_watermark: Annotated[bool, ProtoField(tag=11, wire=WireType.BOOL)] = False
    is_root_user_uploaded: Annotated[bool, ProtoField(tag=13, wire=WireType.BOOL)] = False
    rejection_reason: Annotated[MediaRejectionReason, ProtoField(tag=14, wire=WireType.INT32)] = MediaRejectionReason.MEDIA_REJECTION_REASON_UNSPECIFIED


class CardAttachment(BaseModel):
    json_data: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class FeedbackLabel(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    label_en: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    icon: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class FinalMetadata(BaseModel):
    follow_up_suggestions: Annotated[List[FollowUpSuggestion], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=FollowUpSuggestion)] = Field(default_factory=list)
    feedback_labels: Annotated[List[FeedbackLabel], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=FeedbackLabel)] = Field(default_factory=list)
    tools_used: Annotated[Optional[ToolOverrides], ProtoField(tag=3, wire=WireType.MESSAGE, cls=ToolOverrides)] = None
    disclaimer: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class ImageAttachmentInfo(BaseModel):
    image_attachment_count: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0


class BannerMessage(BaseModel):
    message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class Disclaimer(BaseModel):
    message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class MemoryReference(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    summary: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class MemoryReferences(BaseModel):
    references: Annotated[List[MemoryReference], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=MemoryReference)] = Field(default_factory=list)


class ImageDimensions(BaseModel):
    width: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    height: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class FollowUpSuggestedMode(BaseModel):
    mode: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    web: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    mobile: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class StreamingMetadata(BaseModel):
    stream_key: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    msg_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class AuthNotification(BaseModel):
    providers: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class ToolDefinition(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    args: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class StreamingVideoGenerationResponse(BaseModel):
    video_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    progress: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
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
    video_streaming_duration: Annotated[float, ProtoField(tag=20, wire=WireType.FLOAT)] = 0.0
    resolution_name: Annotated[str, ProtoField(tag=21, wire=WireType.STRING)] = ""
    has_watermark: Annotated[bool, ProtoField(tag=22, wire=WireType.BOOL)] = False
    is_root_user_uploaded: Annotated[bool, ProtoField(tag=24, wire=WireType.BOOL)] = False
    rejection_reason: Annotated[MediaRejectionReason, ProtoField(tag=25, wire=WireType.INT32)] = MediaRejectionReason.MEDIA_REJECTION_REASON_UNSPECIFIED


class StreamingAudioGenerationResponse(BaseModel):
    video_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    audio_urls: Annotated[List[str], ProtoField(tag=2, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class EffortDecision(BaseModel):
    effort: Annotated[EffortDecisionEffort, ProtoField(tag=1, wire=WireType.INT32)] = EffortDecisionEffort.UNSPECIFIED
    steer_model_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class LlmInfo(BaseModel):
    model_hash: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class TextBox(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    placeholder: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    size: Annotated[TextBoxSize, ProtoField(tag=3, wire=WireType.INT32)] = TextBoxSize.TEXT_BOX_SIZE_UNSPECIFIED


class SurveyValue(BaseModel):
    value_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    label: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class Likert(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    labels: Annotated[List[str], ProtoField(tag=2, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    values: Annotated[List[SurveyValue], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=SurveyValue)] = Field(default_factory=list)


class Thumbs(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    labels: Annotated[List[str], ProtoField(tag=2, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    values: Annotated[List[SurveyValue], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=SurveyValue)] = Field(default_factory=list)


class SurveyElement(BaseModel):
    text_box: Annotated[Optional[TextBox], ProtoField(tag=1, wire=WireType.MESSAGE, cls=TextBox)] = None
    likert: Annotated[Optional[Likert], ProtoField(tag=2, wire=WireType.MESSAGE, cls=Likert)] = None
    thumbs: Annotated[Optional[Thumbs], ProtoField(tag=3, wire=WireType.MESSAGE, cls=Thumbs)] = None


class Survey(BaseModel):
    survey_title: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    statsig_survey_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    elements: Annotated[List[SurveyElement], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=SurveyElement)] = Field(default_factory=list)


class SearchProductResults(BaseModel):
    results: Annotated[List[SearchProductResult], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=SearchProductResult)] = Field(default_factory=list)


class GenerateTitleResponse(BaseModel):
    new_title: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class BreakAssetText(BaseModel):
    text: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class BreakAssetImage(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    width: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    height: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0


class BreakAssetVideo(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    length_ms: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    width: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    height: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0


class BreakAsset(BaseModel):
    text: Annotated[Optional[BreakAssetText], ProtoField(tag=1, wire=WireType.MESSAGE, cls=BreakAssetText)] = None
    image: Annotated[Optional[BreakAssetImage], ProtoField(tag=2, wire=WireType.MESSAGE, cls=BreakAssetImage)] = None
    video: Annotated[Optional[BreakAssetVideo], ProtoField(tag=3, wire=WireType.MESSAGE, cls=BreakAssetVideo)] = None


class BreakV1(BaseModel):
    delay_ms: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    headline: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    sub_headline: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    cta_text: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    cta_url: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    assets: Annotated[List[BreakAsset], ProtoField(tag=6, wire=WireType.REPEATED_MESSAGE, cls=BreakAsset)] = Field(default_factory=list)
    countdown_style: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""


class Throttle(BaseModel):
    content_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    break_v1: Annotated[Optional[BreakV1], ProtoField(tag=2, wire=WireType.MESSAGE, cls=BreakV1)] = None


class KeepAlive(BaseModel):
    pass


class AddResponseResponse(BaseModel):
    user_response: Annotated[Optional[Response], ProtoField(tag=1, wire=WireType.MESSAGE, cls=Response)] = None
    token: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    model_response: Annotated[Optional[Response], ProtoField(tag=3, wire=WireType.MESSAGE, cls=Response)] = None
    query_action: Annotated[Optional[QueryAction], ProtoField(tag=4, wire=WireType.MESSAGE, cls=QueryAction)] = None
    image_generation_response: Annotated[Optional[ImageGenerationResponse], ProtoField(tag=5, wire=WireType.MESSAGE, cls=ImageGenerationResponse)] = None
    x_search_results: Annotated[Optional[XSearchResults], ProtoField(tag=6, wire=WireType.MESSAGE, cls=XSearchResults)] = None
    cached_image_generation_response: Annotated[Optional[CachedImageGenerationResponse], ProtoField(tag=7, wire=WireType.MESSAGE, cls=CachedImageGenerationResponse)] = None
    web_search_results: Annotated[Optional[WebSearchResults], ProtoField(tag=8, wire=WireType.MESSAGE, cls=WebSearchResults)] = None
    grok_in_xai_request: Annotated[Optional[GrokInXaiRequest], ProtoField(tag=10, wire=WireType.MESSAGE, cls=GrokInXaiRequest)] = None
    follow_up_suggestions: Annotated[Optional[FollowUpSuggestions], ProtoField(tag=11, wire=WireType.MESSAGE, cls=FollowUpSuggestions)] = None
    streaming_image_generation_response: Annotated[Optional[StreamingImageGenerationResponse], ProtoField(tag=12, wire=WireType.MESSAGE, cls=StreamingImageGenerationResponse)] = None
    card_attachment: Annotated[Optional[CardAttachment], ProtoField(tag=13, wire=WireType.MESSAGE, cls=CardAttachment)] = None
    side_by_side_index: Annotated[int, ProtoField(tag=14, wire=WireType.INT32)] = 0
    final_metadata: Annotated[Optional[FinalMetadata], ProtoField(tag=15, wire=WireType.MESSAGE, cls=FinalMetadata)] = None
    is_thinking: Annotated[bool, ProtoField(tag=16, wire=WireType.BOOL)] = False
    is_soft_stop: Annotated[bool, ProtoField(tag=17, wire=WireType.BOOL)] = False
    message_tag: Annotated[str, ProtoField(tag=18, wire=WireType.STRING)] = ""
    message_step_id: Annotated[int, ProtoField(tag=19, wire=WireType.INT32)] = 0
    response_id: Annotated[str, ProtoField(tag=20, wire=WireType.STRING)] = ""
    image_attachment_info: Annotated[Optional[ImageAttachmentInfo], ProtoField(tag=21, wire=WireType.MESSAGE, cls=ImageAttachmentInfo)] = None
    banner_message: Annotated[Optional[BannerMessage], ProtoField(tag=22, wire=WireType.MESSAGE, cls=BannerMessage)] = None
    disclaimer: Annotated[Optional[Disclaimer], ProtoField(tag=23, wire=WireType.MESSAGE, cls=Disclaimer)] = None
    progress_report: Annotated[Optional[ProgressReport], ProtoField(tag=24, wire=WireType.MESSAGE, cls=ProgressReport)] = None
    memory_references: Annotated[Optional[MemoryReferences], ProtoField(tag=25, wire=WireType.MESSAGE, cls=MemoryReferences)] = None
    image_dimensions: Annotated[Optional[ImageDimensions], ProtoField(tag=26, wire=WireType.MESSAGE, cls=ImageDimensions)] = None
    follow_up_suggested_mode: Annotated[Optional[FollowUpSuggestedMode], ProtoField(tag=27, wire=WireType.MESSAGE, cls=FollowUpSuggestedMode)] = None
    ui_layout: Annotated[Optional[UiLayout], ProtoField(tag=28, wire=WireType.MESSAGE, cls=UiLayout)] = None
    streaming_metadata: Annotated[Optional[StreamingMetadata], ProtoField(tag=29, wire=WireType.MESSAGE, cls=StreamingMetadata)] = None
    auth_notification: Annotated[Optional[AuthNotification], ProtoField(tag=30, wire=WireType.MESSAGE, cls=AuthNotification)] = None
    cited_web_search_results: Annotated[Optional[WebSearchResults], ProtoField(tag=31, wire=WireType.MESSAGE, cls=WebSearchResults)] = None
    tool_request: Annotated[Optional[ToolDefinition], ProtoField(tag=32, wire=WireType.MESSAGE, cls=ToolDefinition)] = None
    tool_usage_card_id: Annotated[str, ProtoField(tag=33, wire=WireType.STRING)] = ""
    streaming_video_generation_response: Annotated[Optional[StreamingVideoGenerationResponse], ProtoField(tag=34, wire=WireType.MESSAGE, cls=StreamingVideoGenerationResponse)] = None
    rollout_id: Annotated[str, ProtoField(tag=35, wire=WireType.STRING)] = ""
    side_by_side_config: Annotated[Optional[SideBySideConfig], ProtoField(tag=36, wire=WireType.MESSAGE, cls=SideBySideConfig)] = None
    streaming_audio_generation_response: Annotated[Optional[StreamingAudioGenerationResponse], ProtoField(tag=37, wire=WireType.MESSAGE, cls=StreamingAudioGenerationResponse)] = None
    effort_decision: Annotated[Optional[EffortDecision], ProtoField(tag=38, wire=WireType.MESSAGE, cls=EffortDecision)] = None
    llm_info: Annotated[Optional[LlmInfo], ProtoField(tag=39, wire=WireType.MESSAGE, cls=LlmInfo)] = None
    fast_tool_response: Annotated[Optional[FastToolResponse], ProtoField(tag=40, wire=WireType.MESSAGE, cls=FastToolResponse)] = None
    survey: Annotated[Optional[Survey], ProtoField(tag=41, wire=WireType.MESSAGE, cls=Survey)] = None
    rag_results: Annotated[Optional[RagResults], ProtoField(tag=42, wire=WireType.MESSAGE, cls=RagResults)] = None
    cited_rag_results: Annotated[Optional[RagResults], ProtoField(tag=43, wire=WireType.MESSAGE, cls=RagResults)] = None
    search_product_results: Annotated[Optional[SearchProductResults], ProtoField(tag=44, wire=WireType.MESSAGE, cls=SearchProductResults)] = None
    connector_search_results: Annotated[Optional[ConnectorSearchResults], ProtoField(tag=45, wire=WireType.MESSAGE, cls=ConnectorSearchResults)] = None
    collection_search_results: Annotated[Optional[CollectionSearchResults], ProtoField(tag=46, wire=WireType.MESSAGE, cls=CollectionSearchResults)] = None
    memory_v2_update_result: Annotated[Optional[MemoryV2UpdateResult], ProtoField(tag=47, wire=WireType.MESSAGE, cls=MemoryV2UpdateResult)] = None
    code_execution_result: Annotated[Optional[CodeExecutionResult], ProtoField(tag=48, wire=WireType.MESSAGE, cls=CodeExecutionResult)] = None
    error: Annotated[Optional[StreamError], ProtoField(tag=49, wire=WireType.MESSAGE, cls=StreamError)] = None
    tool_usage_card: Annotated[Optional[ToolUsageCard], ProtoField(tag=50, wire=WireType.MESSAGE, cls=ToolUsageCard)] = None
    generated_title: Annotated[Optional[GenerateTitleResponse], ProtoField(tag=53, wire=WireType.MESSAGE, cls=GenerateTitleResponse)] = None
    throttle: Annotated[Optional[Throttle], ProtoField(tag=54, wire=WireType.MESSAGE, cls=Throttle)] = None
    keep_alive: Annotated[Optional[KeepAlive], ProtoField(tag=55, wire=WireType.MESSAGE, cls=KeepAlive)] = None


class AddToGroupRequest(BaseModel):
    group_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    node_ids: Annotated[List[str], ProtoField(tag=2, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class AddToGroupResponse(BaseModel):
    pass


class AddToolResponseRequest(BaseModel):
    response_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    tool_response: Annotated[dict, ProtoField(tag=2, wire=WireType.JSON_STRUCT)] = Field(default_factory=dict)


class AddUserResponseRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    message: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    parent_response_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class AgentCustomization(BaseModel):
    agent_id: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    instructions: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class AgentCustomizations(BaseModel):
    values: Annotated[List[AgentCustomization], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=AgentCustomization)] = Field(default_factory=list)


class AlignAudioRequest(BaseModel):
    transcript: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    format_f: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    audio_b64: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    alignment_provider: Annotated[AlignmentProvider, ProtoField(tag=4, wire=WireType.INT32)] = AlignmentProvider.ALIGNMENT_PROVIDER_UNSPECIFIED
    lang_code: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class WordScore(BaseModel):
    word: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    align_score: Annotated[float, ProtoField(tag=2, wire=WireType.FLOAT)] = 0.0
    start_ms: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    end_ms: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0


class AlignAudioResponse(BaseModel):
    words: Annotated[List[WordScore], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=WordScore)] = Field(default_factory=list)
    score: Annotated[float, ProtoField(tag=2, wire=WireType.FLOAT)] = 0.0
    num_samples: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    transcript: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    inf_time: Annotated[float, ProtoField(tag=5, wire=WireType.FLOAT)] = 0.0
    alignment_score: Annotated[float, ProtoField(tag=6, wire=WireType.FLOAT)] = 0.0


class AndroidKeyAttest(BaseModel):
    cert_chain_der: Annotated[List[bytes], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class ArticleItem(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    text: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class AskToShareConversationRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class AudioChunk(BaseModel):
    data__f: Annotated[bytes, ProtoField(tag=1, wire=WireType.BYTES_FIELD)] = b""
    content_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class AudioSegment(BaseModel):
    data_base64: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    sample_rate: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class BulkAddPostsToFolderRequest(BaseModel):
    post_ids: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    folder_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class BulkAddPostsToFolderResponse(BaseModel):
    added_count: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0


class BulkGetCanvasNodesRequest(BaseModel):
    canvas_ids: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class CanvasNodePosition(BaseModel):
    x: Annotated[float, ProtoField(tag=1, wire=WireType.DOUBLE)] = 0.0
    y: Annotated[float, ProtoField(tag=2, wire=WireType.DOUBLE)] = 0.0


class CanvasPostData(BaseModel):
    post_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class CanvasTextData(BaseModel):
    text_content: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    font_size: Annotated[float, ProtoField(tag=2, wire=WireType.DOUBLE)] = 0.0
    text_block_width: Annotated[float, ProtoField(tag=3, wire=WireType.DOUBLE)] = 0.0


class CanvasStitchTrack(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    post_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    duration: Annotated[float, ProtoField(tag=3, wire=WireType.DOUBLE)] = 0.0
    offset: Annotated[float, ProtoField(tag=4, wire=WireType.DOUBLE)] = 0.0
    metadata: Annotated[dict, ProtoField(tag=5, wire=WireType.JSON_STRUCT)] = Field(default_factory=dict)


class CanvasStitchData(BaseModel):
    tracks: Annotated[List[CanvasStitchTrack], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=CanvasStitchTrack)] = Field(default_factory=list)
    aspect_ratio: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class CanvasGroupData(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    columns: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    layout: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    image_gen_speed: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class CanvasBoardData(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    columns: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    layout: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class CanvasInputAsset(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    url: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class CaptionedVideoVariant(BaseModel):
    preset: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    media_url: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    source_resolution: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class MediaPostCaptions(BaseModel):
    baked: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    preset: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    variants: Annotated[List[CaptionedVideoVariant], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=CaptionedVideoVariant)] = Field(default_factory=list)


class CanvasAssetData(BaseModel):
    width: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    height: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    moderated: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    r_rated: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    key: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    image_edit_is_root_user_uploaded: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    mime_type: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    input_assets: Annotated[List[CanvasInputAsset], ProtoField(tag=8, wire=WireType.REPEATED_MESSAGE, cls=CanvasInputAsset)] = Field(default_factory=list)
    preview_image_key: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    duration: Annotated[float, ProtoField(tag=11, wire=WireType.FLOAT)] = 0.0
    resolution_name: Annotated[str, ProtoField(tag=12, wire=WireType.STRING)] = ""
    hd_media_url: Annotated[str, ProtoField(tag=13, wire=WireType.STRING)] = ""
    hd_1080_media_url: Annotated[str, ProtoField(tag=14, wire=WireType.STRING)] = ""
    asset_id: Annotated[str, ProtoField(tag=15, wire=WireType.STRING)] = ""
    generation_type: Annotated[str, ProtoField(tag=16, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=17, wire=WireType.TIMESTAMP)] = ""
    prompt: Annotated[str, ProtoField(tag=18, wire=WireType.STRING)] = ""
    media_url: Annotated[str, ProtoField(tag=19, wire=WireType.STRING)] = ""
    thumbhash: Annotated[str, ProtoField(tag=20, wire=WireType.STRING)] = ""
    has_watermark: Annotated[bool, ProtoField(tag=21, wire=WireType.BOOL)] = False
    is_root_user_uploaded: Annotated[bool, ProtoField(tag=22, wire=WireType.BOOL)] = False
    video_extension_start_time: Annotated[float, ProtoField(tag=23, wire=WireType.DOUBLE)] = 0.0
    captions: Annotated[Optional[MediaPostCaptions], ProtoField(tag=24, wire=WireType.MESSAGE, cls=MediaPostCaptions)] = None


class CanvasDrawableData(BaseModel):
    pass


class CanvasNode(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    position: Annotated[Optional[CanvasNodePosition], ProtoField(tag=7, wire=WireType.MESSAGE, cls=CanvasNodePosition)] = None
    scale: Annotated[float, ProtoField(tag=22, wire=WireType.DOUBLE)] = 0.0
    parent_node_id: Annotated[str, ProtoField(tag=23, wire=WireType.STRING)] = ""
    prompt: Annotated[str, ProtoField(tag=24, wire=WireType.STRING)] = ""
    metadata: Annotated[dict, ProtoField(tag=25, wire=WireType.JSON_STRUCT)] = Field(default_factory=dict)
    post: Annotated[Optional[CanvasPostData], ProtoField(tag=30, wire=WireType.MESSAGE, cls=CanvasPostData)] = None
    text: Annotated[Optional[CanvasTextData], ProtoField(tag=31, wire=WireType.MESSAGE, cls=CanvasTextData)] = None
    stitch: Annotated[Optional[CanvasStitchData], ProtoField(tag=33, wire=WireType.MESSAGE, cls=CanvasStitchData)] = None
    group: Annotated[Optional[CanvasGroupData], ProtoField(tag=34, wire=WireType.MESSAGE, cls=CanvasGroupData)] = None
    board: Annotated[Optional[CanvasBoardData], ProtoField(tag=35, wire=WireType.MESSAGE, cls=CanvasBoardData)] = None
    asset: Annotated[Optional[CanvasAssetData], ProtoField(tag=36, wire=WireType.MESSAGE, cls=CanvasAssetData)] = None
    drawable: Annotated[Optional[CanvasDrawableData], ProtoField(tag=37, wire=WireType.MESSAGE, cls=CanvasDrawableData)] = None


class CanvasNodeList(BaseModel):
    canvas_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    nodes: Annotated[List[CanvasNode], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=CanvasNode)] = Field(default_factory=list)


class BulkGetCanvasNodesResponse(BaseModel):
    canvases: Annotated[List[CanvasNodeList], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=CanvasNodeList)] = Field(default_factory=list)


class BulkGetMediaPostsRequest(BaseModel):
    ids: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class UserInteractionStatus(BaseModel):
    like_status: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False


class InputMediaItem(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    mime_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    media_url: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    resolution: Annotated[Optional[Resolution], ProtoField(tag=4, wire=WireType.MESSAGE, cls=Resolution)] = None
    moderated: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False
    r_rated: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False


class MediaPostTemplate(BaseModel):
    inputs: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    output_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    id_f: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    version: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0


class MediaPost(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    user_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=3, wire=WireType.TIMESTAMP)] = ""
    prompt: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    media_type: Annotated[MediaPostType, ProtoField(tag=5, wire=WireType.INT32)] = MediaPostType.MEDIA_POST_TYPE_INVALID
    media_url: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    mime_type: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    original_post_id: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    audio_urls: Annotated[List[str], ProtoField(tag=9, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    original_post: Annotated[Optional[MediaPost], ProtoField(tag=10, wire=WireType.MESSAGE, cls=MediaPost)] = None
    conversation_id: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    child_posts: Annotated[List[MediaPost], ProtoField(tag=12, wire=WireType.REPEATED_MESSAGE, cls=MediaPost)] = Field(default_factory=list)
    original_prompt: Annotated[str, ProtoField(tag=13, wire=WireType.STRING)] = ""
    mode: Annotated[str, ProtoField(tag=14, wire=WireType.STRING)] = ""
    user_interaction_status: Annotated[Optional[UserInteractionStatus], ProtoField(tag=15, wire=WireType.MESSAGE, cls=UserInteractionStatus)] = None
    resolution: Annotated[Optional[Resolution], ProtoField(tag=16, wire=WireType.MESSAGE, cls=Resolution)] = None
    model_name: Annotated[str, ProtoField(tag=17, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=18, wire=WireType.STRING)] = ""
    hd_media_url: Annotated[str, ProtoField(tag=19, wire=WireType.STRING)] = ""
    thumbnail_image_url: Annotated[str, ProtoField(tag=20, wire=WireType.STRING)] = ""
    original_ref_type: Annotated[OriginalRefType, ProtoField(tag=21, wire=WireType.INT32)] = OriginalRefType.ORIGINAL_REF_TYPE_INVALID
    platform: Annotated[MediaPostPlatform, ProtoField(tag=22, wire=WireType.INT32)] = MediaPostPlatform.MEDIA_POST_PLATFORM_INVALID
    media_status: Annotated[MediaPostMediaStatus, ProtoField(tag=23, wire=WireType.INT32)] = MediaPostMediaStatus.MEDIA_POST_MEDIA_STATUS_INVALID
    last_frame_thumbnail_image_url: Annotated[str, ProtoField(tag=24, wire=WireType.STRING)] = ""
    watermarked_media_url: Annotated[str, ProtoField(tag=25, wire=WireType.STRING)] = ""
    video_extension_start_time: Annotated[float, ProtoField(tag=26, wire=WireType.DOUBLE)] = 0.0
    available_actions: Annotated[List[MediaPostActionType], ProtoField(tag=27, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    video_duration: Annotated[float, ProtoField(tag=28, wire=WireType.FLOAT)] = 0.0
    moderated: Annotated[bool, ProtoField(tag=29, wire=WireType.BOOL)] = False
    images: Annotated[List[MediaPost], ProtoField(tag=30, wire=WireType.REPEATED_MESSAGE, cls=MediaPost)] = Field(default_factory=list)
    videos: Annotated[List[MediaPost], ProtoField(tag=31, wire=WireType.REPEATED_MESSAGE, cls=MediaPost)] = Field(default_factory=list)
    r_rated: Annotated[bool, ProtoField(tag=32, wire=WireType.BOOL)] = False
    is_hidden_for_client: Annotated[bool, ProtoField(tag=33, wire=WireType.BOOL)] = False
    resolution_name: Annotated[str, ProtoField(tag=34, wire=WireType.STRING)] = ""
    input_media_items: Annotated[List[InputMediaItem], ProtoField(tag=35, wire=WireType.REPEATED_MESSAGE, cls=InputMediaItem)] = Field(default_factory=list)
    has_watermark: Annotated[bool, ProtoField(tag=36, wire=WireType.BOOL)] = False
    template: Annotated[Optional[MediaPostTemplate], ProtoField(tag=37, wire=WireType.MESSAGE, cls=MediaPostTemplate)] = None
    remix_image_reference: Annotated[str, ProtoField(tag=38, wire=WireType.STRING)] = ""
    hd_1080_media_url: Annotated[str, ProtoField(tag=39, wire=WireType.STRING)] = ""
    is_root_user_uploaded: Annotated[bool, ProtoField(tag=40, wire=WireType.BOOL)] = False
    is_v2: Annotated[bool, ProtoField(tag=42, wire=WireType.BOOL)] = False
    canvas_id: Annotated[str, ProtoField(tag=43, wire=WireType.STRING)] = ""
    captions: Annotated[Optional[MediaPostCaptions], ProtoField(tag=44, wire=WireType.MESSAGE, cls=MediaPostCaptions)] = None


class BulkGetMediaPostsResponse(BaseModel):
    posts: Annotated[List[MediaPost], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=MediaPost)] = Field(default_factory=list)


class BulkRemovePostsFromFolderRequest(BaseModel):
    post_ids: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    folder_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class BulkRemovePostsFromFolderResponse(BaseModel):
    removed_count: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0


class BulkUnlikeMediaPostsRequest(BaseModel):
    post_ids: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class BulkUnlikeMediaPostsResponse(BaseModel):
    removed_count: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0


class CancelPipelineRequest(BaseModel):
    post_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class CancelPipelineResponse(BaseModel):
    pass


class CanvasDocument(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    user_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    sort_order: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    created_at: Annotated[str, ProtoField(tag=5, wire=WireType.TIMESTAMP)] = ""
    updated_at: Annotated[str, ProtoField(tag=6, wire=WireType.TIMESTAMP)] = ""
    metadata: Annotated[dict, ProtoField(tag=7, wire=WireType.JSON_STRUCT)] = Field(default_factory=dict)


class CaptionVideoRequest(BaseModel):
    video_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    container_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    preset: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    style: Annotated[dict, ProtoField(tag=4, wire=WireType.JSON_STRUCT)] = Field(default_factory=dict)
    canvas_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class CaptionVideoResponse(BaseModel):
    post_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    status: Annotated[MediaPostMediaStatus, ProtoField(tag=2, wire=WireType.INT32)] = MediaPostMediaStatus.MEDIA_POST_MEDIA_STATUS_INVALID
    progress_pct: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    message: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    post: Annotated[Optional[MediaPost], ProtoField(tag=5, wire=WireType.MESSAGE, cls=MediaPost)] = None
    error_message: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    canvas_node: Annotated[Optional[CanvasNode], ProtoField(tag=7, wire=WireType.MESSAGE, cls=CanvasNode)] = None


class ChatMessageItem(BaseModel):
    role: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    content: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ChooseSbsResponseRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    response_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class CloneConversationRequest(BaseModel):
    share_link_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class Workspace(BaseModel):
    workspace_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=3, wire=WireType.TIMESTAMP)] = ""
    last_use_time: Annotated[str, ProtoField(tag=4, wire=WireType.TIMESTAMP)] = ""
    icon: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    custom_personality: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    is_public: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False
    is_readonly: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False


class Task(BaseModel):
    task_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    user_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    prompt: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    metadata_json_string: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    is_active: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    notification_method: Annotated[NotificationUiOption, ProtoField(tag=7, wire=WireType.INT32)] = NotificationUiOption.DEFAULT
    model_mode: Annotated[ModelMode, ProtoField(tag=8, wire=WireType.INT32)] = ModelMode.BASE
    notification_decider_enable: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = False
    notification_decider_guideline: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    model_name: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    toolset: Annotated[List[str], ProtoField(tag=12, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    team_id: Annotated[str, ProtoField(tag=13, wire=WireType.STRING)] = ""


class TaskSchedule(BaseModel):
    schedule_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    task_cadence: Annotated[TaskCadence, ProtoField(tag=3, wire=WireType.INT32)] = TaskCadence.TASK_CADENCE_ONCE
    is_enabled: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    next_run: Annotated[bytes, ProtoField(tag=5, wire=WireType.BYTES_FIELD)] = b""
    day_of_week: Annotated[int, ProtoField(tag=6, wire=WireType.INT32)] = 0
    day_of_month: Annotated[int, ProtoField(tag=7, wire=WireType.INT32)] = 0
    day_of_year: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    time_of_day: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    timezone: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    is_completed: Annotated[bool, ProtoField(tag=11, wire=WireType.BOOL)] = False
    end_date: Annotated[bytes, ProtoField(tag=12, wire=WireType.BYTES_FIELD)] = b""


class TaskWithSchedule(BaseModel):
    task: Annotated[Optional[Task], ProtoField(tag=1, wire=WireType.MESSAGE, cls=Task)] = None
    schedules: Annotated[List[TaskSchedule], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=TaskSchedule)] = Field(default_factory=list)


class TaskResult(BaseModel):
    task_result_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    status: Annotated[TaskResultStatus, ProtoField(tag=4, wire=WireType.INT32)] = TaskResultStatus.TASK_RESULT_PENDING
    error: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=7, wire=WireType.TIMESTAMP)] = ""
    update_time: Annotated[str, ProtoField(tag=8, wire=WireType.TIMESTAMP)] = ""
    is_read: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = False
    exec_time: Annotated[int, ProtoField(tag=10, wire=WireType.INT32)] = 0
    schedule_id: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    notification_decision: Annotated[TaskNotificationDecision, ProtoField(tag=12, wire=WireType.INT32)] = TaskNotificationDecision.DISABLED
    task_id: Annotated[str, ProtoField(tag=13, wire=WireType.STRING)] = ""


class OptionalTaskWithSchedule(BaseModel):
    task: Annotated[Optional[TaskWithSchedule], ProtoField(tag=1, wire=WireType.MESSAGE, cls=TaskWithSchedule)] = None
    result: Annotated[Optional[TaskResult], ProtoField(tag=2, wire=WireType.MESSAGE, cls=TaskResult)] = None


class Conversation(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=3, wire=WireType.TIMESTAMP)] = ""
    modify_time: Annotated[str, ProtoField(tag=4, wire=WireType.TIMESTAMP)] = ""
    starred: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    system_prompt_name: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    temporary: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False
    media_types: Annotated[List[str], ProtoField(tag=10, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    workspaces: Annotated[List[Workspace], ProtoField(tag=11, wire=WireType.REPEATED_MESSAGE, cls=Workspace)] = Field(default_factory=list)
    task_result: Annotated[Optional[OptionalTaskWithSchedule], ProtoField(tag=12, wire=WireType.MESSAGE, cls=OptionalTaskWithSchedule)] = None
    team_id: Annotated[str, ProtoField(tag=13, wire=WireType.STRING)] = ""
    x_user_id: Annotated[str, ProtoField(tag=14, wire=WireType.STRING)] = ""
    template_id: Annotated[str, ProtoField(tag=15, wire=WireType.STRING)] = ""
    voice_chat_asset_url: Annotated[str, ProtoField(tag=16, wire=WireType.STRING)] = ""
    voice_chat_alignment_info: Annotated[str, ProtoField(tag=17, wire=WireType.STRING)] = ""
    voice_chat_session_metadata: Annotated[str, ProtoField(tag=18, wire=WireType.STRING)] = ""


class CloneConversationResponse(BaseModel):
    conversation: Annotated[Optional[Conversation], ProtoField(tag=1, wire=WireType.MESSAGE, cls=Conversation)] = None
    responses: Annotated[List[Response], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=Response)] = Field(default_factory=list)


class CompanionConversation(BaseModel):
    companion_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    started_at: Annotated[int, ProtoField(tag=3, wire=WireType.INT64)] = 0
    updated_at: Annotated[int, ProtoField(tag=4, wire=WireType.INT64)] = 0


class CompletedPartInfo(BaseModel):
    part_number: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    etag: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ConversationHistorySummary(BaseModel):
    title: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    timestamp_ms: Annotated[int, ProtoField(tag=2, wire=WireType.INT64)] = 0


class CreateCanvasDocumentRequest(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    metadata: Annotated[dict, ProtoField(tag=2, wire=WireType.JSON_STRUCT)] = Field(default_factory=dict)
    post_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    lineage_post_ids: Annotated[List[str], ProtoField(tag=4, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class CreateCanvasDocumentResponse(BaseModel):
    document: Annotated[Optional[CanvasDocument], ProtoField(tag=1, wire=WireType.MESSAGE, cls=CanvasDocument)] = None
    nodes: Annotated[List[CanvasNode], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=CanvasNode)] = Field(default_factory=list)


class CreateCanvasNodeRequest(BaseModel):
    canvas_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    node: Annotated[Optional[CanvasNode], ProtoField(tag=2, wire=WireType.MESSAGE, cls=CanvasNode)] = None


class CreateCanvasNodeResponse(BaseModel):
    node: Annotated[Optional[CanvasNode], ProtoField(tag=1, wire=WireType.MESSAGE, cls=CanvasNode)] = None


class CreateConversationAndRespondRequest(BaseModel):
    system_prompt_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    temporary: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    model_name: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    message: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    file_attachments: Annotated[List[str], ProtoField(tag=6, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    image_attachments: Annotated[List[str], ProtoField(tag=7, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    disable_search: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False
    enable_image_generation: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = False
    return_image_bytes: Annotated[bool, ProtoField(tag=10, wire=WireType.BOOL)] = False
    return_raw_grok_in_xai_request: Annotated[bool, ProtoField(tag=11, wire=WireType.BOOL)] = False
    enable_image_streaming: Annotated[bool, ProtoField(tag=12, wire=WireType.BOOL)] = False
    image_generation_count: Annotated[int, ProtoField(tag=13, wire=WireType.INT32)] = 0
    force_concise: Annotated[bool, ProtoField(tag=14, wire=WireType.BOOL)] = False
    tool_overrides: Annotated[Optional[ToolOverrides], ProtoField(tag=15, wire=WireType.MESSAGE, cls=ToolOverrides)] = None
    enable_side_by_side: Annotated[bool, ProtoField(tag=16, wire=WireType.BOOL)] = False
    send_final_metadata: Annotated[bool, ProtoField(tag=18, wire=WireType.BOOL)] = False
    custom_instructions: Annotated[str, ProtoField(tag=19, wire=WireType.STRING)] = ""
    custom_personality: Annotated[str, ProtoField(tag=20, wire=WireType.STRING)] = ""
    deepsearch_preset: Annotated[str, ProtoField(tag=30, wire=WireType.STRING)] = ""
    image_edit_uri: Annotated[str, ProtoField(tag=31, wire=WireType.STRING)] = ""
    is_reasoning: Annotated[bool, ProtoField(tag=32, wire=WireType.BOOL)] = False
    webpage_urls: Annotated[List[str], ProtoField(tag=33, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    image_edit_uris: Annotated[List[str], ProtoField(tag=34, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    workspace_ids: Annotated[List[str], ProtoField(tag=35, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    disable_text_follow_ups: Annotated[bool, ProtoField(tag=36, wire=WireType.BOOL)] = False
    disable_artifact: Annotated[bool, ProtoField(tag=37, wire=WireType.BOOL)] = False
    response_metadata: Annotated[dict, ProtoField(tag=38, wire=WireType.JSON_STRUCT)] = Field(default_factory=dict)
    disable_artifact_diff: Annotated[bool, ProtoField(tag=39, wire=WireType.BOOL)] = False
    do_force_trigger_artifact: Annotated[bool, ProtoField(tag=40, wire=WireType.BOOL)] = False
    is_from_grok_files: Annotated[bool, ProtoField(tag=41, wire=WireType.BOOL)] = False
    selected_file_text_content: Annotated[str, ProtoField(tag=42, wire=WireType.STRING)] = ""
    selected_file_text_content_start_position: Annotated[int, ProtoField(tag=43, wire=WireType.INT32)] = 0
    selected_file_text_content_end_position: Annotated[int, ProtoField(tag=44, wire=WireType.INT32)] = 0
    disable_memory: Annotated[bool, ProtoField(tag=45, wire=WireType.BOOL)] = False
    force_side_by_side: Annotated[bool, ProtoField(tag=46, wire=WireType.BOOL)] = False
    model_mode: Annotated[ModelMode, ProtoField(tag=48, wire=WireType.INT32)] = ModelMode.BASE
    models_user_can_use: Annotated[List[str], ProtoField(tag=49, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    skip_response_cache: Annotated[bool, ProtoField(tag=50, wire=WireType.BOOL)] = False
    is_async_chat: Annotated[bool, ProtoField(tag=51, wire=WireType.BOOL)] = False
    enable_nsfw: Annotated[bool, ProtoField(tag=52, wire=WireType.BOOL)] = False
    is_kids_mode: Annotated[bool, ProtoField(tag=53, wire=WireType.BOOL)] = False
    supported_fast_tools: Annotated[Optional[SupportedFastTools], ProtoField(tag=54, wire=WireType.MESSAGE, cls=SupportedFastTools)] = None
    is_regen_request: Annotated[bool, ProtoField(tag=55, wire=WireType.BOOL)] = False
    companion_id: Annotated[str, ProtoField(tag=59, wire=WireType.STRING)] = ""
    template_id: Annotated[str, ProtoField(tag=60, wire=WireType.STRING)] = ""
    disable_self_harm_short_circuit: Annotated[bool, ProtoField(tag=61, wire=WireType.BOOL)] = False
    collection_ids: Annotated[List[str], ProtoField(tag=62, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    connector_ids: Annotated[List[str], ProtoField(tag=63, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    search_all_connectors: Annotated[bool, ProtoField(tag=64, wire=WireType.BOOL)] = False
    device_env_info: Annotated[Optional[DeviceEnvInfo], ProtoField(tag=65, wire=WireType.MESSAGE, cls=DeviceEnvInfo)] = None
    model_override_key: Annotated[str, ProtoField(tag=66, wire=WireType.STRING)] = ""
    browser_geo_location: Annotated[Optional[GeoLocation], ProtoField(tag=67, wire=WireType.MESSAGE, cls=GeoLocation)] = None
    disable_personalization: Annotated[bool, ProtoField(tag=69, wire=WireType.BOOL)] = False
    connectors: Annotated[List[Connector], ProtoField(tag=70, wire=WireType.REPEATED_MESSAGE, cls=Connector)] = Field(default_factory=list)
    imagine_project_id: Annotated[str, ProtoField(tag=71, wire=WireType.STRING)] = ""
    mode_id: Annotated[str, ProtoField(tag=72, wire=WireType.STRING)] = ""
    imagine_canvas_context: Annotated[Optional[ImagineCanvasContext], ProtoField(tag=75, wire=WireType.MESSAGE, cls=ImagineCanvasContext)] = None
    disabled_connector_ids: Annotated[List[str], ProtoField(tag=76, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class CreateConversationAndRespondResponseChunk(BaseModel):
    response: Annotated[Optional[AddResponseResponse], ProtoField(tag=1, wire=WireType.MESSAGE, cls=AddResponseResponse)] = None
    conversation: Annotated[Optional[Conversation], ProtoField(tag=2, wire=WireType.MESSAGE, cls=Conversation)] = None
    title: Annotated[Optional[GenerateTitleResponse], ProtoField(tag=3, wire=WireType.MESSAGE, cls=GenerateTitleResponse)] = None


class CreateConversationRequest(BaseModel):
    system_prompt_name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    temporary: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    add_response_request: Annotated[Optional[AddResponseRequest], ProtoField(tag=3, wire=WireType.MESSAGE, cls=AddResponseRequest)] = None
    workspace_ids: Annotated[List[str], ProtoField(tag=4, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    task_result_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    template_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class CreateGrokCastRequest(BaseModel):
    title: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    generation_prompt: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    audio_asset_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    alignment_info: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class CreateMediaConversationRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    canvas_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    post_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class MediaConversation(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    user_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    canvas_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    post_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    created_at: Annotated[str, ProtoField(tag=6, wire=WireType.TIMESTAMP)] = ""
    updated_at: Annotated[str, ProtoField(tag=7, wire=WireType.TIMESTAMP)] = ""


class CreateMediaConversationResponse(BaseModel):
    conversation: Annotated[Optional[MediaConversation], ProtoField(tag=1, wire=WireType.MESSAGE, cls=MediaConversation)] = None


class CreateMediaFolderRequest(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class MediaFolder(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    user_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=4, wire=WireType.TIMESTAMP)] = ""
    update_time: Annotated[str, ProtoField(tag=5, wire=WireType.TIMESTAMP)] = ""


class CreateMediaFolderResponse(BaseModel):
    folder: Annotated[Optional[MediaFolder], ProtoField(tag=1, wire=WireType.MESSAGE, cls=MediaFolder)] = None


class CreateMediaPostRequest(BaseModel):
    media_type: Annotated[MediaPostType, ProtoField(tag=1, wire=WireType.INT32)] = MediaPostType.MEDIA_POST_TYPE_INVALID
    media_url: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    original_post_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    prompt: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    original_ref_type: Annotated[OriginalRefType, ProtoField(tag=5, wire=WireType.INT32)] = OriginalRefType.ORIGINAL_REF_TYPE_INVALID
    asset_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class CreateMediaPostResponse(BaseModel):
    post: Annotated[Optional[MediaPost], ProtoField(tag=1, wire=WireType.MESSAGE, cls=MediaPost)] = None


class CreateMediaProjectRequest(BaseModel):
    pass


class MediaProjectAsset(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    thumbnail_image_url: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class MediaProjectClip(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    asset_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    start_time: Annotated[float, ProtoField(tag=3, wire=WireType.DOUBLE)] = 0.0
    end_time: Annotated[float, ProtoField(tag=4, wire=WireType.DOUBLE)] = 0.0


class MediaProjectTimeline(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    clips: Annotated[List[MediaProjectClip], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=MediaProjectClip)] = Field(default_factory=list)


class MediaProject(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    user_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    versions: Annotated[List[str], ProtoField(tag=3, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    current_version: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    assets: Annotated[List[MediaProjectAsset], ProtoField(tag=5, wire=WireType.REPEATED_MESSAGE, cls=MediaProjectAsset)] = Field(default_factory=list)
    timelines: Annotated[List[MediaProjectTimeline], ProtoField(tag=6, wire=WireType.REPEATED_MESSAGE, cls=MediaProjectTimeline)] = Field(default_factory=list)
    create_time: Annotated[str, ProtoField(tag=7, wire=WireType.TIMESTAMP)] = ""
    update_time: Annotated[str, ProtoField(tag=8, wire=WireType.TIMESTAMP)] = ""
    conversation_ids: Annotated[List[str], ProtoField(tag=9, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class CreateMediaProjectResponse(BaseModel):
    project: Annotated[Optional[MediaProject], ProtoField(tag=1, wire=WireType.MESSAGE, cls=MediaProject)] = None


class CreatePassphraseRequest(BaseModel):
    language_code: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class CreatePassphraseResponse(BaseModel):
    passphrase_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    retrievable_at_ms: Annotated[int, ProtoField(tag=2, wire=WireType.INT64)] = 0
    expires_at_ms: Annotated[int, ProtoField(tag=3, wire=WireType.INT64)] = 0


class CreatePipelineTemplateRequest(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    thumbnail_url: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    preview_url: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    spec_json: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    anonymous: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False


class PipelineTemplateVersionInfo(BaseModel):
    version: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    published_at: Annotated[str, ProtoField(tag=2, wire=WireType.TIMESTAMP)] = ""
    published_by: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class PipelineTemplateProto(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    thumbnail_url: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    preview_url: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    spec_json: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    versions: Annotated[List[PipelineTemplateVersionInfo], ProtoField(tag=9, wire=WireType.REPEATED_MESSAGE, cls=PipelineTemplateVersionInfo)] = Field(default_factory=list)
    published_version: Annotated[int, ProtoField(tag=10, wire=WireType.INT32)] = 0
    user_id: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    visibility: Annotated[PipelineTemplateVisibility, ProtoField(tag=13, wire=WireType.INT32)] = PipelineTemplateVisibility.PIPELINE_TEMPLATE_VISIBILITY_PRIVATE
    is_featured: Annotated[bool, ProtoField(tag=14, wire=WireType.BOOL)] = False
    sort_order: Annotated[int, ProtoField(tag=15, wire=WireType.INT32)] = 0
    run_count: Annotated[int, ProtoField(tag=16, wire=WireType.INT64)] = 0
    credit_cost: Annotated[int, ProtoField(tag=17, wire=WireType.INT32)] = 0
    created_at: Annotated[str, ProtoField(tag=18, wire=WireType.TIMESTAMP)] = ""
    updated_at: Annotated[str, ProtoField(tag=19, wire=WireType.TIMESTAMP)] = ""
    x_handle: Annotated[str, ProtoField(tag=20, wire=WireType.STRING)] = ""


class CreatePipelineTemplateResponse(BaseModel):
    template: Annotated[Optional[PipelineTemplateProto], ProtoField(tag=1, wire=WireType.MESSAGE, cls=PipelineTemplateProto)] = None


class CreatePostLinkRequest(BaseModel):
    post_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    source: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    platform: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class CreatePostLinkResponse(BaseModel):
    share_link: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class CreateShareLinkRequest(BaseModel):
    voice_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ShareLinkMetadata(BaseModel):
    share_token: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    voice_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    owner_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    voice_name: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    creator_display_name: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    duration_seconds: Annotated[float, ProtoField(tag=6, wire=WireType.FLOAT)] = 0.0
    created_at: Annotated[str, ProtoField(tag=7, wire=WireType.TIMESTAMP)] = ""
    resolve_count: Annotated[int, ProtoField(tag=8, wire=WireType.INT64)] = 0


class CreateShareLinkResponse(BaseModel):
    share_token: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    metadata: Annotated[Optional[ShareLinkMetadata], ProtoField(tag=2, wire=WireType.MESSAGE, cls=ShareLinkMetadata)] = None


class CreateTokenRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    agent_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    session_payload: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    request_agent_dispatch: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    livekit_url: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    params: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class CreateTokenResponse(BaseModel):
    token: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    request_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class CreateVoiceRequest(BaseModel):
    audio_b64: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    format_f: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    passphrase_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class VoiceMetadata(BaseModel):
    voice_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    user_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    gcs_path: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    duration_seconds: Annotated[float, ProtoField(tag=5, wire=WireType.FLOAT)] = 0.0
    sample_rate: Annotated[int, ProtoField(tag=6, wire=WireType.INT32)] = 0
    sha256_hash: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    created_at: Annotated[str, ProtoField(tag=8, wire=WireType.TIMESTAMP)] = ""
    updated_at: Annotated[str, ProtoField(tag=9, wire=WireType.TIMESTAMP)] = ""
    deleted_at: Annotated[str, ProtoField(tag=10, wire=WireType.TIMESTAMP)] = ""
    visibility: Annotated[VoiceVisibility, ProtoField(tag=11, wire=WireType.INT32)] = VoiceVisibility.VOICE_VISIBILITY_UNSPECIFIED
    personality_preset_id: Annotated[str, ProtoField(tag=12, wire=WireType.STRING)] = ""
    personality_custom_prompt: Annotated[str, ProtoField(tag=13, wire=WireType.STRING)] = ""
    approved: Annotated[bool, ProtoField(tag=14, wire=WireType.BOOL)] = False


class CreateVoiceResponse(BaseModel):
    voice_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    metadata: Annotated[Optional[VoiceMetadata], ProtoField(tag=2, wire=WireType.MESSAGE, cls=VoiceMetadata)] = None


class DeleteAllMediaPostDataRequest(BaseModel):
    pass


class DeleteAllMediaPostDataResponse(BaseModel):
    pass


class DeleteAllMemoriesV2Request(BaseModel):
    companion_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class DeleteAllMemoriesV2Response(BaseModel):
    num_deleted: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0


class DeleteCanvasDocumentRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class DeleteCanvasDocumentResponse(BaseModel):
    pass


class DeleteCanvasNodeRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class DeleteCanvasNodeResponse(BaseModel):
    pass


class DeleteCharactersRequest(BaseModel):
    character_ids: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class DeleteCharactersResponse(BaseModel):
    pass


class DeleteCompanionConversationRequest(BaseModel):
    companion_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class DeleteCompanionConversationResponse(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class DeleteConversationRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    delete_media: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class DeleteMediaFolderRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class DeleteMediaFolderResponse(BaseModel):
    pass


class DeleteMediaPostRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    is_hidden_for_client: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class DeleteMediaPostResponse(BaseModel):
    pass


class DeleteMemoryRequest(BaseModel):
    conversation_ids: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class DeletePipelineTemplateRequest(BaseModel):
    template_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class DeletePipelineTemplateResponse(BaseModel):
    pass


class DeleteShareLinkRequest(BaseModel):
    share_link_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class DeleteSingleMemoryV2Request(BaseModel):
    id_f: Annotated[int, ProtoField(tag=1, wire=WireType.INT64)] = 0


class DeleteUserSkillRequest(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class DeleteVoiceRequest(BaseModel):
    voice_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class DeleteVoiceResponse(BaseModel):
    success: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False


class DirectUploadData(BaseModel):
    file_data: Annotated[bytes, ProtoField(tag=1, wire=WireType.BYTES_FIELD)] = b""
    file_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    file_mime_type: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    file_source: Annotated[UploadedFileSourceType, ProtoField(tag=4, wire=WireType.INT32)] = UploadedFileSourceType.SELF_UPLOAD_FILE_SOURCE


class DownloadUserSkillRequest(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class DownloadUserSkillResponse(BaseModel):
    zip_content: Annotated[bytes, ProtoField(tag=1, wire=WireType.BYTES_FIELD)] = b""
    filename: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class EditMemoryV2Request(BaseModel):
    id_f: Annotated[int, ProtoField(tag=1, wire=WireType.INT64)] = 0
    content: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class UserMemoryV2(BaseModel):
    id_f: Annotated[int, ProtoField(tag=1, wire=WireType.INT64)] = 0
    content: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    companion_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    created_at: Annotated[str, ProtoField(tag=4, wire=WireType.TIMESTAMP)] = ""
    updated_at: Annotated[str, ProtoField(tag=5, wire=WireType.TIMESTAMP)] = ""
    expires_at: Annotated[str, ProtoField(tag=6, wire=WireType.TIMESTAMP)] = ""


class EditMemoryV2Response(BaseModel):
    memory: Annotated[Optional[UserMemoryV2], ProtoField(tag=1, wire=WireType.MESSAGE, cls=UserMemoryV2)] = None


class EditVoiceApprovalRequest(BaseModel):
    voice_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    approved: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class EditVoiceApprovalResponse(BaseModel):
    metadata: Annotated[Optional[VoiceMetadata], ProtoField(tag=1, wire=WireType.MESSAGE, cls=VoiceMetadata)] = None


class FeatureControls(BaseModel):
    enable_file_uploads: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    enable_image_uploads: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    enable_web_search: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    enable_x_search: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    enable_voice_mode: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False
    enable_imagine: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    enable_imagine_nsfw: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False
    enable_imagine_chat: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False


class FeedbackAttachment(BaseModel):
    filename: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    content_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    data__f: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class FetchMemoriesV2Request(BaseModel):
    companion_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class FetchMemoriesV2Response(BaseModel):
    memories: Annotated[List[UserMemoryV2], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=UserMemoryV2)] = Field(default_factory=list)


class FileUploadAbortRequest(BaseModel):
    upload_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class FileUploadAbortResponse(BaseModel):
    final_status: Annotated[UploadJobStatus, ProtoField(tag=1, wire=WireType.INT32)] = UploadJobStatus.UNSET
    aborted_now: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class FileUploadStatusRequest(BaseModel):
    upload_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class FileUploadStatusResponse(BaseModel):
    upload_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    asset_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    status: Annotated[UploadJobStatus, ProtoField(tag=3, wire=WireType.INT32)] = UploadJobStatus.UNSET
    file_metadata: Annotated[Optional[FileMetadata], ProtoField(tag=4, wire=WireType.MESSAGE, cls=FileMetadata)] = None
    error_message: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class FinancialValue(BaseModel):
    value__f: Annotated[float, ProtoField(tag=1, wire=WireType.DOUBLE)] = 0.0
    change: Annotated[float, ProtoField(tag=2, wire=WireType.DOUBLE)] = 0.0
    change_percent: Annotated[float, ProtoField(tag=3, wire=WireType.DOUBLE)] = 0.0
    unit: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    label: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class FinancialReport(BaseModel):
    fiscal_year: Annotated[int, ProtoField(tag=1, wire=WireType.INT64)] = 0
    fiscal_period: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    report: Annotated[Optional[FinancialValue], ProtoField(tag=3, wire=WireType.MESSAGE, cls=FinancialValue)] = None
    end_date: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    filing_date: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class FindStockRequest(BaseModel):
    ticker: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class StockOverview(BaseModel):
    ticker: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    icon_url: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    logo_url: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    exchange: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    currency: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    market: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    weighted_shares_outstanding: Annotated[int, ProtoField(tag=8, wire=WireType.INT64)] = 0
    share_class_shares_outstanding: Annotated[int, ProtoField(tag=9, wire=WireType.INT64)] = 0
    ticker_type: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""


class StockChartData(BaseModel):
    timestamp: Annotated[int, ProtoField(tag=1, wire=WireType.INT64)] = 0
    open__f: Annotated[float, ProtoField(tag=2, wire=WireType.DOUBLE)] = 0.0
    high: Annotated[float, ProtoField(tag=3, wire=WireType.DOUBLE)] = 0.0
    low: Annotated[float, ProtoField(tag=4, wire=WireType.DOUBLE)] = 0.0
    close: Annotated[float, ProtoField(tag=5, wire=WireType.DOUBLE)] = 0.0
    volume: Annotated[float, ProtoField(tag=6, wire=WireType.DOUBLE)] = 0.0
    average: Annotated[float, ProtoField(tag=7, wire=WireType.DOUBLE)] = 0.0


class GetStockMiniSummaryResponse(BaseModel):
    ticker: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    stock_overview: Annotated[Optional[StockOverview], ProtoField(tag=2, wire=WireType.MESSAGE, cls=StockOverview)] = None
    finance_value: Annotated[Optional[FinancialValue], ProtoField(tag=3, wire=WireType.MESSAGE, cls=FinancialValue)] = None
    prev_day: Annotated[Optional[StockChartData], ProtoField(tag=4, wire=WireType.MESSAGE, cls=StockChartData)] = None
    timestamp: Annotated[int, ProtoField(tag=5, wire=WireType.INT64)] = 0


class FindStockResponse(BaseModel):
    stock_summaries: Annotated[List[GetStockMiniSummaryResponse], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=GetStockMiniSummaryResponse)] = Field(default_factory=list)


class ForkPipelineTemplateRequest(BaseModel):
    source_template_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ForkPipelineTemplateResponse(BaseModel):
    template: Annotated[Optional[PipelineTemplateProto], ProtoField(tag=1, wire=WireType.MESSAGE, cls=PipelineTemplateProto)] = None


class GenerateTitleRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    leaf_response_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GetAllArtifactsMetadataRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GrokStudioArtifactMetadata(BaseModel):
    artifact_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    content_type: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=5, wire=WireType.TIMESTAMP)] = ""
    inline_status: Annotated[ArtifactInlineStatusType, ProtoField(tag=6, wire=WireType.INT32)] = ArtifactInlineStatusType.DEFAULT_ARTIFACT_INLINE_STATUS
    update_time: Annotated[str, ProtoField(tag=7, wire=WireType.TIMESTAMP)] = ""


class GetAllArtifactsMetadataResponse(BaseModel):
    artifacts_metadata: Annotated[List[GrokStudioArtifactMetadata], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=GrokStudioArtifactMetadata)] = Field(default_factory=list)


class GetArtifactByIdRequest(BaseModel):
    artifact_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    response_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class GrokStudioVersionedArtifact(BaseModel):
    artifact_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    artifact_version_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    content_type: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    response_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    full_artifact: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    artifact_diff: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=9, wire=WireType.TIMESTAMP)] = ""
    inline_status: Annotated[ArtifactInlineStatusType, ProtoField(tag=10, wire=WireType.INT32)] = ArtifactInlineStatusType.DEFAULT_ARTIFACT_INLINE_STATUS
    update_time: Annotated[str, ProtoField(tag=11, wire=WireType.TIMESTAMP)] = ""


class GetArtifactByIdResponse(BaseModel):
    artifacts: Annotated[List[GrokStudioVersionedArtifact], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=GrokStudioVersionedArtifact)] = Field(default_factory=list)


class GetArtifactContentRequest(BaseModel):
    artifact_version_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetArtifactContentResponse(BaseModel):
    full_artifact: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    artifact_diff: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GetAttestationChallengeRequest(BaseModel):
    pass


class GetAttestationChallengeResponse(BaseModel):
    challenge: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetCanvasAssetsRequest(BaseModel):
    asset_ids: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class GetCanvasAssetsResponse(BaseModel):
    assets: Annotated[List[CanvasAssetData], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=CanvasAssetData)] = Field(default_factory=list)


class GetCanvasDocumentRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetCanvasDocumentResponse(BaseModel):
    document: Annotated[Optional[CanvasDocument], ProtoField(tag=1, wire=WireType.MESSAGE, cls=CanvasDocument)] = None
    nodes: Annotated[List[CanvasNode], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=CanvasNode)] = Field(default_factory=list)


class GetCompanionConversationsRequest(BaseModel):
    pass


class GetCompanionConversationsResponse(BaseModel):
    conversations: Annotated[List[CompanionConversation], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=CompanionConversation)] = Field(default_factory=list)


class GetConversationExistsRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetConversationExistsResponse(BaseModel):
    exists: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False


class GetConversationRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    include_workspaces: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    include_task_result: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    rid: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class GrokForTeamsSwitchPrompt(BaseModel):
    team_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    switch_to_personal_team: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class GetConversationResponse(BaseModel):
    conversation: Annotated[Optional[Conversation], ProtoField(tag=1, wire=WireType.MESSAGE, cls=Conversation)] = None
    share_link_path: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    team_switch_prompt: Annotated[Optional[GrokForTeamsSwitchPrompt], ProtoField(tag=3, wire=WireType.MESSAGE, cls=GrokForTeamsSwitchPrompt)] = None


class GetConversationStartersResponse(BaseModel):
    starters: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class GetConversationsRequest(BaseModel):
    conversation_ids: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    include_workspaces: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    include_task_result: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False


class GetConversationsResponse(BaseModel):
    conversations: Annotated[List[Conversation], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=Conversation)] = Field(default_factory=list)


class GetFeatureControlsRequest(BaseModel):
    team_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetFileMetadataRequest(BaseModel):
    file_metadata_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetGrokCastRequest(BaseModel):
    grokcast_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetImagineQuotaInfoRequest(BaseModel):
    pass


class ImagineQuotaInfo(BaseModel):
    available: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    remaining_queries: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    window_size_seconds: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    next_available_at: Annotated[str, ProtoField(tag=4, wire=WireType.TIMESTAMP)] = ""


class GetImagineQuotaInfoResponse(BaseModel):
    image: Annotated[Optional[ImagineQuotaInfo], ProtoField(tag=1, wire=WireType.MESSAGE, cls=ImagineQuotaInfo)] = None
    image_pro: Annotated[Optional[ImagineQuotaInfo], ProtoField(tag=2, wire=WireType.MESSAGE, cls=ImagineQuotaInfo)] = None
    image_edit: Annotated[Optional[ImagineQuotaInfo], ProtoField(tag=3, wire=WireType.MESSAGE, cls=ImagineQuotaInfo)] = None
    video: Annotated[Optional[ImagineQuotaInfo], ProtoField(tag=4, wire=WireType.MESSAGE, cls=ImagineQuotaInfo)] = None
    video_720p: Annotated[Optional[ImagineQuotaInfo], ProtoField(tag=5, wire=WireType.MESSAGE, cls=ImagineQuotaInfo)] = None


class GetImportedMemoryStatusRequest(BaseModel):
    pass


class GetImportedMemoryStatusResponse(BaseModel):
    status: Annotated[ImportedMemoryStatus, ProtoField(tag=1, wire=WireType.INT32)] = ImportedMemoryStatus.IMPORTED_MEMORY_STATUS_UNSPECIFIED
    last_import_timestamp: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GetMediaConversationsRequest(BaseModel):
    canvas_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    post_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GetMediaConversationsResponse(BaseModel):
    conversations: Annotated[List[MediaConversation], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=MediaConversation)] = Field(default_factory=list)


class GetMediaPostRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    is_kids_mode: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    is_nsfw_enabled: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    with_container_only: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    request_user_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class GetMediaPostResponse(BaseModel):
    post: Annotated[Optional[MediaPost], ProtoField(tag=1, wire=WireType.MESSAGE, cls=MediaPost)] = None


class GetMediaProjectRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetMediaProjectResponse(BaseModel):
    project: Annotated[Optional[MediaProject], ProtoField(tag=1, wire=WireType.MESSAGE, cls=MediaProject)] = None


class GetMediaSearchStatusRequest(BaseModel):
    pass


class GetMediaSearchStatusResponse(BaseModel):
    status: Annotated[MediaSearchIndexStatus, ProtoField(tag=1, wire=WireType.INT32)] = MediaSearchIndexStatus.MEDIA_SEARCH_INDEX_STATUS_NOT_ELIGIBLE
    item_count: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class GetMemoryRequest(BaseModel):
    conversation_ids: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class UserMemory(BaseModel):
    convo_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    convo_summary: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GetMemoryResponse(BaseModel):
    memories: Annotated[List[UserMemory], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=UserMemory)] = Field(default_factory=list)


class GetModelsImagineOverridesRequest(BaseModel):
    pass


class ModelMapOverride(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    key: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    type_f: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    options: Annotated[List[str], ProtoField(tag=4, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class GetModelsImagineOverridesResponse(BaseModel):
    model_map_overrides: Annotated[List[ModelMapOverride], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=ModelMapOverride)] = Field(default_factory=list)


class GetModelsRequest(BaseModel):
    locale: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ModelDescription(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    model_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    tags: Annotated[List[str], ProtoField(tag=4, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    badge_text: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    model_mode: Annotated[ModelMode, ProtoField(tag=6, wire=WireType.INT32)] = ModelMode.BASE
    mode_description: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    mode_name: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    prompting_backend: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""


class GetModelsResponse(BaseModel):
    models: Annotated[List[ModelDescription], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=ModelDescription)] = Field(default_factory=list)
    default_free_model: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    default_pro_model: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    unavailable_models: Annotated[List[ModelDescription], ProtoField(tag=4, wire=WireType.REPEATED_MESSAGE, cls=ModelDescription)] = Field(default_factory=list)
    default_anon_model: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    default_heavy_model: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    default_anon_mode: Annotated[ModelMode, ProtoField(tag=7, wire=WireType.INT32)] = ModelMode.BASE
    default_free_mode: Annotated[ModelMode, ProtoField(tag=8, wire=WireType.INT32)] = ModelMode.BASE
    default_pro_mode: Annotated[ModelMode, ProtoField(tag=9, wire=WireType.INT32)] = ModelMode.BASE
    default_heavy_mode: Annotated[ModelMode, ProtoField(tag=10, wire=WireType.INT32)] = ModelMode.BASE


class GetPassphraseRequest(BaseModel):
    passphrase_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetPassphraseResponse(BaseModel):
    passphrase: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetPipelineTemplateRequest(BaseModel):
    template_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class PipelineTemplateInputDef(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    input_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    label: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    required: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False
    default_value: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class PipelineTemplateSummary(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    thumbnail_url: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    preview_url: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    inputs: Annotated[List[PipelineTemplateInputDef], ProtoField(tag=8, wire=WireType.REPEATED_MESSAGE, cls=PipelineTemplateInputDef)] = Field(default_factory=list)
    published_version: Annotated[int, ProtoField(tag=9, wire=WireType.INT32)] = 0
    user_id: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    run_count: Annotated[int, ProtoField(tag=11, wire=WireType.INT64)] = 0
    credit_cost: Annotated[int, ProtoField(tag=12, wire=WireType.INT32)] = 0
    created_at: Annotated[str, ProtoField(tag=13, wire=WireType.TIMESTAMP)] = ""
    x_handle: Annotated[str, ProtoField(tag=14, wire=WireType.STRING)] = ""
    primary_output_media_type: Annotated[str, ProtoField(tag=15, wire=WireType.STRING)] = ""


class GetPipelineTemplateResponse(BaseModel):
    template: Annotated[Optional[PipelineTemplateProto], ProtoField(tag=1, wire=WireType.MESSAGE, cls=PipelineTemplateProto)] = None
    summary: Annotated[Optional[PipelineTemplateSummary], ProtoField(tag=2, wire=WireType.MESSAGE, cls=PipelineTemplateSummary)] = None


class GetQuickAnswerRequest(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class Suggestion(BaseModel):
    text: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    type_f: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GetQuickAnswerResponse(BaseModel):
    suggestions: Annotated[List[Suggestion], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=Suggestion)] = Field(default_factory=list)


class GetRateLimitsRequest(BaseModel):
    request_kind: Annotated[RequestKind, ProtoField(tag=1, wire=WireType.INT32)] = RequestKind.DEFAULT
    model_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ModelEffortRateLimits(BaseModel):
    cost: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    wait_time_seconds: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    remaining_queries: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0


class GetRateLimitsResponse(BaseModel):
    window_size_seconds: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    remaining_queries: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    wait_time_seconds: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    total_queries: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    remaining_tokens: Annotated[int, ProtoField(tag=5, wire=WireType.INT32)] = 0
    total_tokens: Annotated[int, ProtoField(tag=6, wire=WireType.INT32)] = 0
    low_effort_rate_limits: Annotated[Optional[ModelEffortRateLimits], ProtoField(tag=7, wire=WireType.MESSAGE, cls=ModelEffortRateLimits)] = None
    high_effort_rate_limits: Annotated[Optional[ModelEffortRateLimits], ProtoField(tag=8, wire=WireType.MESSAGE, cls=ModelEffortRateLimits)] = None
    pre_generation_delay_ms: Annotated[int, ProtoField(tag=9, wire=WireType.INT32)] = 0


class GetRelatedTickersResponse(BaseModel):
    related_tickers: Annotated[Optional[GetStockMiniSummaryResponse], ProtoField(tag=1, wire=WireType.MESSAGE, cls=GetStockMiniSummaryResponse)] = None


class GetShareLinkRequest(BaseModel):
    share_link_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetShareLinkResponse(BaseModel):
    responses: Annotated[List[Response], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=Response)] = Field(default_factory=list)
    conversation: Annotated[Optional[Conversation], ProtoField(tag=2, wire=WireType.MESSAGE, cls=Conversation)] = None
    team_switch_prompt: Annotated[Optional[GrokForTeamsSwitchPrompt], ProtoField(tag=3, wire=WireType.MESSAGE, cls=GrokForTeamsSwitchPrompt)] = None
    allow_indexing: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    view_count: Annotated[int, ProtoField(tag=5, wire=WireType.INT64)] = 0


class GetSharedArtifactRequest(BaseModel):
    shared_artifact_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetSharedArtifactResponse(BaseModel):
    parsed_artifact: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    conversation: Annotated[Optional[Conversation], ProtoField(tag=2, wire=WireType.MESSAGE, cls=Conversation)] = None


class GetStockChartDataRequest(BaseModel):
    ticker: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    timespan: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GetStockChartDataResponse(BaseModel):
    ticker: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    chart_data: Annotated[Optional[StockChartData], ProtoField(tag=2, wire=WireType.MESSAGE, cls=StockChartData)] = None
    unit: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class GetStockFinancialsRequest(BaseModel):
    ticker: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    timeframe: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GetStockFinancialsResponse(BaseModel):
    ticker: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    balance_sheets: Annotated[Optional[FinancialReport], ProtoField(tag=2, wire=WireType.MESSAGE, cls=FinancialReport)] = None
    income_statements: Annotated[Optional[FinancialReport], ProtoField(tag=3, wire=WireType.MESSAGE, cls=FinancialReport)] = None
    cash_flows: Annotated[Optional[FinancialReport], ProtoField(tag=4, wire=WireType.MESSAGE, cls=FinancialReport)] = None


class StockDividend(BaseModel):
    ex_dividend_date: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    payment_date: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    frequency: Annotated[int, ProtoField(tag=3, wire=WireType.INT64)] = 0
    cash_amount: Annotated[float, ProtoField(tag=4, wire=WireType.DOUBLE)] = 0.0
    dividend_yield: Annotated[float, ProtoField(tag=5, wire=WireType.DOUBLE)] = 0.0


class GetStockSummaryResponse(BaseModel):
    ticker: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    timestamp: Annotated[int, ProtoField(tag=2, wire=WireType.INT64)] = 0
    market_cap: Annotated[float, ProtoField(tag=3, wire=WireType.DOUBLE)] = 0.0
    prev_day: Annotated[Optional[StockChartData], ProtoField(tag=4, wire=WireType.MESSAGE, cls=StockChartData)] = None
    current_day: Annotated[Optional[StockChartData], ProtoField(tag=5, wire=WireType.MESSAGE, cls=StockChartData)] = None
    dividend: Annotated[Optional[StockDividend], ProtoField(tag=6, wire=WireType.MESSAGE, cls=StockDividend)] = None
    one_year: Annotated[Optional[StockChartData], ProtoField(tag=7, wire=WireType.MESSAGE, cls=StockChartData)] = None


class GetStockTickerRequest(BaseModel):
    ticker: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class SuggestionConversationChatMessage(BaseModel):
    role: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    content: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class SuggestionConversationSummary(BaseModel):
    title: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    timestamp_ms: Annotated[int, ProtoField(tag=2, wire=WireType.INT64)] = 0


class GetSuggestionsRequest(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    count: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    include_answers: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    conversation: Annotated[List[SuggestionConversationChatMessage], ProtoField(tag=4, wire=WireType.REPEATED_MESSAGE, cls=SuggestionConversationChatMessage)] = Field(default_factory=list)
    conversation_history: Annotated[List[SuggestionConversationSummary], ProtoField(tag=5, wire=WireType.REPEATED_MESSAGE, cls=SuggestionConversationSummary)] = Field(default_factory=list)


class GetSuggestionsResponse(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    suggestions: Annotated[List[Suggestion], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=Suggestion)] = Field(default_factory=list)


class GetUserMemoryBlurbRequest(BaseModel):
    pass


class GetUserMemoryBlurbResponse(BaseModel):
    memory_content: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetUserSkillRequest(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetVoiceRequest(BaseModel):
    voice_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetVoiceResponse(BaseModel):
    metadata: Annotated[Optional[VoiceMetadata], ProtoField(tag=1, wire=WireType.MESSAGE, cls=VoiceMetadata)] = None


class GoogleDriveFile(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    mime_type: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class GoogleDriveFilesListRequest(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GoogleDriveFilesListResponse(BaseModel):
    files: Annotated[List[GoogleDriveFile], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=GoogleDriveFile)] = Field(default_factory=list)


class GoogleDriveReadFileRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GoogleDriveReadFileResponse(BaseModel):
    content: Annotated[bytes, ProtoField(tag=1, wire=WireType.BYTES_FIELD)] = b""
    mime: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GrokCast(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    owner_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    status: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    generation_prompt: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    audio_asset_id: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    alignment_info: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    created_at: Annotated[str, ProtoField(tag=9, wire=WireType.TIMESTAMP)] = ""
    updated_at: Annotated[str, ProtoField(tag=10, wire=WireType.TIMESTAMP)] = ""
    deleted_at: Annotated[str, ProtoField(tag=11, wire=WireType.TIMESTAMP)] = ""


class GrokCastListItem(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    status: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class GrokCompletionSuggestion(BaseModel):
    text: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ImageGeneration(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    image_url: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    image_query: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    assistant_message: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=5, wire=WireType.TIMESTAMP)] = ""
    response_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class ImportMemoryRequest(BaseModel):
    content: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class InflightResponse(BaseModel):
    response_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    status: Annotated[ResponseStatus, ProtoField(tag=2, wire=WireType.INT32)] = ResponseStatus.RESPONSE_STATUS_UNKNOWN
    create_time: Annotated[str, ProtoField(tag=3, wire=WireType.TIMESTAMP)] = ""
    parent_response_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    thread_parent_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class IosAppAttest(BaseModel):
    key_id: Annotated[bytes, ProtoField(tag=1, wire=WireType.BYTES_FIELD)] = b""
    attestation_object: Annotated[bytes, ProtoField(tag=2, wire=WireType.BYTES_FIELD)] = b""


class LikeMediaPostRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    folder_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class LikeMediaPostResponse(BaseModel):
    pass


class ListCanvasDocumentsRequest(BaseModel):
    limit: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    cursor: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ListCanvasDocumentsResponse(BaseModel):
    documents: Annotated[List[CanvasDocument], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=CanvasDocument)] = Field(default_factory=list)
    next_cursor: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ListCanvasNodesRequest(BaseModel):
    canvas_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ListCanvasNodesResponse(BaseModel):
    nodes: Annotated[List[CanvasNode], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=CanvasNode)] = Field(default_factory=list)


class ListCharactersRequest(BaseModel):
    pass


class MediaCharacter(BaseModel):
    character_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    preview_url: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    character_name: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class ListCharactersResponse(BaseModel):
    characters: Annotated[List[MediaCharacter], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=MediaCharacter)] = Field(default_factory=list)


class ListConversationsMatch(BaseModel):
    conversation: Annotated[Optional[Conversation], ProtoField(tag=1, wire=WireType.MESSAGE, cls=Conversation)] = None
    match_type: Annotated[ListConversationsMatchType, ProtoField(tag=2, wire=WireType.INT32)] = ListConversationsMatchType.UNKNOWN
    matched_response_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    highlight: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    matched_words: Annotated[List[str], ProtoField(tag=5, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class ListConversationsRequest(BaseModel):
    page_size: Annotated[int, ProtoField(tag=1, wire=WireType.INT64)] = 0
    page_token: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    search_query: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    workspace_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    filter_is_starred: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    force_elastic: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False


class ListConversationsResponse(BaseModel):
    conversations: Annotated[List[Conversation], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=Conversation)] = Field(default_factory=list)
    next_page_token: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    text_search_matches: Annotated[List[ListConversationsMatch], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=ListConversationsMatch)] = Field(default_factory=list)


class ListGrokCastsRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ListGrokCastsResponse(BaseModel):
    grokcasts: Annotated[List[GrokCastListItem], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=GrokCastListItem)] = Field(default_factory=list)


class ListImageGenerationsResponse(BaseModel):
    generations: Annotated[List[ImageGeneration], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=ImageGeneration)] = Field(default_factory=list)


class ListMediaFoldersRequest(BaseModel):
    pass


class ListMediaFoldersResponse(BaseModel):
    folders: Annotated[List[MediaFolder], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=MediaFolder)] = Field(default_factory=list)


class ListMediaPostFoldersRequest(BaseModel):
    post_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ListMediaPostFoldersResponse(BaseModel):
    folders: Annotated[List[MediaFolder], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=MediaFolder)] = Field(default_factory=list)


class ListMediaPostsFilter(BaseModel):
    source: Annotated[MediaPostSource, ProtoField(tag=1, wire=WireType.INT32)] = MediaPostSource.MEDIA_POST_SOURCE_INVALID
    user_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    media_type: Annotated[MediaPostType, ProtoField(tag=3, wire=WireType.INT32)] = MediaPostType.MEDIA_POST_TYPE_INVALID
    folder_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    safe_for_work: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False


class ListMediaPostsRequest(BaseModel):
    limit: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    cursor: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    filter: Annotated[Optional[ListMediaPostsFilter], ProtoField(tag=3, wire=WireType.MESSAGE, cls=ListMediaPostsFilter)] = None
    is_kids_mode: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    is_nsfw_enabled: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False
    with_container_only: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    include_canvas: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False


class ListMediaPostsResponse(BaseModel):
    posts: Annotated[List[MediaPost], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=MediaPost)] = Field(default_factory=list)
    next_cursor: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ListMediaProjectsRequest(BaseModel):
    limit: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    cursor: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ListMediaProjectsResponse(BaseModel):
    projects: Annotated[List[MediaProject], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=MediaProject)] = Field(default_factory=list)
    next_cursor: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ListModesRequest(BaseModel):
    locale: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ModeAvailabilityUnavailable(BaseModel):
    message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class Unavailable(BaseModel):
    message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ModeAvailabilityRequiresUpgrade(BaseModel):
    message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    minimum_subscription_tier: Annotated[ModeSubscriptionTier, ProtoField(tag=2, wire=WireType.INT32)] = ModeSubscriptionTier.TIER_UNSPECIFIED


class RequiresUpgrade(BaseModel):
    message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    minimum_subscription_tier: Annotated[ModeSubscriptionTier, ProtoField(tag=2, wire=WireType.INT32)] = ModeSubscriptionTier.TIER_UNSPECIFIED


class ModeAvailabilityComingSoon(BaseModel):
    message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    eta: Annotated[bytes, ProtoField(tag=2, wire=WireType.BYTES_FIELD)] = b""


class ComingSoon(BaseModel):
    message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    eta: Annotated[bytes, ProtoField(tag=2, wire=WireType.BYTES_FIELD)] = b""


class ModeAvailability(BaseModel):
    available: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    unavailable: Annotated[Optional[ModeAvailabilityUnavailable], ProtoField(tag=2, wire=WireType.MESSAGE, cls=ModeAvailabilityUnavailable)] = None
    requires_upgrade: Annotated[Optional[ModeAvailabilityRequiresUpgrade], ProtoField(tag=3, wire=WireType.MESSAGE, cls=ModeAvailabilityRequiresUpgrade)] = None
    coming_soon: Annotated[Optional[ModeAvailabilityComingSoon], ProtoField(tag=4, wire=WireType.MESSAGE, cls=ModeAvailabilityComingSoon)] = None


class Mode(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    badge_text: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    availability: Annotated[Optional[ModeAvailability], ProtoField(tag=5, wire=WireType.MESSAGE, cls=ModeAvailability)] = None
    icon_hint: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    tags: Annotated[List[ModeTag], ProtoField(tag=7, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class ListModesResponse(BaseModel):
    modes: Annotated[List[Mode], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    default_mode_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class PermissionResponseEntry(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    definition: Annotated[Optional[ToolDefinition], ProtoField(tag=2, wire=WireType.MESSAGE, cls=ToolDefinition)] = None


class ListPermissionsResponse(BaseModel):
    tools: Annotated[List[PermissionResponseEntry], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=PermissionResponseEntry)] = Field(default_factory=list)


class ListPipelineTemplatesRequest(BaseModel):
    filter: Annotated[PipelineTemplateListFilter, ProtoField(tag=1, wire=WireType.INT32)] = PipelineTemplateListFilter.PIPELINE_TEMPLATE_LIST_FILTER_FEATURED
    limit: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    cursor: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class ListPipelineTemplatesResponse(BaseModel):
    templates: Annotated[List[PipelineTemplateProto], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=PipelineTemplateProto)] = Field(default_factory=list)
    summaries: Annotated[List[PipelineTemplateSummary], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=PipelineTemplateSummary)] = Field(default_factory=list)
    next_cursor: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class ListResponseNodesRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    include_threads: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class ResponseNode(BaseModel):
    response_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    sender: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    parent_response_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    thread_parent_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class ListResponseNodesResponse(BaseModel):
    response_nodes: Annotated[List[ResponseNode], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=ResponseNode)] = Field(default_factory=list)
    inflight_responses: Annotated[List[InflightResponse], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=InflightResponse)] = Field(default_factory=list)


class ListResponsesRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    include_threads: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class ListResponsesResponse(BaseModel):
    responses: Annotated[List[Response], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=Response)] = Field(default_factory=list)
    inflight_responses: Annotated[List[InflightResponse], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=InflightResponse)] = Field(default_factory=list)


class ListSavedVoicesRequest(BaseModel):
    limit: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0


class SavedVoiceEntry(BaseModel):
    voice_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    saved_at: Annotated[str, ProtoField(tag=2, wire=WireType.TIMESTAMP)] = ""
    voice: Annotated[Optional[VoiceMetadata], ProtoField(tag=3, wire=WireType.MESSAGE, cls=VoiceMetadata)] = None


class ListSavedVoicesResponse(BaseModel):
    saved_voices: Annotated[List[SavedVoiceEntry], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=SavedVoiceEntry)] = Field(default_factory=list)


class ShareLinkSummary(BaseModel):
    share_link_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    conversation_title: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=4, wire=WireType.TIMESTAMP)] = ""


class ListShareLinkSummariesResponse(BaseModel):
    share_link_summaries: Annotated[List[ShareLinkSummary], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=ShareLinkSummary)] = Field(default_factory=list)
    next_page_token: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ListShareLinksRequest(BaseModel):
    page_size: Annotated[int, ProtoField(tag=1, wire=WireType.INT64)] = 0
    page_token: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    shared_with_me: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    conversation_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    response_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    order_by: Annotated[ListShareLinksOrderBy, ProtoField(tag=6, wire=WireType.INT32)] = ListShareLinksOrderBy.LIST_SHARE_LINKS_ORDER_BY_INVALID
    workspace_id: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""


class ShareLink(BaseModel):
    share_link_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    response_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    is_public: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    create_time: Annotated[str, ProtoField(tag=5, wire=WireType.TIMESTAMP)] = ""
    modify_time: Annotated[str, ProtoField(tag=6, wire=WireType.TIMESTAMP)] = ""
    team_id: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    shared_with_team: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False
    shared_with_user_ids: Annotated[List[str], ProtoField(tag=9, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    public_id: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    xai_user_id: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    shared_link: Annotated[Optional[GetShareLinkResponse], ProtoField(tag=12, wire=WireType.MESSAGE, cls=GetShareLinkResponse)] = None
    view_count: Annotated[int, ProtoField(tag=13, wire=WireType.INT64)] = 0


class ListShareLinksResponse(BaseModel):
    share_links: Annotated[List[ShareLink], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=ShareLink)] = Field(default_factory=list)
    next_page_token: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ListSharedMediaPostsRequest(BaseModel):
    limit: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    cursor: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class SharedMediaPostItem(BaseModel):
    post_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    thumbnail_image_url: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    prompt: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    view_count: Annotated[int, ProtoField(tag=4, wire=WireType.INT64)] = 0
    created_at: Annotated[int, ProtoField(tag=5, wire=WireType.INT64)] = 0


class ListSharedMediaPostsResponse(BaseModel):
    posts: Annotated[List[SharedMediaPostItem], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=SharedMediaPostItem)] = Field(default_factory=list)
    next_cursor: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ListSkillsRequest(BaseModel):
    locale: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class Skill(BaseModel):
    index: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    icon: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    display_name: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class ListSkillsResponse(BaseModel):
    skills: Annotated[List[Skill], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=Skill)] = Field(default_factory=list)


class ListSoftDeletedConversationsRequest(BaseModel):
    page_size: Annotated[int, ProtoField(tag=1, wire=WireType.INT64)] = 0
    page_token: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    workspace_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class ListSoftDeletedConversationsResponse(BaseModel):
    conversations: Annotated[List[Conversation], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=Conversation)] = Field(default_factory=list)
    next_page_token: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ListTopVoicesRequest(BaseModel):
    limit: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0


class TopVoiceEntry(BaseModel):
    voice: Annotated[Optional[VoiceMetadata], ProtoField(tag=1, wire=WireType.MESSAGE, cls=VoiceMetadata)] = None
    save_count: Annotated[int, ProtoField(tag=2, wire=WireType.INT64)] = 0


class ListTopVoicesResponse(BaseModel):
    voices: Annotated[List[TopVoiceEntry], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=TopVoiceEntry)] = Field(default_factory=list)


class SkillFileInfo(BaseModel):
    relative_path: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    size_bytes: Annotated[int, ProtoField(tag=2, wire=WireType.INT64)] = 0
    executable: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    content_type: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class UserSkillMetadata(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    enabled: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    total_bytes: Annotated[int, ProtoField(tag=4, wire=WireType.INT64)] = 0
    file_count: Annotated[int, ProtoField(tag=5, wire=WireType.INT32)] = 0
    files: Annotated[List[SkillFileInfo], ProtoField(tag=6, wire=WireType.REPEATED_MESSAGE, cls=SkillFileInfo)] = Field(default_factory=list)
    created_at: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    updated_at: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    upload_format: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    skill_md_content: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""


class ListUserSkillsResponse(BaseModel):
    skills: Annotated[List[UserSkillMetadata], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=UserSkillMetadata)] = Field(default_factory=list)


class ListVoiceShareLinksRequest(BaseModel):
    voice_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    limit: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class ListVoiceShareLinksResponse(BaseModel):
    links: Annotated[List[ShareLinkMetadata], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=ShareLinkMetadata)] = Field(default_factory=list)


class ListVoicesAdminRequest(BaseModel):
    visibility: Annotated[VoiceVisibility, ProtoField(tag=1, wire=WireType.INT32)] = VoiceVisibility.VOICE_VISIBILITY_UNSPECIFIED
    approved: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    query: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    limit: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    sort_by: Annotated[VoiceAdminSortBy, ProtoField(tag=6, wire=WireType.INT32)] = VoiceAdminSortBy.VOICE_ADMIN_SORT_BY_UNSPECIFIED


class ListVoicesAdminResponse(BaseModel):
    voices: Annotated[List[VoiceMetadata], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=VoiceMetadata)] = Field(default_factory=list)


class ListVoicesRequest(BaseModel):
    limit: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    cursor: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ListVoicesResponse(BaseModel):
    voices: Annotated[List[VoiceMetadata], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=VoiceMetadata)] = Field(default_factory=list)
    next_cursor: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class LoadResponsesRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    response_ids: Annotated[List[str], ProtoField(tag=2, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class LoadResponsesResponse(BaseModel):
    responses: Annotated[List[Response], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=Response)] = Field(default_factory=list)


class MediaSearchResult(BaseModel):
    post_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    root_post_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    media_type: Annotated[MediaPostType, ProtoField(tag=3, wire=WireType.INT32)] = MediaPostType.MEDIA_POST_TYPE_INVALID
    media_url: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    width: Annotated[int, ProtoField(tag=5, wire=WireType.INT32)] = 0
    height: Annotated[int, ProtoField(tag=6, wire=WireType.INT32)] = 0
    create_time: Annotated[str, ProtoField(tag=7, wire=WireType.TIMESTAMP)] = ""
    r_rated: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False
    duration: Annotated[float, ProtoField(tag=9, wire=WireType.FLOAT)] = 0.0
    result_type: Annotated[MediaSearchResultType, ProtoField(tag=10, wire=WireType.INT32)] = MediaSearchResultType.MEDIA_SEARCH_RESULT_TYPE_MEDIA_POST
    thumbnail_url: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""


class MemoryKeyMapping(BaseModel):
    x_user_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    x_conversation_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    xai_user_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    xai_conversation_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class MigratedConversation(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=3, wire=WireType.TIMESTAMP)] = ""
    modify_time: Annotated[str, ProtoField(tag=4, wire=WireType.TIMESTAMP)] = ""
    starred: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False
    system_prompt_name: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    is_x_shared: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False
    controller: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""


class MigrateConversationsRequest(BaseModel):
    conversations: Annotated[List[MigratedConversation], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=MigratedConversation)] = Field(default_factory=list)


class MigrateFileRequest(BaseModel):
    file_name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    file_mime_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    content: Annotated[bytes, ProtoField(tag=3, wire=WireType.BYTES_FIELD)] = b""
    is_model_generated: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False


class MigrateMemoryRequest(BaseModel):
    memory_key_mappings: Annotated[List[MemoryKeyMapping], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=MemoryKeyMapping)] = Field(default_factory=list)


class MigratedResponse(BaseModel):
    response_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    message: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    sender: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=5, wire=WireType.TIMESTAMP)] = ""
    parent_response_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    partial: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False
    query: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    query_type: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    web_search_results: Annotated[List[WebSearchResult], ProtoField(tag=10, wire=WireType.REPEATED_MESSAGE, cls=WebSearchResult)] = Field(default_factory=list)
    xpost_ids: Annotated[List[str], ProtoField(tag=11, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    generated_image_urls: Annotated[List[str], ProtoField(tag=12, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    image_attachments: Annotated[List[str], ProtoField(tag=13, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    file_attachments: Annotated[List[str], ProtoField(tag=14, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    card_attachments_json: Annotated[List[str], ProtoField(tag=15, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    thinking_trace: Annotated[str, ProtoField(tag=16, wire=WireType.STRING)] = ""
    steps: Annotated[List[ResponseStep], ProtoField(tag=17, wire=WireType.REPEATED_MESSAGE, cls=ResponseStep)] = Field(default_factory=list)
    image_edit_uri: Annotated[str, ProtoField(tag=18, wire=WireType.STRING)] = ""
    error: Annotated[str, ProtoField(tag=19, wire=WireType.STRING)] = ""
    webpage_urls: Annotated[List[str], ProtoField(tag=20, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    metadata: Annotated[dict, ProtoField(tag=21, wire=WireType.JSON_STRUCT)] = Field(default_factory=dict)
    cited_web_search_results: Annotated[List[WebSearchResult], ProtoField(tag=22, wire=WireType.REPEATED_MESSAGE, cls=WebSearchResult)] = Field(default_factory=list)
    memory_references: Annotated[List[MemoryReference], ProtoField(tag=23, wire=WireType.REPEATED_MESSAGE, cls=MemoryReference)] = Field(default_factory=list)
    ui_layout: Annotated[Optional[UiLayout], ProtoField(tag=24, wire=WireType.MESSAGE, cls=UiLayout)] = None
    rag_results: Annotated[List[RagResult], ProtoField(tag=25, wire=WireType.REPEATED_MESSAGE, cls=RagResult)] = Field(default_factory=list)
    cited_rag_results: Annotated[List[RagResult], ProtoField(tag=26, wire=WireType.REPEATED_MESSAGE, cls=RagResult)] = Field(default_factory=list)
    connector_search_results: Annotated[List[ConnectorSearchResultItem], ProtoField(tag=49, wire=WireType.REPEATED_MESSAGE, cls=ConnectorSearchResultItem)] = Field(default_factory=list)
    collection_search_results: Annotated[List[CollectionSearchResultItem], ProtoField(tag=50, wire=WireType.REPEATED_MESSAGE, cls=CollectionSearchResultItem)] = Field(default_factory=list)


class MigrateResponsesRequest(BaseModel):
    responses: Annotated[List[MigratedResponse], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=MigratedResponse)] = Field(default_factory=list)


class PartUploadUrl(BaseModel):
    part_number: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    url: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class MultipartUploadDetails(BaseModel):
    parts: Annotated[List[PartUploadUrl], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=PartUploadUrl)] = Field(default_factory=list)
    part_size: Annotated[int, ProtoField(tag=2, wire=WireType.INT64)] = 0


class OrganizationAdminControls(BaseModel):
    disable_personal_workspaces: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    disable_response_likes_dislikes: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    block_personal_usage_on_network: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False


class PatchCanvasNodeRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    position: Annotated[Optional[CanvasNodePosition], ProtoField(tag=2, wire=WireType.MESSAGE, cls=CanvasNodePosition)] = None
    scale: Annotated[float, ProtoField(tag=3, wire=WireType.DOUBLE)] = 0.0
    parent_node_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class PatchCanvasNodeResponse(BaseModel):
    pass


class PipelineInputField(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    text_value: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    image_url: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class PipelineStepProgress(BaseModel):
    step_name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    status: Annotated[PipelineStepStatus, ProtoField(tag=2, wire=WireType.INT32)] = PipelineStepStatus.PIPELINE_STEP_STATUS_PENDING
    progress_pct: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    retry_attempt: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    retry_max: Annotated[int, ProtoField(tag=5, wire=WireType.INT32)] = 0


class PostVoiceChatRecordingRequest(BaseModel):
    content_bytes: Annotated[bytes, ProtoField(tag=1, wire=WireType.BYTES_FIELD)] = b""
    mime_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    response_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    session_metadata: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    alignment_info: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class PostVoiceChatRecordingResponse(BaseModel):
    share_link_path: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    asset_url: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class PresignedCompletion(BaseModel):
    upload_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    completed_parts: Annotated[List[CompletedPartInfo], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=CompletedPartInfo)] = Field(default_factory=list)


class PublishPipelineTemplateRequest(BaseModel):
    template_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class PublishPipelineTemplateResponse(BaseModel):
    template: Annotated[Optional[PipelineTemplateProto], ProtoField(tag=1, wire=WireType.MESSAGE, cls=PipelineTemplateProto)] = None
    published_version: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class QuickAnswerSuggestion(BaseModel):
    text: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ReadResponseRequest(BaseModel):
    response_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    voice_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ReadResponseResponse(BaseModel):
    audio_chunk: Annotated[bytes, ProtoField(tag=1, wire=WireType.BYTES_FIELD)] = b""


class ReadUserSkillFileRequest(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    file_path: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ReadUserSkillFileResponse(BaseModel):
    content: Annotated[bytes, ProtoField(tag=1, wire=WireType.BYTES_FIELD)] = b""
    content_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    size_bytes: Annotated[int, ProtoField(tag=3, wire=WireType.INT64)] = 0


class ReconnectResponseRequest(BaseModel):
    response_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ReconnectResponseResponse(BaseModel):
    response: Annotated[Optional[AddResponseResponse], ProtoField(tag=1, wire=WireType.MESSAGE, cls=AddResponseResponse)] = None
    title: Annotated[Optional[GenerateTitleResponse], ProtoField(tag=2, wire=WireType.MESSAGE, cls=GenerateTitleResponse)] = None


class RegisterAttestationRequest(BaseModel):
    challenge: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    ios: Annotated[Optional[IosAppAttest], ProtoField(tag=2, wire=WireType.MESSAGE, cls=IosAppAttest)] = None
    android: Annotated[Optional[AndroidKeyAttest], ProtoField(tag=3, wire=WireType.MESSAGE, cls=AndroidKeyAttest)] = None


class RegisterAttestationResponse(BaseModel):
    pass


class RemoveFromGroupRequest(BaseModel):
    node_ids: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class RemoveFromGroupResponse(BaseModel):
    pass


class ResolveShareLinkRequest(BaseModel):
    share_token: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ResolveShareLinkResponse(BaseModel):
    link: Annotated[Optional[ShareLinkMetadata], ProtoField(tag=1, wire=WireType.MESSAGE, cls=ShareLinkMetadata)] = None
    voice: Annotated[Optional[VoiceMetadata], ProtoField(tag=2, wire=WireType.MESSAGE, cls=VoiceMetadata)] = None


class RestoreCanvasNodeRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class RestoreCanvasNodeResponse(BaseModel):
    pass


class RestoreSoftDeletedConversationRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ResumableUploadDetails(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    recommended_chunk_size: Annotated[int, ProtoField(tag=2, wire=WireType.INT64)] = 0


class ResumePipelineRequest(BaseModel):
    post_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class RevokeShareLinkRequest(BaseModel):
    share_token: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class RevokeShareLinkResponse(BaseModel):
    success: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False


class RevokeTookPermissionRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class RollbackPipelineTemplateRequest(BaseModel):
    template_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    target_version: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class RollbackPipelineTemplateResponse(BaseModel):
    template: Annotated[Optional[PipelineTemplateProto], ProtoField(tag=1, wire=WireType.MESSAGE, cls=PipelineTemplateProto)] = None


class RunCodeRequest(BaseModel):
    language: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    code: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class RunCodeResponse(BaseModel):
    success: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    stdout: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    stderr: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    output_files: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class RunTemplatePipelineRequest(BaseModel):
    template_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    inputs: Annotated[List[PipelineInputField], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=PipelineInputField)] = Field(default_factory=list)
    spec_json: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    redo_post_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    redo_appends_container: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False
    is_kids_mode: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False
    enable_nsfw: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = False


class RunTemplatePipelineResponse(BaseModel):
    post_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    pipeline_status: Annotated[MediaPostMediaStatus, ProtoField(tag=2, wire=WireType.INT32)] = MediaPostMediaStatus.MEDIA_POST_MEDIA_STATUS_INVALID
    steps: Annotated[List[PipelineStepProgress], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=PipelineStepProgress)] = Field(default_factory=list)
    overall_progress_pct: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    post: Annotated[Optional[MediaPost], ProtoField(tag=5, wire=WireType.MESSAGE, cls=MediaPost)] = None
    error_message: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class SaveVoiceRequest(BaseModel):
    voice_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    share_token: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class SaveVoiceResponse(BaseModel):
    success: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False


class SearchCompletionSuggestion(BaseModel):
    text: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class SearchMediaPostsRequest(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    limit: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    cursor: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    exclude_root_post_ids: Annotated[List[str], ProtoField(tag=4, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    root_post_ids: Annotated[List[str], ProtoField(tag=5, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    similar_to_post_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class SearchMediaPostsResponse(BaseModel):
    results: Annotated[List[MediaSearchResult], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=MediaSearchResult)] = Field(default_factory=list)
    next_cursor: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class SearchVoicesRequest(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    limit: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class SearchVoicesResponse(BaseModel):
    voices: Annotated[List[VoiceMetadata], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=VoiceMetadata)] = Field(default_factory=list)


class SetCanvasThumbnailRequest(BaseModel):
    canvas_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    image: Annotated[bytes, ProtoField(tag=2, wire=WireType.BYTES_FIELD)] = b""
    content_type: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class SetCanvasThumbnailResponse(BaseModel):
    thumbnail_url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class SetMediaPostVisibilityRequest(BaseModel):
    post_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    visibility: Annotated[MediaPostVisibility, ProtoField(tag=2, wire=WireType.INT32)] = MediaPostVisibility.MEDIA_POST_VISIBILITY_INVALID


class SetMediaPostVisibilityResponse(BaseModel):
    pass


class SetUserSettingsRequest(BaseModel):
    exclude_from_training: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    preferences: Annotated[object, ProtoField(tag=2, wire=WireType.JSON_VALUE)] = None
    allow_x_personalization: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    enable_memory: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    allow_share_indexing: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False
    allow_companion_notifications: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    allow_auto_share: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False
    agent_customizations_deprecated: Annotated[List[AgentCustomization], ProtoField(tag=8, wire=WireType.REPEATED_MESSAGE, cls=AgentCustomization)] = Field(default_factory=list)
    agent_customizations: Annotated[Optional[AgentCustomizations], ProtoField(tag=9, wire=WireType.MESSAGE, cls=AgentCustomizations)] = None
    allow_grok_finished_notification: Annotated[bool, ProtoField(tag=11, wire=WireType.BOOL)] = False


class SetUserSkillEnabledRequest(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    enabled: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class ShareArtifactRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    response_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    artifact_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    artifact_version_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class ShareArtifactResponse(BaseModel):
    shared_artifact_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ShareConversationRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    response_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    team_members_to_share: Annotated[List[str], ProtoField(tag=3, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    share_with_team_members: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    share_publicly: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False
    allow_indexing: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False


class ShareConversationResponse(BaseModel):
    share_link_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ShareVoiceChatRequest(BaseModel):
    video_bytes: Annotated[bytes, ProtoField(tag=1, wire=WireType.BYTES_FIELD)] = b""
    text: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ShortResponse(BaseModel):
    response_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    sender: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    message: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    parent_response_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    generated_image_urls: Annotated[List[str], ProtoField(tag=6, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    image_attachments: Annotated[List[str], ProtoField(tag=7, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    file_attachments: Annotated[List[str], ProtoField(tag=8, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    image_edit_uri: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    webpage_urls: Annotated[List[str], ProtoField(tag=10, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    metadata: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=12, wire=WireType.TIMESTAMP)] = ""
    selected_file_text_content: Annotated[str, ProtoField(tag=13, wire=WireType.STRING)] = ""
    selected_file_text_content_start_position: Annotated[int, ProtoField(tag=14, wire=WireType.INT32)] = 0
    selected_file_text_content_end_position: Annotated[int, ProtoField(tag=15, wire=WireType.INT32)] = 0
    thread_parent_id: Annotated[str, ProtoField(tag=16, wire=WireType.STRING)] = ""
    parent_quoted_text: Annotated[str, ProtoField(tag=17, wire=WireType.STRING)] = ""
    model: Annotated[str, ProtoField(tag=18, wire=WireType.STRING)] = ""
    card_attachments_json: Annotated[List[str], ProtoField(tag=19, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class SinglePutDetails(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    required_headers: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class SoftDeleteAllConversationsRequest(BaseModel):
    pass


class SoftDeleteConversationRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class SpeechToTextGenerateRequest(BaseModel):
    audio_base64: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    audio_format: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    max_tokens: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    enhance: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    history: Annotated[List[ChatMessageItem], ProtoField(tag=5, wire=WireType.REPEATED_MESSAGE, cls=ChatMessageItem)] = Field(default_factory=list)
    refinement_level: Annotated[RefinementLevel, ProtoField(tag=6, wire=WireType.INT32)] = RefinementLevel.REFINEMENT_LEVEL_UNSPECIFIED


class SpeechToTextGenerateResponse(BaseModel):
    text: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    sampling_time: Annotated[float, ProtoField(tag=2, wire=WireType.FLOAT)] = 0.0
    words: Annotated[List[WordScore], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=WordScore)] = Field(default_factory=list)
    language_code: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class StockSuggestion(BaseModel):
    data__f: Annotated[Optional[GetStockMiniSummaryResponse], ProtoField(tag=1, wire=WireType.MESSAGE, cls=GetStockMiniSummaryResponse)] = None


class StopConversationInflightResponsesRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class StopInflightResponseRequest(BaseModel):
    response_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class SuggestionChatMessage(BaseModel):
    role: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    content: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class StreamSuggestionsRequest(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    accepted_types: Annotated[List[AcceptedSuggestionType], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=AcceptedSuggestionType)] = Field(default_factory=list)
    conversation: Annotated[List[SuggestionChatMessage], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=SuggestionChatMessage)] = Field(default_factory=list)
    conversation_history: Annotated[List[ConversationHistorySummary], ProtoField(tag=4, wire=WireType.REPEATED_MESSAGE, cls=ConversationHistorySummary)] = Field(default_factory=list)


class StreamSuggestionsResponse(BaseModel):
    search_completion: Annotated[Optional[SearchCompletionSuggestion], ProtoField(tag=1, wire=WireType.MESSAGE, cls=SearchCompletionSuggestion)] = None
    stock: Annotated[Optional[StockSuggestion], ProtoField(tag=2, wire=WireType.MESSAGE, cls=StockSuggestion)] = None
    quick_answer: Annotated[Optional[QuickAnswerSuggestion], ProtoField(tag=3, wire=WireType.MESSAGE, cls=QuickAnswerSuggestion)] = None
    grok_completion: Annotated[Optional[GrokCompletionSuggestion], ProtoField(tag=4, wire=WireType.MESSAGE, cls=GrokCompletionSuggestion)] = None


class SubmitTidaReportRequest(BaseModel):
    content_belongs_to: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    reporter_email: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    signature: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    content_type: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    content_links: Annotated[List[str], ProtoField(tag=5, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    description: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    confirm_include_content_in_updates: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False
    confirm_private_info_report: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False
    confirm_accuracy_under_perjury: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = False
    reporter_account_name: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    reported_account_username: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=12, wire=WireType.STRING)] = ""
    response_id: Annotated[str, ProtoField(tag=13, wire=WireType.STRING)] = ""
    media_post_id: Annotated[str, ProtoField(tag=14, wire=WireType.STRING)] = ""
    media_url: Annotated[str, ProtoField(tag=15, wire=WireType.STRING)] = ""
    report_category: Annotated[str, ProtoField(tag=16, wire=WireType.STRING)] = ""
    verification_code: Annotated[str, ProtoField(tag=17, wire=WireType.STRING)] = ""
    report_source: Annotated[str, ProtoField(tag=18, wire=WireType.STRING)] = ""


class SubmitTidaReportResponse(BaseModel):
    report_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class TeamPublicSettings(BaseModel):
    allow_public_share: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False


class TextToSpeechV2Request(BaseModel):
    articles: Annotated[List[ArticleItem], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=ArticleItem)] = Field(default_factory=list)
    sanitize: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    voice: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    enable_alignment: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False


class ToolWithScope(BaseModel):
    scope: Annotated[ToolPermissionScope, ProtoField(tag=1, wire=WireType.INT32)] = ToolPermissionScope.TOOL_PERMISSION_SCOPE_UNSPECIFIED
    definition: Annotated[Optional[ToolDefinition], ProtoField(tag=2, wire=WireType.MESSAGE, cls=ToolDefinition)] = None


class TranscribeRequest(BaseModel):
    audio_b64: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    format_f: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    prefix: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    beam_size: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    patience: Annotated[float, ProtoField(tag=5, wire=WireType.FLOAT)] = 0.0
    batch_size: Annotated[int, ProtoField(tag=6, wire=WireType.INT32)] = 0


class TranscriptionSegment(BaseModel):
    start: Annotated[float, ProtoField(tag=1, wire=WireType.FLOAT)] = 0.0
    end: Annotated[float, ProtoField(tag=2, wire=WireType.FLOAT)] = 0.0
    words: Annotated[List[WordScore], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=WordScore)] = Field(default_factory=list)
    language_code: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class TranscribeResponse(BaseModel):
    segments: Annotated[List[TranscriptionSegment], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=TranscriptionSegment)] = Field(default_factory=list)


class TriggerMediaSearchIndexRequest(BaseModel):
    pass


class TriggerMediaSearchIndexResponse(BaseModel):
    status: Annotated[MediaSearchIndexStatus, ProtoField(tag=1, wire=WireType.INT32)] = MediaSearchIndexStatus.MEDIA_SEARCH_INDEX_STATUS_NOT_ELIGIBLE
    item_count: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class TtsMultipartChunk(BaseModel):
    data__f: Annotated[bytes, ProtoField(tag=1, wire=WireType.BYTES_FIELD)] = b""
    content_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class UnlikeMediaPostRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    folder_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class UnlikeMediaPostResponse(BaseModel):
    pass


class UnsaveVoiceRequest(BaseModel):
    voice_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class UnsaveVoiceResponse(BaseModel):
    success: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False


class UpdateArtifactInlineStatusRequest(BaseModel):
    artifact_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    artifact_version_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    inline_status: Annotated[ArtifactInlineStatusType, ProtoField(tag=3, wire=WireType.INT32)] = ArtifactInlineStatusType.DEFAULT_ARTIFACT_INLINE_STATUS


class UpdateArtifactInlineStatusResponse(BaseModel):
    artifact_version_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class UpdateArtifactRequest(BaseModel):
    artifact_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    full_artifact: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    artifact_diff: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    artifact_version_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class UpdateArtifactResponse(BaseModel):
    artifact_version_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class UpdateCanvasDocumentRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    sort_order: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    metadata: Annotated[dict, ProtoField(tag=4, wire=WireType.JSON_STRUCT)] = Field(default_factory=dict)


class UpdateCanvasDocumentResponse(BaseModel):
    document: Annotated[Optional[CanvasDocument], ProtoField(tag=1, wire=WireType.MESSAGE, cls=CanvasDocument)] = None


class UpdateCanvasNodeRequest(BaseModel):
    node: Annotated[Optional[CanvasNode], ProtoField(tag=1, wire=WireType.MESSAGE, cls=CanvasNode)] = None


class UpdateCanvasNodeResponse(BaseModel):
    node: Annotated[Optional[CanvasNode], ProtoField(tag=1, wire=WireType.MESSAGE, cls=CanvasNode)] = None


class UpdateConversationRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    starred: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False


class UpdateFeatureControlsRequest(BaseModel):
    team_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    features: Annotated[Optional[FeatureControls], ProtoField(tag=2, wire=WireType.MESSAGE, cls=FeatureControls)] = None
    update_mask: Annotated[List[str], ProtoField(tag=3, wire=WireType.FIELD_MASK)] = Field(default_factory=list)


class UpdateMediaFolderRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class UpdateMediaFolderResponse(BaseModel):
    folder: Annotated[Optional[MediaFolder], ProtoField(tag=1, wire=WireType.MESSAGE, cls=MediaFolder)] = None


class UpdateMediaProjectRequest(BaseModel):
    project: Annotated[Optional[MediaProject], ProtoField(tag=1, wire=WireType.MESSAGE, cls=MediaProject)] = None


class UpdateMediaProjectResponse(BaseModel):
    project: Annotated[Optional[MediaProject], ProtoField(tag=1, wire=WireType.MESSAGE, cls=MediaProject)] = None


class UpdateOrganizationAdminControlsRequest(BaseModel):
    controls: Annotated[Optional[OrganizationAdminControls], ProtoField(tag=1, wire=WireType.MESSAGE, cls=OrganizationAdminControls)] = None
    update_mask: Annotated[List[str], ProtoField(tag=2, wire=WireType.FIELD_MASK)] = Field(default_factory=list)


class UpdatePipelineTemplateRequest(BaseModel):
    template_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    thumbnail_url: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    preview_url: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    spec_json: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    is_featured: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = False
    sort_order: Annotated[int, ProtoField(tag=10, wire=WireType.INT32)] = 0
    anonymous: Annotated[bool, ProtoField(tag=11, wire=WireType.BOOL)] = False


class UpdatePipelineTemplateResponse(BaseModel):
    template: Annotated[Optional[PipelineTemplateProto], ProtoField(tag=1, wire=WireType.MESSAGE, cls=PipelineTemplateProto)] = None


class UpdateUserMemoryBlurbRequest(BaseModel):
    memory_content: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class UpdateUserMemoryBlurbResponse(BaseModel):
    memory_content: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class UpdateVoicePersonalityRequest(BaseModel):
    voice_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    personality_preset_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    personality_custom_prompt: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class UpdateVoicePersonalityResponse(BaseModel):
    metadata: Annotated[Optional[VoiceMetadata], ProtoField(tag=1, wire=WireType.MESSAGE, cls=VoiceMetadata)] = None


class UpdateVoiceVisibilityRequest(BaseModel):
    voice_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    visibility: Annotated[VoiceVisibility, ProtoField(tag=2, wire=WireType.INT32)] = VoiceVisibility.VOICE_VISIBILITY_UNSPECIFIED


class UpdateVoiceVisibilityResponse(BaseModel):
    metadata: Annotated[Optional[VoiceMetadata], ProtoField(tag=1, wire=WireType.MESSAGE, cls=VoiceMetadata)] = None


class UploadFileCompleteRequest(BaseModel):
    presigned: Annotated[Optional[PresignedCompletion], ProtoField(tag=1, wire=WireType.MESSAGE, cls=PresignedCompletion)] = None
    direct_upload: Annotated[Optional[DirectUploadData], ProtoField(tag=2, wire=WireType.MESSAGE, cls=DirectUploadData)] = None


class UploadFileCompleteResponse(BaseModel):
    upload_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    file_metadata: Annotated[Optional[FileMetadata], ProtoField(tag=2, wire=WireType.MESSAGE, cls=FileMetadata)] = None
    terminal_error: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class UploadFileInitRequest(BaseModel):
    file_name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    file_mime_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    file_source: Annotated[UploadedFileSourceType, ProtoField(tag=3, wire=WireType.INT32)] = UploadedFileSourceType.SELF_UPLOAD_FILE_SOURCE
    third_party_file_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    size_bytes: Annotated[int, ProtoField(tag=5, wire=WireType.INT64)] = 0
    resumable_supported: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    multipart_supported: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False


class UploadFileInitResponse(BaseModel):
    upload_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    asset_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    expires_at: Annotated[str, ProtoField(tag=3, wire=WireType.TIMESTAMP)] = ""
    upload_method: Annotated[UploadMethod, ProtoField(tag=4, wire=WireType.INT32)] = UploadMethod.UPLOAD_METHOD_UNSPECIFIED
    single_put: Annotated[Optional[SinglePutDetails], ProtoField(tag=5, wire=WireType.MESSAGE, cls=SinglePutDetails)] = None
    resumable: Annotated[Optional[ResumableUploadDetails], ProtoField(tag=6, wire=WireType.MESSAGE, cls=ResumableUploadDetails)] = None
    multipart: Annotated[Optional[MultipartUploadDetails], ProtoField(tag=7, wire=WireType.MESSAGE, cls=MultipartUploadDetails)] = None


class UploadFilePatchRequest(BaseModel):
    upload_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    completed_parts: Annotated[List[CompletedPartInfo], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=CompletedPartInfo)] = Field(default_factory=list)


class UploadFileRequest(BaseModel):
    file_name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    file_mime_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    content: Annotated[bytes, ProtoField(tag=3, wire=WireType.BYTES_FIELD)] = b""
    make_public: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    file_source: Annotated[UploadedFileSourceType, ProtoField(tag=5, wire=WireType.INT32)] = UploadedFileSourceType.SELF_UPLOAD_FILE_SOURCE
    third_party_file_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    workspace_id: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""


class UploadUserSkillRequest(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    filename: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    content: Annotated[bytes, ProtoField(tag=3, wire=WireType.BYTES_FIELD)] = b""


class UpscaleVideoRequest(BaseModel):
    video_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    target_resolution: Annotated[UpscaleTargetResolution, ProtoField(tag=2, wire=WireType.INT32)] = UpscaleTargetResolution.UPSCALE_TARGET_RESOLUTION_HD


class UpscaleVideoResponse(BaseModel):
    hd_media_url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class UsageLimitExhaustedDetails(BaseModel):
    reset_time: Annotated[str, ProtoField(tag=1, wire=WireType.TIMESTAMP)] = ""
    period_type: Annotated[UsagePeriodType, ProtoField(tag=2, wire=WireType.INT32)] = UsagePeriodType.USAGE_PERIOD_TYPE_UNSPECIFIED
    is_top_up_available: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    upgrade_tier: Annotated[UsageUpgradeTier, ProtoField(tag=4, wire=WireType.INT32)] = UsageUpgradeTier.USAGE_UPGRADE_TIER_UNSPECIFIED


class UserIssueReportRequest(BaseModel):
    reportJSONString: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    reportWithDumpJSONString: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    report: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    feedback_type: Annotated[UserFeedbackType, ProtoField(tag=4, wire=WireType.INT32)] = UserFeedbackType.general_feedback
    attachments: Annotated[List[FeedbackAttachment], ProtoField(tag=5, wire=WireType.REPEATED_MESSAGE, cls=FeedbackAttachment)] = Field(default_factory=list)


class UserSettings(BaseModel):
    exclude_from_training: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    preferences: Annotated[object, ProtoField(tag=2, wire=WireType.JSON_VALUE)] = None
    allow_x_personalization: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    enable_memory: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    allow_share_indexing: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False
    allow_companion_notifications: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    allow_auto_share: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False
    agent_customizations: Annotated[List[AgentCustomization], ProtoField(tag=8, wire=WireType.REPEATED_MESSAGE, cls=AgentCustomization)] = Field(default_factory=list)
    allow_grok_finished_notification: Annotated[bool, ProtoField(tag=10, wire=WireType.BOOL)] = False


class VerifyPassphraseRequest(BaseModel):
    passphrase_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    passphrase_audio_b64: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    passphrase_audio_format: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    reference_audio_b64: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    reference_audio_format: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class VerifyPassphraseResponse(BaseModel):
    success: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    similarity_score: Annotated[float, ProtoField(tag=2, wire=WireType.FLOAT)] = 0.0


class FreeTrialDetails(BaseModel):
    trial_days: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0


class DiscountDetails(BaseModel):
    percentage_off: Annotated[float, ProtoField(tag=1, wire=WireType.FLOAT)] = 0.0
    duration_months: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class PayUpfrontDetails(BaseModel):
    months_paid: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    months_free: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    percentage_off: Annotated[float, ProtoField(tag=3, wire=WireType.FLOAT)] = 0.0


class ActiveOffer(BaseModel):
    type_f: Annotated[ActiveOfferType, ProtoField(tag=1, wire=WireType.INT32)] = ActiveOfferType.ACTIVE_OFFER_TYPE_UNSPECIFIED
    purpose: Annotated[OfferPurpose, ProtoField(tag=2, wire=WireType.INT32)] = OfferPurpose.OFFER_PURPOSE_UNSPECIFIED
    campaign_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    offer_start: Annotated[bytes, ProtoField(tag=4, wire=WireType.BYTES_FIELD)] = b""
    offer_end: Annotated[bytes, ProtoField(tag=5, wire=WireType.BYTES_FIELD)] = b""
    provider_offer_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    free_trial: Annotated[Optional[FreeTrialDetails], ProtoField(tag=10, wire=WireType.MESSAGE, cls=FreeTrialDetails)] = None
    discount: Annotated[Optional[DiscountDetails], ProtoField(tag=11, wire=WireType.MESSAGE, cls=DiscountDetails)] = None
    pay_upfront: Annotated[Optional[PayUpfrontDetails], ProtoField(tag=12, wire=WireType.MESSAGE, cls=PayUpfrontDetails)] = None


class AddAssetRequest(BaseModel):
    workspace_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    asset_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class AddConversationRequest(BaseModel):
    workspace_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class CreateTaskScheduleRequest(BaseModel):
    task_cadence: Annotated[TaskCadence, ProtoField(tag=2, wire=WireType.INT32)] = TaskCadence.TASK_CADENCE_ONCE
    is_enabled: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    iso_utc_schedule: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    timezone: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    time_of_day: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    day_of_week: Annotated[int, ProtoField(tag=7, wire=WireType.INT32)] = 0
    day_of_month: Annotated[int, ProtoField(tag=8, wire=WireType.INT32)] = 0
    day_of_year: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""


class AddTaskScheduleToTaskRequest(BaseModel):
    task_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    schedule: Annotated[Optional[CreateTaskScheduleRequest], ProtoField(tag=2, wire=WireType.MESSAGE, cls=CreateTaskScheduleRequest)] = None


class AppleLapsedPayment(BaseModel):
    original_transaction_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ArchiveTaskRequest(BaseModel):
    task_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    is_enabled: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False


class AssetMetadata(BaseModel):
    asset_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    mime_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    size_bytes: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    create_time: Annotated[str, ProtoField(tag=5, wire=WireType.TIMESTAMP)] = ""
    last_use_time: Annotated[str, ProtoField(tag=6, wire=WireType.TIMESTAMP)] = ""
    summary: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    preview_image_key: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    key: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    aux_keys: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    response_id: Annotated[str, ProtoField(tag=12, wire=WireType.STRING)] = ""
    source: Annotated[AssetSource, ProtoField(tag=13, wire=WireType.INT32)] = AssetSource.SOURCE_ANY
    is_deleted: Annotated[bool, ProtoField(tag=14, wire=WireType.BOOL)] = False
    file_source: Annotated[UploadedFileSourceType, ProtoField(tag=15, wire=WireType.INT32)] = UploadedFileSourceType.SELF_UPLOAD_FILE_SOURCE
    third_party_file_id: Annotated[str, ProtoField(tag=16, wire=WireType.STRING)] = ""
    third_party_file_mime_type: Annotated[str, ProtoField(tag=17, wire=WireType.STRING)] = ""
    current_conversation_id: Annotated[str, ProtoField(tag=18, wire=WireType.STRING)] = ""
    root_asset_id: Annotated[str, ProtoField(tag=19, wire=WireType.STRING)] = ""
    source_conversation_id: Annotated[str, ProtoField(tag=20, wire=WireType.STRING)] = ""
    asset_diff: Annotated[str, ProtoField(tag=21, wire=WireType.STRING)] = ""
    is_model_generated: Annotated[bool, ProtoField(tag=22, wire=WireType.BOOL)] = False
    update_time: Annotated[str, ProtoField(tag=23, wire=WireType.TIMESTAMP)] = ""
    is_latest: Annotated[bool, ProtoField(tag=24, wire=WireType.BOOL)] = False
    inline_status: Annotated[ArtifactInlineStatusType, ProtoField(tag=25, wire=WireType.INT32)] = ArtifactInlineStatusType.DEFAULT_ARTIFACT_INLINE_STATUS
    is_root_asset_created_by_model: Annotated[bool, ProtoField(tag=26, wire=WireType.BOOL)] = False
    root_asset_source_conversation_id: Annotated[str, ProtoField(tag=27, wire=WireType.STRING)] = ""
    workspace_sharing_key: Annotated[str, ProtoField(tag=28, wire=WireType.STRING)] = ""
    workspace_sharing_preview_image_key: Annotated[str, ProtoField(tag=29, wire=WireType.STRING)] = ""
    team_id: Annotated[str, ProtoField(tag=30, wire=WireType.STRING)] = ""
    shared_with_team: Annotated[bool, ProtoField(tag=31, wire=WireType.BOOL)] = False
    shared_with_user_ids: Annotated[List[str], ProtoField(tag=32, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    hd_key: Annotated[str, ProtoField(tag=37, wire=WireType.STRING)] = ""
    hd_1080_key: Annotated[str, ProtoField(tag=38, wire=WireType.STRING)] = ""


class AutoTopupRule(BaseModel):
    enabled: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    min_before_hitting_sl: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    topup_amount: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    max_amount_per_month: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class BatchSetIsReadForTaskResultRequest(BaseModel):
    task_result_ids: Annotated[List[str], ProtoField(tag=1, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    value__f: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class BillingCycle(BaseModel):
    year: Annotated[int, ProtoField(tag=1, wire=WireType.INT32)] = 0
    month: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class BillingPeriodUsage(BaseModel):
    billing_cycle: Annotated[Optional[BillingCycle], ProtoField(tag=1, wire=WireType.MESSAGE, cls=BillingCycle)] = None
    included_used: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    on_demand_used: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    total_used: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class CheckPaymentSetupFinalizedResponse(BaseModel):
    has_billing_info: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    has_payment_method: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class CloneAssetRequest(BaseModel):
    asset_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class Content(BaseModel):
    text: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    asset: Annotated[Optional[AssetMetadata], ProtoField(tag=2, wire=WireType.MESSAGE, cls=AssetMetadata)] = None


class ContentRequest(BaseModel):
    text: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    asset_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class CreateAssetRequest(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    mime_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    content: Annotated[bytes, ProtoField(tag=3, wire=WireType.BYTES_FIELD)] = b""
    make_public: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    file_source: Annotated[UploadedFileSourceType, ProtoField(tag=5, wire=WireType.INT32)] = UploadedFileSourceType.SELF_UPLOAD_FILE_SOURCE
    third_party_file_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    third_party_file_mime_type: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    asset_id: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    root_asset_id: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    current_conversation_id: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    source_conversation_id: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    asset_diff: Annotated[str, ProtoField(tag=12, wire=WireType.STRING)] = ""
    is_model_generated: Annotated[bool, ProtoField(tag=13, wire=WireType.BOOL)] = False
    response_id: Annotated[str, ProtoField(tag=14, wire=WireType.STRING)] = ""
    update_time: Annotated[str, ProtoField(tag=15, wire=WireType.TIMESTAMP)] = ""
    should_generate_name: Annotated[bool, ProtoField(tag=16, wire=WireType.BOOL)] = False


class PortalSessionFlowDataFlowDataAfterCompletionHostedConfirmation(BaseModel):
    custom_message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class HostedConfirmation(BaseModel):
    custom_message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class PortalSessionFlowDataFlowDataAfterCompletionRedirectToUrl(BaseModel):
    return_url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class RedirectToUrl(BaseModel):
    return_url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class PortalSessionFlowDataFlowDataAfterCompletion(BaseModel):
    type_f: Annotated[AfterCompletionType, ProtoField(tag=1, wire=WireType.INT32)] = AfterCompletionType.hosted_confirmation
    hosted_confirmation: Annotated[Optional[PortalSessionFlowDataFlowDataAfterCompletionHostedConfirmation], ProtoField(tag=2, wire=WireType.MESSAGE, cls=PortalSessionFlowDataFlowDataAfterCompletionHostedConfirmation)] = None
    redirect: Annotated[Optional[PortalSessionFlowDataFlowDataAfterCompletionRedirectToUrl], ProtoField(tag=3, wire=WireType.MESSAGE, cls=PortalSessionFlowDataFlowDataAfterCompletionRedirectToUrl)] = None


class FlowDataAfterCompletion(BaseModel):
    type_f: Annotated[AfterCompletionType, ProtoField(tag=1, wire=WireType.INT32)] = AfterCompletionType.hosted_confirmation
    hosted_confirmation: Annotated[Optional[PortalSessionFlowDataFlowDataAfterCompletionHostedConfirmation], ProtoField(tag=2, wire=WireType.MESSAGE, cls=PortalSessionFlowDataFlowDataAfterCompletionHostedConfirmation)] = None
    redirect: Annotated[Optional[PortalSessionFlowDataFlowDataAfterCompletionRedirectToUrl], ProtoField(tag=3, wire=WireType.MESSAGE, cls=PortalSessionFlowDataFlowDataAfterCompletionRedirectToUrl)] = None


class PortalSessionFlowDataFlowDataSubscriptionCancelRetentionCouponOffer(BaseModel):
    coupon: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class CouponOffer(BaseModel):
    coupon: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class PortalSessionFlowDataFlowDataSubscriptionCancelRetention(BaseModel):
    coupon_offer: Annotated[Optional[PortalSessionFlowDataFlowDataSubscriptionCancelRetentionCouponOffer], ProtoField(tag=1, wire=WireType.MESSAGE, cls=PortalSessionFlowDataFlowDataSubscriptionCancelRetentionCouponOffer)] = None


class Retention(BaseModel):
    coupon_offer: Annotated[Optional[PortalSessionFlowDataFlowDataSubscriptionCancelRetentionCouponOffer], ProtoField(tag=1, wire=WireType.MESSAGE, cls=PortalSessionFlowDataFlowDataSubscriptionCancelRetentionCouponOffer)] = None


class PortalSessionFlowDataFlowDataSubscriptionCancel(BaseModel):
    subscription: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    retention: Annotated[Optional[PortalSessionFlowDataFlowDataSubscriptionCancelRetention], ProtoField(tag=2, wire=WireType.MESSAGE, cls=PortalSessionFlowDataFlowDataSubscriptionCancelRetention)] = None


class FlowDataSubscriptionCancel(BaseModel):
    subscription: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    retention: Annotated[Optional[PortalSessionFlowDataFlowDataSubscriptionCancelRetention], ProtoField(tag=2, wire=WireType.MESSAGE, cls=PortalSessionFlowDataFlowDataSubscriptionCancelRetention)] = None


class PortalSessionFlowDataFlowDataSubscriptionUpdate(BaseModel):
    subscription: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class FlowDataSubscriptionUpdate(BaseModel):
    subscription: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class PortalSessionFlowData(BaseModel):
    type_f: Annotated[BillingPortalFlowType, ProtoField(tag=1, wire=WireType.INT32)] = BillingPortalFlowType.payment_method_update
    after_completion: Annotated[Optional[PortalSessionFlowDataFlowDataAfterCompletion], ProtoField(tag=2, wire=WireType.MESSAGE, cls=PortalSessionFlowDataFlowDataAfterCompletion)] = None
    subscription_cancel: Annotated[Optional[PortalSessionFlowDataFlowDataSubscriptionCancel], ProtoField(tag=3, wire=WireType.MESSAGE, cls=PortalSessionFlowDataFlowDataSubscriptionCancel)] = None
    subscription_update: Annotated[Optional[PortalSessionFlowDataFlowDataSubscriptionUpdate], ProtoField(tag=4, wire=WireType.MESSAGE, cls=PortalSessionFlowDataFlowDataSubscriptionUpdate)] = None


class CreateBillingPortalSessionRequest(BaseModel):
    configuration: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    flow_data: Annotated[Optional[PortalSessionFlowData], ProtoField(tag=2, wire=WireType.MESSAGE, cls=PortalSessionFlowData)] = None
    return_url: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class CreateBillingPortalSessionResponse(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class CreateStripeCustomerRequest(BaseModel):
    billing_info: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class CreateStripeCustomerResponse(BaseModel):
    pass


class CreateSystemPromptRequest(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    content: Annotated[List[ContentRequest], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=ContentRequest)] = Field(default_factory=list)


class CreateTaskRequest(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    prompt: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    metadata_json_string: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    schedule: Annotated[Optional[CreateTaskScheduleRequest], ProtoField(tag=4, wire=WireType.MESSAGE, cls=CreateTaskScheduleRequest)] = None
    notification_method: Annotated[NotificationUiOption, ProtoField(tag=5, wire=WireType.INT32)] = NotificationUiOption.DEFAULT
    model_mode: Annotated[ModelMode, ProtoField(tag=6, wire=WireType.INT32)] = ModelMode.BASE
    notification_decider_enable: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False
    notification_decider_guideline: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    model_name: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    response_id: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    toolset: Annotated[List[str], ProtoField(tag=11, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class CreateWorkspaceRequest(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    icon: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    custom_personality: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class DeleteAssetRequest(BaseModel):
    asset_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class DeleteSystemPromptRequest(BaseModel):
    system_prompt_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class DeleteWorkspaceRequest(BaseModel):
    workspace_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class File(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    path: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    is_directory: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    size: Annotated[int, ProtoField(tag=4, wire=WireType.INT64)] = 0
    mime_type: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    modified_at: Annotated[str, ProtoField(tag=6, wire=WireType.TIMESTAMP)] = ""


class GetAssetMetadataRequest(BaseModel):
    asset_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetAutoTopupRuleResponse(BaseModel):
    rule: Annotated[Optional[AutoTopupRule], ProtoField(tag=1, wire=WireType.MESSAGE, cls=AutoTopupRule)] = None


class GetAutoTopupStatsResponse(BaseModel):
    curr_num_of_topups_in_24_hours: Annotated[int, ProtoField(tag=1, wire=WireType.INT64)] = 0
    max_num_of_topups_in_24_hours: Annotated[int, ProtoField(tag=2, wire=WireType.INT64)] = 0
    amount_topped_up_this_bp: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class GetFileContentRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    path: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    share_link_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    is_download: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False


class GetFileContentResponse(BaseModel):
    data_url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    mime_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    size: Annotated[int, ProtoField(tag=3, wire=WireType.INT64)] = 0
    is_truncated: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    signed_url: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    download_signed_url: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class GetGoogleObfuscatedIdRequest(BaseModel):
    pass


class SubscriptionProviderGoogle(BaseModel):
    purchase_token: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    product_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    base_plan_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    expiry_time: Annotated[str, ProtoField(tag=4, wire=WireType.TIMESTAMP)] = ""
    auto_renew_enabled: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False


class SubscriptionProviderApple(BaseModel):
    txid: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    original_txid: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    bundle_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    product_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    auto_renew_on: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False


class SubscriptionProviderStripe(BaseModel):
    subscription_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    invoice_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    product_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    current_period_end: Annotated[bytes, ProtoField(tag=4, wire=WireType.BYTES_FIELD)] = b""
    cancel_at_period_end: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False
    subscription_type: Annotated[SubscriptionType, ProtoField(tag=6, wire=WireType.INT32)] = SubscriptionType.MONTHLY


class SubscriptionProviderX(BaseModel):
    pass


class SubscriptionProviderEnterprise(BaseModel):
    team_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    subscription_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class LapsedPaymentInGracePeriod(BaseModel):
    grace_period_end: Annotated[bytes, ProtoField(tag=1, wire=WireType.BYTES_FIELD)] = b""


class LapsedPaymentOnHold(BaseModel):
    suspended_at: Annotated[str, ProtoField(tag=1, wire=WireType.TIMESTAMP)] = ""


class StripeLapsedPayment(BaseModel):
    subscription_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    stripe_status: Annotated[StripeSubscriptionStatus, ProtoField(tag=2, wire=WireType.INT32)] = StripeSubscriptionStatus.STRIPE_SUBSCRIPTION_STATUS_UNKNOWN


class GoogleLapsedPayment(BaseModel):
    product_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class LapsedPaymentInfo(BaseModel):
    in_grace_period: Annotated[Optional[LapsedPaymentInGracePeriod], ProtoField(tag=1, wire=WireType.MESSAGE, cls=LapsedPaymentInGracePeriod)] = None
    on_hold: Annotated[Optional[LapsedPaymentOnHold], ProtoField(tag=2, wire=WireType.MESSAGE, cls=LapsedPaymentOnHold)] = None
    stripe: Annotated[Optional[StripeLapsedPayment], ProtoField(tag=10, wire=WireType.MESSAGE, cls=StripeLapsedPayment)] = None
    apple: Annotated[Optional[AppleLapsedPayment], ProtoField(tag=11, wire=WireType.MESSAGE, cls=AppleLapsedPayment)] = None
    google: Annotated[Optional[GoogleLapsedPayment], ProtoField(tag=12, wire=WireType.MESSAGE, cls=GoogleLapsedPayment)] = None


class SubscriptionProviderAdHoc(BaseModel):
    product_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class SubscriptionProviderEapi(BaseModel):
    product_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class SubscriptionProviderPaypal(BaseModel):
    subscription_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    plan_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class SubscriptionProviderBraintree(BaseModel):
    subscription_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    plan_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ScheduledChange(BaseModel):
    type_f: Annotated[ScheduledChangeType, ProtoField(tag=1, wire=WireType.INT32)] = ScheduledChangeType.SCHEDULED_CHANGE_TYPE_UNSPECIFIED
    target_tier: Annotated[SubscriptionTier, ProtoField(tag=2, wire=WireType.INT32)] = SubscriptionTier.SUBSCRIPTION_TIER_INVALID
    target_interval: Annotated[BillingInterval, ProtoField(tag=3, wire=WireType.INT32)] = BillingInterval.BILLING_INTERVAL_UNKNOWN


class Subscription(BaseModel):
    google: Annotated[Optional[SubscriptionProviderGoogle], ProtoField(tag=1, wire=WireType.MESSAGE, cls=SubscriptionProviderGoogle)] = None
    apple: Annotated[Optional[SubscriptionProviderApple], ProtoField(tag=2, wire=WireType.MESSAGE, cls=SubscriptionProviderApple)] = None
    stripe: Annotated[Optional[SubscriptionProviderStripe], ProtoField(tag=3, wire=WireType.MESSAGE, cls=SubscriptionProviderStripe)] = None
    x: Annotated[Optional[SubscriptionProviderX], ProtoField(tag=4, wire=WireType.MESSAGE, cls=SubscriptionProviderX)] = None
    tier: Annotated[SubscriptionTier, ProtoField(tag=5, wire=WireType.INT32)] = SubscriptionTier.SUBSCRIPTION_TIER_INVALID
    status: Annotated[SubscriptionStatus, ProtoField(tag=6, wire=WireType.INT32)] = SubscriptionStatus.SUBSCRIPTION_STATUS_INVALID
    create_time: Annotated[str, ProtoField(tag=7, wire=WireType.TIMESTAMP)] = ""
    mod_time: Annotated[str, ProtoField(tag=8, wire=WireType.TIMESTAMP)] = ""
    xai_user_id: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    enterprise: Annotated[Optional[SubscriptionProviderEnterprise], ProtoField(tag=10, wire=WireType.MESSAGE, cls=SubscriptionProviderEnterprise)] = None
    lapsed_payment_info: Annotated[Optional[LapsedPaymentInfo], ProtoField(tag=11, wire=WireType.MESSAGE, cls=LapsedPaymentInfo)] = None
    adhoc: Annotated[Optional[SubscriptionProviderAdHoc], ProtoField(tag=20, wire=WireType.MESSAGE, cls=SubscriptionProviderAdHoc)] = None
    eapi: Annotated[Optional[SubscriptionProviderEapi], ProtoField(tag=21, wire=WireType.MESSAGE, cls=SubscriptionProviderEapi)] = None
    paypal: Annotated[Optional[SubscriptionProviderPaypal], ProtoField(tag=22, wire=WireType.MESSAGE, cls=SubscriptionProviderPaypal)] = None
    braintree: Annotated[Optional[SubscriptionProviderBraintree], ProtoField(tag=23, wire=WireType.MESSAGE, cls=SubscriptionProviderBraintree)] = None
    billing_interval: Annotated[BillingInterval, ProtoField(tag=30, wire=WireType.INT32)] = BillingInterval.BILLING_INTERVAL_UNKNOWN
    billing_period_end: Annotated[bytes, ProtoField(tag=32, wire=WireType.BYTES_FIELD)] = b""
    cancel_at_period_end: Annotated[bool, ProtoField(tag=33, wire=WireType.BOOL)] = False
    scheduled_change: Annotated[Optional[ScheduledChange], ProtoField(tag=34, wire=WireType.MESSAGE, cls=ScheduledChange)] = None
    active_offer: Annotated[Optional[ActiveOffer], ProtoField(tag=35, wire=WireType.MESSAGE, cls=ActiveOffer)] = None
    future_offers: Annotated[List[ActiveOffer], ProtoField(tag=36, wire=WireType.REPEATED_MESSAGE, cls=ActiveOffer)] = Field(default_factory=list)


class SubscriptionList(BaseModel):
    subscriptions: Annotated[List[Subscription], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=Subscription)] = Field(default_factory=list)


class GetGoogleObfuscatedIdResponse(BaseModel):
    obfuscated_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    existing_active_subscriptions: Annotated[Optional[SubscriptionList], ProtoField(tag=2, wire=WireType.MESSAGE, cls=SubscriptionList)] = None


class GrokBuildBillingConfig(BaseModel):
    monthly_limit: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    used: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    on_demand_cap: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    billing_period_start: Annotated[bytes, ProtoField(tag=4, wire=WireType.BYTES_FIELD)] = b""
    billing_period_end: Annotated[bytes, ProtoField(tag=5, wire=WireType.BYTES_FIELD)] = b""
    history: Annotated[List[BillingPeriodUsage], ProtoField(tag=6, wire=WireType.REPEATED_MESSAGE, cls=BillingPeriodUsage)] = Field(default_factory=list)


class GetGrokBuildBillingConfigResponse(BaseModel):
    config: Annotated[Optional[GrokBuildBillingConfig], ProtoField(tag=1, wire=WireType.MESSAGE, cls=GrokBuildBillingConfig)] = None


class GetGrokCreatedTasksByConversationIdRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class UsagePeriod(BaseModel):
    type_f: Annotated[UsagePeriodType, ProtoField(tag=1, wire=WireType.INT32)] = UsagePeriodType.USAGE_PERIOD_TYPE_UNSPECIFIED
    start: Annotated[bytes, ProtoField(tag=2, wire=WireType.BYTES_FIELD)] = b""
    end: Annotated[bytes, ProtoField(tag=3, wire=WireType.BYTES_FIELD)] = b""


class PeriodUsage(BaseModel):
    billing_cycle: Annotated[Optional[BillingCycle], ProtoField(tag=1, wire=WireType.MESSAGE, cls=BillingCycle)] = None
    on_demand_used: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    period: Annotated[Optional[UsagePeriod], ProtoField(tag=3, wire=WireType.MESSAGE, cls=UsagePeriod)] = None


class ProductUsage(BaseModel):
    product: Annotated[Optional[Product], ProtoField(tag=1, wire=WireType.MESSAGE, cls=Product)] = None
    usage_percent: Annotated[float, ProtoField(tag=2, wire=WireType.FLOAT)] = 0.0


class GrokCreditsConfig(BaseModel):
    credit_usage_percent: Annotated[float, ProtoField(tag=1, wire=WireType.FLOAT)] = 0.0
    on_demand_cap: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    on_demand_used: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    billing_period_start: Annotated[bytes, ProtoField(tag=4, wire=WireType.BYTES_FIELD)] = b""
    billing_period_end: Annotated[bytes, ProtoField(tag=5, wire=WireType.BYTES_FIELD)] = b""
    history: Annotated[List[PeriodUsage], ProtoField(tag=6, wire=WireType.REPEATED_MESSAGE, cls=PeriodUsage)] = Field(default_factory=list)
    product_usage: Annotated[List[ProductUsage], ProtoField(tag=7, wire=WireType.REPEATED_MESSAGE, cls=ProductUsage)] = Field(default_factory=list)
    current_period: Annotated[Optional[UsagePeriod], ProtoField(tag=8, wire=WireType.MESSAGE, cls=UsagePeriod)] = None
    is_unified_billing_user: Annotated[bool, ProtoField(tag=11, wire=WireType.BOOL)] = False
    prepaid_balance: Annotated[str, ProtoField(tag=12, wire=WireType.STRING)] = ""


class GetGrokCreditsConfigResponse(BaseModel):
    config: Annotated[Optional[GrokCreditsConfig], ProtoField(tag=1, wire=WireType.MESSAGE, cls=GrokCreditsConfig)] = None


class GetLatestAssetMetadataVersionRequest(BaseModel):
    root_asset_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetProductsInfoRequest(BaseModel):
    provider: Annotated[SubscriptionProvider, ProtoField(tag=1, wire=WireType.INT32)] = SubscriptionProvider.SUBSCRIPTION_PROVIDER_INVALID
    user_activity: Annotated[UserActivity, ProtoField(tag=2, wire=WireType.INT32)] = UserActivity.USER_ACTIVITY_UNKNOWN


class GetProductsInfoResponse(BaseModel):
    google: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    apple: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    stripe: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    x: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    paypal: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    braintree: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class GetStatRequest(BaseModel):
    pass


class GetStorageUsageInfoRequest(BaseModel):
    pass


class GetStorageUsageInfoResponse(BaseModel):
    total_storage_bytes: Annotated[int, ProtoField(tag=1, wire=WireType.INT64)] = 0
    used_storage_bytes: Annotated[int, ProtoField(tag=2, wire=WireType.INT64)] = 0
    total_generated_video_storage_bytes: Annotated[int, ProtoField(tag=3, wire=WireType.INT64)] = 0
    used_generated_video_storage_bytes: Annotated[int, ProtoField(tag=4, wire=WireType.INT64)] = 0


class GetSubscriptionsRequest(BaseModel):
    provider: Annotated[SubscriptionProvider, ProtoField(tag=1, wire=WireType.INT32)] = SubscriptionProvider.SUBSCRIPTION_PROVIDER_INVALID
    status: Annotated[SubscriptionStatus, ProtoField(tag=2, wire=WireType.INT32)] = SubscriptionStatus.SUBSCRIPTION_STATUS_INVALID


class GetSubscriptionsResponse(BaseModel):
    subscriptions: Annotated[List[Subscription], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=Subscription)] = Field(default_factory=list)


class GetSystemPromptRequest(BaseModel):
    system_prompt_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetTaskByConversationIdIfExistsRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class GetTaskWithResultsRequest(BaseModel):
    task_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class PublicTeam(BaseModel):
    team_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GetTeamsWhereUserHasActiveSubResponse(BaseModel):
    public_teams: Annotated[List[PublicTeam], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=PublicTeam)] = Field(default_factory=list)


class GetUserTasksRequest(BaseModel):
    pass


class GetWorkspaceRequest(BaseModel):
    workspace_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class InternalStats(BaseModel):
    stats_json: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ListAllAssetVersionsRequest(BaseModel):
    root_asset_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ListAllAssetVersionsResponse(BaseModel):
    assets: Annotated[List[AssetMetadata], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=AssetMetadata)] = Field(default_factory=list)


class ListAssetMetadataRequest(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    page_size: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    page_token: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    mime_types: Annotated[List[str], ProtoField(tag=4, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    order_by: Annotated[ListAssetMetadataRequestOrderBy, ProtoField(tag=6, wire=WireType.INT32)] = ListAssetMetadataRequestOrderBy.ORDER_BY_INVALID
    workspace_id: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    source: Annotated[AssetSource, ProtoField(tag=8, wire=WireType.INT32)] = AssetSource.SOURCE_ANY
    asset_ids: Annotated[List[str], ProtoField(tag=9, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    is_latest: Annotated[bool, ProtoField(tag=10, wire=WireType.BOOL)] = False
    shared_with_me: Annotated[bool, ProtoField(tag=11, wire=WireType.BOOL)] = False
    include_imagine_files: Annotated[bool, ProtoField(tag=12, wire=WireType.BOOL)] = False


class ListAssetMetadataResponse(BaseModel):
    assets: Annotated[List[AssetMetadata], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=AssetMetadata)] = Field(default_factory=list)
    next_page_token: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ListFilesRequest(BaseModel):
    conversation_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    path: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    page_token: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    page_size: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    share_link_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class ListFilesResponse(BaseModel):
    files: Annotated[List[File], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=File)] = Field(default_factory=list)
    path: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    next_page_token: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class PaymentMethodInfo(BaseModel):
    payment_method_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    payment_type: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    billing_info: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    card_details: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    link_details: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    added_ts: Annotated[bytes, ProtoField(tag=7, wire=WireType.BYTES_FIELD)] = b""


class ListPaymentMethodsResponse(BaseModel):
    payment_methods: Annotated[List[PaymentMethodInfo], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=PaymentMethodInfo)] = Field(default_factory=list)


class PrepaidBalanceChange(BaseModel):
    amount: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    invoice_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    invoice_reference: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=4, wire=WireType.TIMESTAMP)] = ""
    topup_status: Annotated[PrepaidBalanceChangeTopUpStatus, ProtoField(tag=5, wire=WireType.INT32)] = PrepaidBalanceChangeTopUpStatus.INVALID
    change_origin: Annotated[PrepaidBalanceChangeChangeOrigin, ProtoField(tag=6, wire=WireType.INT32)] = PrepaidBalanceChangeChangeOrigin.INVALID_ORIGIN


class ListPrepaidBalanceChangesResponse(BaseModel):
    changes: Annotated[List[PrepaidBalanceChange], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=PrepaidBalanceChange)] = Field(default_factory=list)
    total: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ListSystemPromptsRequest(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    page_size: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    page_token: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    order_by: Annotated[ListSystemPromptsRequestOrderBy, ProtoField(tag=4, wire=WireType.INT32)] = ListSystemPromptsRequestOrderBy.ORDER_BY_INVALID


class SystemPrompt(BaseModel):
    system_prompt_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    create_time: Annotated[str, ProtoField(tag=3, wire=WireType.TIMESTAMP)] = ""
    last_use_time: Annotated[str, ProtoField(tag=4, wire=WireType.TIMESTAMP)] = ""
    content: Annotated[List[Content], ProtoField(tag=5, wire=WireType.REPEATED_MESSAGE, cls=Content)] = Field(default_factory=list)


class ListSystemPromptsResponse(BaseModel):
    assets: Annotated[List[SystemPrompt], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=SystemPrompt)] = Field(default_factory=list)
    next_page_token: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ListWorkspacesRequest(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    page_size: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    page_token: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    order_by: Annotated[ListWorkspacesRequestOrderBy, ProtoField(tag=4, wire=WireType.INT32)] = ListWorkspacesRequestOrderBy.ORDER_BY_INVALID


class ListWorkspacesResponse(BaseModel):
    workspaces: Annotated[List[Workspace], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=Workspace)] = Field(default_factory=list)
    next_page_token: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class PauseTaskScheduleRequest(BaseModel):
    schedule_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    is_enabled: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class PortalSessionFlowDataHostedConfirmation(BaseModel):
    custom_message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class PortalSessionFlowDataRedirectToUrl(BaseModel):
    return_url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class PortalSessionFlowDataFlowDataSubscriptionCancelCouponOffer(BaseModel):
    coupon: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class PortalSessionFlowDataRetentionCouponOffer(BaseModel):
    coupon: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class PortalSessionFlowDataRetention(BaseModel):
    coupon_offer: Annotated[Optional[PortalSessionFlowDataFlowDataSubscriptionCancelRetentionCouponOffer], ProtoField(tag=1, wire=WireType.MESSAGE, cls=PortalSessionFlowDataFlowDataSubscriptionCancelRetentionCouponOffer)] = None


class PortalSessionFlowDataCouponOffer(BaseModel):
    coupon: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class FlowDataAfterCompletionHostedConfirmation(BaseModel):
    custom_message: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class FlowDataAfterCompletionRedirectToUrl(BaseModel):
    return_url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class FlowDataSubscriptionCancelRetentionCouponOffer(BaseModel):
    coupon: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class FlowDataSubscriptionCancelRetention(BaseModel):
    coupon_offer: Annotated[Optional[PortalSessionFlowDataFlowDataSubscriptionCancelRetentionCouponOffer], ProtoField(tag=1, wire=WireType.MESSAGE, cls=PortalSessionFlowDataFlowDataSubscriptionCancelRetentionCouponOffer)] = None


class FlowDataSubscriptionCancelCouponOffer(BaseModel):
    coupon: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class RetentionCouponOffer(BaseModel):
    coupon: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class RemoveAssetRequest(BaseModel):
    workspace_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    asset_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class RemoveConversationRequest(BaseModel):
    workspace_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    conversation_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class ResetAssetConversationRequest(BaseModel):
    asset_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class RestoreAssetVersionRequest(BaseModel):
    asset_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class SearchAssetMetadataMatch(BaseModel):
    asset_metadata: Annotated[Optional[AssetMetadata], ProtoField(tag=1, wire=WireType.MESSAGE, cls=AssetMetadata)] = None
    highlight: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    name_highlight: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class SearchAssetMetadataRequest(BaseModel):
    query: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    page_size: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    page_token: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    mime_types: Annotated[List[str], ProtoField(tag=4, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    source: Annotated[AssetSource, ProtoField(tag=5, wire=WireType.INT32)] = AssetSource.SOURCE_ANY


class SearchAssetMetadataResponse(BaseModel):
    matches: Annotated[List[SearchAssetMetadataMatch], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=SearchAssetMetadataMatch)] = Field(default_factory=list)
    next_page_token: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class SetAutoTopupRuleRequest(BaseModel):
    rule: Annotated[Optional[AutoTopupRule], ProtoField(tag=1, wire=WireType.MESSAGE, cls=AutoTopupRule)] = None


class SetAutoTopupRuleResponse(BaseModel):
    pass


class SetDefaultPaymentMethodRequest(BaseModel):
    payment_method_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class SetDefaultPaymentMethodResponse(BaseModel):
    pass


class SetGrokBuildOnDemandConfigRequest(BaseModel):
    cap: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class SetGrokBuildOnDemandConfigResponse(BaseModel):
    pass


class SetIsReadForTaskResultRequest(BaseModel):
    task_result_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    value__f: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class ShareAssetRequest(BaseModel):
    asset_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    team_members_to_share: Annotated[List[str], ProtoField(tag=3, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    share_with_team_members: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False


class ShareAssetResponse(BaseModel):
    root_asset_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class StripeUiLocationEmbedded(BaseModel):
    return_url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    is_embedded: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class StripeUiLocationStripeHosted(BaseModel):
    success_url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class SubscribeViaStripeRequest(BaseModel):
    embedded: Annotated[Optional[StripeUiLocationEmbedded], ProtoField(tag=2, wire=WireType.MESSAGE, cls=StripeUiLocationEmbedded)] = None
    stripe_hosted: Annotated[Optional[StripeUiLocationStripeHosted], ProtoField(tag=3, wire=WireType.MESSAGE, cls=StripeUiLocationStripeHosted)] = None
    price_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    discount_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    subscription_type: Annotated[SubscriptionType, ProtoField(tag=6, wire=WireType.INT32)] = SubscriptionType.MONTHLY
    x_prem_discount_code_month: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    x_prem_discount_code_year: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    edu_discount_code_month: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    edu_discount_code_year: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    allowed_payment_method_types: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    ignore_existing_active_subscriptions: Annotated[bool, ProtoField(tag=20, wire=WireType.BOOL)] = False


class SubscribeViaStripeResponse(BaseModel):
    client_secret: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    url: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    ignored_due_to_active_subscriptions: Annotated[List[SubscriptionProvider], ProtoField(tag=3, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class TaskIdWithOriginResponseId(BaseModel):
    task_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    origin_response_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class TaskIdsWithOriginResponseIds(BaseModel):
    task_id_with_response_ids: Annotated[List[TaskIdWithOriginResponseId], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=TaskIdWithOriginResponseId)] = Field(default_factory=list)


class TaskResults(BaseModel):
    results: Annotated[List[TaskResult], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=TaskResult)] = Field(default_factory=list)
    next_page: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class TaskTool(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    label: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    icon: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    tool_ids: Annotated[List[str], ProtoField(tag=4, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    connector_ids: Annotated[List[str], ProtoField(tag=5, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class TaskToolsResults(BaseModel):
    tools: Annotated[List[TaskTool], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=TaskTool)] = Field(default_factory=list)


class TaskUsage(BaseModel):
    usage: Annotated[float, ProtoField(tag=1, wire=WireType.FLOAT)] = 0.0
    limit: Annotated[float, ProtoField(tag=2, wire=WireType.FLOAT)] = 0.0
    frequent_usage: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    frequent_limit: Annotated[int, ProtoField(tag=4, wire=WireType.INT32)] = 0
    occasional_usage: Annotated[int, ProtoField(tag=5, wire=WireType.INT32)] = 0
    occasional_limit: Annotated[int, ProtoField(tag=6, wire=WireType.INT32)] = 0


class TaskUsageRequest(BaseModel):
    pass


class TopUpOrGetExistingPendingChangeRequest(BaseModel):
    amount: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class TopUpOrGetExistingPendingChangeResponse(BaseModel):
    change: Annotated[Optional[PrepaidBalanceChange], ProtoField(tag=1, wire=WireType.MESSAGE, cls=PrepaidBalanceChange)] = None


class UnreadCountForTask(BaseModel):
    task_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    unread_count: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0


class UpdateAssetRequest(BaseModel):
    asset_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    make_new_version: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    name: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    content: Annotated[bytes, ProtoField(tag=4, wire=WireType.BYTES_FIELD)] = b""


class UpdateSystemPromptRequest(BaseModel):
    system_prompt_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    content: Annotated[List[Content], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=Content)] = Field(default_factory=list)


class UpdateTaskRequest(BaseModel):
    task_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    schedule_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    updated_task: Annotated[Optional[CreateTaskRequest], ProtoField(tag=3, wire=WireType.MESSAGE, cls=CreateTaskRequest)] = None


class UpdateWorkspaceRequest(BaseModel):
    workspace_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    icon: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    custom_personality: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    is_public: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False


class UserTasks(BaseModel):
    tasks: Annotated[List[TaskWithSchedule], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=TaskWithSchedule)] = Field(default_factory=list)


class UserTasksWithUnreadResults(BaseModel):
    tasks: Annotated[List[TaskWithSchedule], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=TaskWithSchedule)] = Field(default_factory=list)
    unread_results: Annotated[List[TaskResult], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=TaskResult)] = Field(default_factory=list)
    unread_counts: Annotated[List[UnreadCountForTask], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=UnreadCountForTask)] = Field(default_factory=list)
    task_usage: Annotated[Optional[TaskUsage], ProtoField(tag=4, wire=WireType.MESSAGE, cls=TaskUsage)] = None


class getTaskResultsRequest(BaseModel):
    task_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    next_page: Annotated[int, ProtoField(tag=2, wire=WireType.INT32)] = 0
    limit: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0

