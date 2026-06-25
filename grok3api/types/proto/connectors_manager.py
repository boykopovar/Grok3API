from typing import Annotated, List, Optional

from enum import IntEnum
from pydantic import BaseModel, Field

from grok3api.types.pb_meta import ProtoField, WireType
from grok3api.types.proto.shared import *


class AssetProcessingStatus(IntEnum):
    ASSET_PROCESSING_STATUS_UNKNOWN = 0
    ASSET_PROCESSING_STATUS_INDEXING = 1
    ASSET_PROCESSING_STATUS_DONE = 2
    ASSET_PROCESSING_STATUS_ERROR = 3


class ConnectorAttribute(IntEnum):
    CONNECTOR_ATTRIBUTE_UNKNOWN = 0
    CONNECTOR_ATTRIBUTE_REQUIRES_DYNAMIC_MCP_TOOL_CALL = 1
    CONNECTOR_ATTRIBUTE_SUPPORTS_DOCUMENT_SEARCH = 2


class ConnectorScope(IntEnum):
    CONNECTOR_SCOPE_UNKNOWN = 0
    CONNECTOR_SCOPE_ORGANIZATION = 1
    CONNECTOR_SCOPE_TEAM = 2
    CONNECTOR_SCOPE_USER = 3


class OAuthStrategy(IntEnum):
    OAUTH_STRATEGY_UNKNOWN = 0
    OAUTH_STRATEGY_NONE = 1
    OAUTH_STRATEGY_DCR = 2
    OAUTH_STRATEGY_CIMD = 3
    OAUTH_STRATEGY_BYO = 4


class AssetSummary(BaseModel):
    asset_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    original_mime_type: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    indexed_mime_type: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    view_url: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    status: Annotated[AssetProcessingStatus, ProtoField(tag=7, wire=WireType.INT32)] = AssetProcessingStatus.ASSET_PROCESSING_STATUS_UNKNOWN


class CatalogToolSummary(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class CatalogConnector(BaseModel):
    catalog_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    display_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    icon_url: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    category: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    discovered_tools: Annotated[List[CatalogToolSummary], ProtoField(tag=6, wire=WireType.REPEATED_MESSAGE, cls=CatalogToolSummary)] = Field(default_factory=list)
    server_url: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    user_count: Annotated[int, ProtoField(tag=8, wire=WireType.INT64)] = 0
    connector_id: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""


class ChangeStatistics(BaseModel):
    values: Annotated[int, ProtoField(tag=1, wire=WireType.INT64)] = 0


class ConnectorSync(BaseModel):
    connector_sync_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    connector_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    start_time: Annotated[str, ProtoField(tag=3, wire=WireType.TIMESTAMP)] = ""
    heartbeat_time: Annotated[str, ProtoField(tag=4, wire=WireType.TIMESTAMP)] = ""
    end_time: Annotated[str, ProtoField(tag=5, wire=WireType.TIMESTAMP)] = ""
    error: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    stats: Annotated[Optional[ChangeStatistics], ProtoField(tag=7, wire=WireType.MESSAGE, cls=ChangeStatistics)] = None


class SyncInfo(BaseModel):
    latest_sync: Annotated[Optional[ConnectorSync], ProtoField(tag=1, wire=WireType.MESSAGE, cls=ConnectorSync)] = None
    latest_successful_sync_start_time: Annotated[str, ProtoField(tag=2, wire=WireType.TIMESTAMP)] = ""
    sync_history: Annotated[List[ConnectorSync], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=ConnectorSync)] = Field(default_factory=list)


class ConnectorAndLatestSync(BaseModel):
    connector: Annotated[Optional[Connector], ProtoField(tag=1, wire=WireType.MESSAGE, cls=Connector)] = None
    latest_successful_sync_start_time: Annotated[str, ProtoField(tag=2, wire=WireType.TIMESTAMP)] = ""
    latest_sync: Annotated[Optional[ConnectorSync], ProtoField(tag=3, wire=WireType.MESSAGE, cls=ConnectorSync)] = None
    no_sync: Annotated[bool, ProtoField(tag=4, wire=WireType.EMPTY_MESSAGE)] = False
    pending_first_sync: Annotated[bool, ProtoField(tag=5, wire=WireType.EMPTY_MESSAGE)] = False
    sync: Annotated[Optional[SyncInfo], ProtoField(tag=6, wire=WireType.MESSAGE, cls=SyncInfo)] = None


class GoogleDriveConfig(BaseModel):
    workspace_domain_name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    require_explicit_access: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class SlackConfig(BaseModel):
    pass


class NotionConfig(BaseModel):
    pass


class GmailConfig(BaseModel):
    pass


class McpConfig(BaseModel):
    server_url: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    is_enabled: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False
    requires_oauth: Annotated[bool, ProtoField(tag=7, wire=WireType.BOOL)] = False
    icon_id: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    allowed_tool_names: Annotated[List[str], ProtoField(tag=9, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    blocked_tool_names: Annotated[List[str], ProtoField(tag=10, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class SharepointConfig(BaseModel):
    tenant_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    allowed_site_ids: Annotated[List[str], ProtoField(tag=2, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    auth_mode: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class GoogleCalendarConfig(BaseModel):
    pass


class OutlookConfig(BaseModel):
    pass


class MicrosoftTeamsConfig(BaseModel):
    pass


class OutlookCalendarConfig(BaseModel):
    pass


class ConnectorConfig(BaseModel):
    google_drive_config: Annotated[Optional[GoogleDriveConfig], ProtoField(tag=1, wire=WireType.MESSAGE, cls=GoogleDriveConfig)] = None
    slack_config: Annotated[Optional[SlackConfig], ProtoField(tag=2, wire=WireType.MESSAGE, cls=SlackConfig)] = None
    test_config: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    notion_config: Annotated[Optional[NotionConfig], ProtoField(tag=4, wire=WireType.MESSAGE, cls=NotionConfig)] = None
    gmail_config: Annotated[Optional[GmailConfig], ProtoField(tag=5, wire=WireType.MESSAGE, cls=GmailConfig)] = None
    mcp_config: Annotated[Optional[McpConfig], ProtoField(tag=6, wire=WireType.MESSAGE, cls=McpConfig)] = None
    sharepoint_config: Annotated[Optional[SharepointConfig], ProtoField(tag=7, wire=WireType.MESSAGE, cls=SharepointConfig)] = None
    google_calendar_config: Annotated[Optional[GoogleCalendarConfig], ProtoField(tag=8, wire=WireType.MESSAGE, cls=GoogleCalendarConfig)] = None
    outlook_config: Annotated[Optional[OutlookConfig], ProtoField(tag=9, wire=WireType.MESSAGE, cls=OutlookConfig)] = None
    microsoft_teams_config: Annotated[Optional[MicrosoftTeamsConfig], ProtoField(tag=10, wire=WireType.MESSAGE, cls=MicrosoftTeamsConfig)] = None
    outlook_calendar_config: Annotated[Optional[OutlookCalendarConfig], ProtoField(tag=11, wire=WireType.MESSAGE, cls=OutlookCalendarConfig)] = None


class ConnectorSyncLogEntry(BaseModel):
    create_time: Annotated[str, ProtoField(tag=1, wire=WireType.TIMESTAMP)] = ""
    origin: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    message: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class ConnectorV2(BaseModel):
    connector_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    connector_type: Annotated[ConnectorType, ProtoField(tag=2, wire=WireType.INT32)] = ConnectorType.CONNECTOR_TYPE_UNKNOWN
    auth_valid: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    connector_config: Annotated[Optional[ConnectorConfig], ProtoField(tag=4, wire=WireType.MESSAGE, cls=ConnectorConfig)] = None
    name: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    icon_url: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    catalog_id: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    category: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    server_url: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    oauth_connector_id: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""


class CreateConnectorRequest(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    connector_type: Annotated[ConnectorType, ProtoField(tag=3, wire=WireType.INT32)] = ConnectorType.CONNECTOR_TYPE_UNKNOWN
    allowed_user_ids: Annotated[List[str], ProtoField(tag=4, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    team_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    google_drive_config: Annotated[Optional[GoogleDriveConfig], ProtoField(tag=6, wire=WireType.MESSAGE, cls=GoogleDriveConfig)] = None
    config: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    connector_config: Annotated[Optional[ConnectorConfig], ProtoField(tag=8, wire=WireType.MESSAGE, cls=ConnectorConfig)] = None
    scope: Annotated[ConnectorScope, ProtoField(tag=9, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    connector_catalog_id: Annotated[str, ProtoField(tag=11, wire=WireType.STRING)] = ""
    confirm_override: Annotated[bool, ProtoField(tag=12, wire=WireType.BOOL)] = False


class DeleteOauthConnectorRequest(BaseModel):
    team_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    filter_connector_type: Annotated[ConnectorType, ProtoField(tag=3, wire=WireType.INT32)] = ConnectorType.CONNECTOR_TYPE_UNKNOWN
    connector_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    scope: Annotated[ConnectorScope, ProtoField(tag=5, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class DiscoveredOAuthMetadata(BaseModel):
    issuer: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    authorization_endpoint: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    token_endpoint: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    registration_endpoint: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    scopes_supported: Annotated[List[str], ProtoField(tag=5, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    grant_types_supported: Annotated[List[str], ProtoField(tag=6, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    response_types_supported: Annotated[List[str], ProtoField(tag=7, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    code_challenge_methods_supported: Annotated[List[str], ProtoField(tag=8, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class ExchangeCodeRequest(BaseModel):
    oauth_cookie: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    code: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    state: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    team_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    connector_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    scope: Annotated[ConnectorScope, ProtoField(tag=6, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""


class GetAuthUrlRequest(BaseModel):
    redirect_url: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    team_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    filter_connector_type: Annotated[ConnectorType, ProtoField(tag=5, wire=WireType.INT32)] = ConnectorType.CONNECTOR_TYPE_UNKNOWN
    connector_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    scope: Annotated[ConnectorScope, ProtoField(tag=7, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""


class GetAuthUrlResponse(BaseModel):
    auth_url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    oauth_cookie: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class GetConnectorRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    return_create_user: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    return_modify_user: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    return_allowed_users: Annotated[bool, ProtoField(tag=4, wire=WireType.BOOL)] = False
    team_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    sync_history_length: Annotated[int, ProtoField(tag=6, wire=WireType.INT32)] = 0
    scope: Annotated[ConnectorScope, ProtoField(tag=7, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""


class GetConnectorResponse(BaseModel):
    connector: Annotated[Optional[Connector], ProtoField(tag=1, wire=WireType.MESSAGE, cls=Connector)] = None
    latest_successful_sync_start_time: Annotated[str, ProtoField(tag=2, wire=WireType.TIMESTAMP)] = ""
    sync_history: Annotated[List[ConnectorSync], ProtoField(tag=3, wire=WireType.REPEATED_MESSAGE, cls=ConnectorSync)] = Field(default_factory=list)
    no_sync: Annotated[bool, ProtoField(tag=4, wire=WireType.EMPTY_MESSAGE)] = False
    pending_first_sync: Annotated[bool, ProtoField(tag=5, wire=WireType.EMPTY_MESSAGE)] = False
    sync: Annotated[Optional[SyncInfo], ProtoField(tag=6, wire=WireType.MESSAGE, cls=SyncInfo)] = None


class GetConnectorSyncLogsRequest(BaseModel):
    team_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    connector_sync_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    scope: Annotated[ConnectorScope, ProtoField(tag=3, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class GetConnectorSyncLogsResponse(BaseModel):
    entries: Annotated[List[ConnectorSyncLogEntry], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=ConnectorSyncLogEntry)] = Field(default_factory=list)


class GetTeamHistoryRequest(BaseModel):
    team_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    scope: Annotated[ConnectorScope, ProtoField(tag=2, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class TeamHistoryItem(BaseModel):
    team_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    action_time: Annotated[str, ProtoField(tag=2, wire=WireType.TIMESTAMP)] = ""
    user_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    action_type: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    action_details_json: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class GetTeamHistoryResponse(BaseModel):
    items: Annotated[List[TeamHistoryItem], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=TeamHistoryItem)] = Field(default_factory=list)


class GetValidAccessTokenRequest(BaseModel):
    scope: Annotated[ConnectorScope, ProtoField(tag=1, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    connector_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class GetValidAccessTokenResponse(BaseModel):
    access_token: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class InvalidateOAuthTokenRequest(BaseModel):
    connector_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ListAssetsForConnectorRequest(BaseModel):
    connector_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    team_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    page_size: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    page_token: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    scope: Annotated[ConnectorScope, ProtoField(tag=5, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""


class ListAssetsForConnectorResponse(BaseModel):
    assets: Annotated[List[AssetSummary], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=AssetSummary)] = Field(default_factory=list)
    connector_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    total_count: Annotated[int, ProtoField(tag=3, wire=WireType.INT32)] = 0
    next_page_token: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class ListAvailableConnectorsRequestV2(BaseModel):
    pass


class ListAvailableConnectorsResponseV2(BaseModel):
    connectors: Annotated[List[CatalogConnector], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=CatalogConnector)] = Field(default_factory=list)
    connectors_v2: Annotated[List[ConnectorV2], ProtoField(tag=2, wire=WireType.REPEATED_MESSAGE, cls=ConnectorV2)] = Field(default_factory=list)


class ListCatalogConnectorsRequest(BaseModel):
    pass


class ListCatalogConnectorsResponse(BaseModel):
    catalog_connectors: Annotated[List[CatalogConnector], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=CatalogConnector)] = Field(default_factory=list)


class ListConnectorsForUserRequest(BaseModel):
    team_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    scope: Annotated[ConnectorScope, ProtoField(tag=2, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class PublicConnectorForUser(BaseModel):
    connector_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    connector_type: Annotated[ConnectorType, ProtoField(tag=2, wire=WireType.INT32)] = ConnectorType.CONNECTOR_TYPE_UNKNOWN
    is_active_for_user: Annotated[bool, ProtoField(tag=3, wire=WireType.BOOL)] = False
    latest_successful_sync: Annotated[Optional[ConnectorSync], ProtoField(tag=4, wire=WireType.MESSAGE, cls=ConnectorSync)] = None
    latest_sync: Annotated[Optional[ConnectorSync], ProtoField(tag=5, wire=WireType.MESSAGE, cls=ConnectorSync)] = None
    connector_config: Annotated[Optional[ConnectorConfig], ProtoField(tag=6, wire=WireType.MESSAGE, cls=ConnectorConfig)] = None
    name: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    attributes: Annotated[List[ConnectorAttribute], ProtoField(tag=8, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    needs_reauth: Annotated[bool, ProtoField(tag=9, wire=WireType.BOOL)] = False


class ListConnectorsForUserResponse(BaseModel):
    connectors: Annotated[List[PublicConnectorForUser], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=PublicConnectorForUser)] = Field(default_factory=list)


class ListConnectorsRequest(BaseModel):
    return_create_user: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    return_modify_user: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    team_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    scope: Annotated[ConnectorScope, ProtoField(tag=4, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""


class ListConnectorsRequestV2(BaseModel):
    refresh_token: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False


class ListConnectorsResponse(BaseModel):
    connectors: Annotated[List[ConnectorAndLatestSync], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=ConnectorAndLatestSync)] = Field(default_factory=list)


class ListConnectorsResponseV2(BaseModel):
    connectors: Annotated[List[ConnectorV2], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=ConnectorV2)] = Field(default_factory=list)


class ListMcpDiscoveredToolsRequest(BaseModel):
    scope_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    connector_ids: Annotated[List[str], ProtoField(tag=3, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    scope: Annotated[ConnectorScope, ProtoField(tag=4, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    include_all_tools: Annotated[bool, ProtoField(tag=5, wire=WireType.BOOL)] = False
    admin: Annotated[bool, ProtoField(tag=6, wire=WireType.BOOL)] = False


class McpTool(BaseModel):
    name: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    remote_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    title: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    description: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    json_schema: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    connector_id: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    server_name: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""
    server_url: Annotated[str, ProtoField(tag=8, wire=WireType.STRING)] = ""
    scope: Annotated[str, ProtoField(tag=9, wire=WireType.STRING)] = ""
    annotations_json: Annotated[str, ProtoField(tag=10, wire=WireType.STRING)] = ""
    is_blocked: Annotated[bool, ProtoField(tag=11, wire=WireType.BOOL)] = False


class ListMcpDiscoveredToolsResponse(BaseModel):
    mcp_tools: Annotated[List[McpTool], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=McpTool)] = Field(default_factory=list)
    connectors_needing_reauth: Annotated[List[str], ProtoField(tag=2, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    connector_ids_needing_reauth: Annotated[List[str], ProtoField(tag=3, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class ListOauthConnectorsRequest(BaseModel):
    team_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    connector_type: Annotated[ConnectorType, ProtoField(tag=2, wire=WireType.INT32)] = ConnectorType.CONNECTOR_TYPE_UNKNOWN
    scope: Annotated[ConnectorScope, ProtoField(tag=3, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class OAuthConnectorStatus(BaseModel):
    connector_type: Annotated[ConnectorType, ProtoField(tag=1, wire=WireType.INT32)] = ConnectorType.CONNECTOR_TYPE_UNKNOWN
    create_time: Annotated[str, ProtoField(tag=2, wire=WireType.TIMESTAMP)] = ""
    user: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class ListOauthConnectorsResponse(BaseModel):
    status: Annotated[List[OAuthConnectorStatus], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=OAuthConnectorStatus)] = Field(default_factory=list)


class ListSharepointSitesRequest(BaseModel):
    connector_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    scope: Annotated[ConnectorScope, ProtoField(tag=2, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class SharepointSite(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    display_name: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    name: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    web_url: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class ListSharepointSitesResponse(BaseModel):
    sites: Annotated[List[SharepointSite], ProtoField(tag=1, wire=WireType.REPEATED_MESSAGE, cls=SharepointSite)] = Field(default_factory=list)


class OAuthClientCredentials(BaseModel):
    client_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    client_secret: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    authorization_endpoint: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    token_endpoint: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""
    scopes: Annotated[List[str], ProtoField(tag=5, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    issuer: Annotated[str, ProtoField(tag=6, wire=WireType.STRING)] = ""
    registration_endpoint: Annotated[str, ProtoField(tag=7, wire=WireType.STRING)] = ""


class RemoveConnectorRequest(BaseModel):
    id_f: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    team_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    scope: Annotated[ConnectorScope, ProtoField(tag=3, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=4, wire=WireType.STRING)] = ""


class SetMcpOauthCredentialsRequest(BaseModel):
    scope: Annotated[ConnectorScope, ProtoField(tag=1, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""
    connector_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    credentials: Annotated[Optional[OAuthClientCredentials], ProtoField(tag=4, wire=WireType.MESSAGE, cls=OAuthClientCredentials)] = None


class SetSharepointAllowedSitesRequest(BaseModel):
    connector_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    scope: Annotated[ConnectorScope, ProtoField(tag=2, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    allowed_site_ids: Annotated[List[str], ProtoField(tag=4, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)


class SetSharepointAllowedSitesResponse(BaseModel):
    pass


class TriggerConnectorSyncRequest(BaseModel):
    connector_id: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""
    scope: Annotated[ConnectorScope, ProtoField(tag=2, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""


class TriggerConnectorSyncResponse(BaseModel):
    success: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    message: Annotated[str, ProtoField(tag=2, wire=WireType.STRING)] = ""


class UpdateConnectorRequest(BaseModel):
    connector: Annotated[Optional[Connector], ProtoField(tag=1, wire=WireType.MESSAGE, cls=Connector)] = None
    field_mask: Annotated[List[str], ProtoField(tag=2, wire=WireType.FIELD_MASK)] = Field(default_factory=list)
    team_id: Annotated[str, ProtoField(tag=3, wire=WireType.STRING)] = ""
    scope: Annotated[ConnectorScope, ProtoField(tag=4, wire=WireType.INT32)] = ConnectorScope.CONNECTOR_SCOPE_UNKNOWN
    scope_id: Annotated[str, ProtoField(tag=5, wire=WireType.STRING)] = ""
    allowed_tool_names: Annotated[List[str], ProtoField(tag=6, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    blocked_tool_names: Annotated[List[str], ProtoField(tag=7, wire=WireType.REPEATED_STRING)] = Field(default_factory=list)
    admin: Annotated[bool, ProtoField(tag=8, wire=WireType.BOOL)] = False


class ValidateMcpServerUrlRequest(BaseModel):
    url: Annotated[str, ProtoField(tag=1, wire=WireType.STRING)] = ""


class ValidateMcpServerUrlResponse(BaseModel):
    is_valid: Annotated[bool, ProtoField(tag=1, wire=WireType.BOOL)] = False
    auth_required: Annotated[bool, ProtoField(tag=2, wire=WireType.BOOL)] = False
    oauth_strategy: Annotated[OAuthStrategy, ProtoField(tag=3, wire=WireType.INT32)] = OAuthStrategy.OAUTH_STRATEGY_UNKNOWN
    discovered_oauth_metadata: Annotated[Optional[DiscoveredOAuthMetadata], ProtoField(tag=4, wire=WireType.MESSAGE, cls=DiscoveredOAuthMetadata)] = None

