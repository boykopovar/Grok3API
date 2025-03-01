from dataclasses import dataclass, field
from typing import List, Optional, Any, Dict

from grok3.types.GeneratedImage import GeneratedImage


@dataclass
class ModelResponse:
    responseId: str
    message: str
    sender: str
    createTime: str
    parentResponseId: str
    manual: bool
    partial: bool
    shared: bool
    query: str
    queryType: str
    webSearchResults: List[Any] = field(default_factory=list)
    xpostIds: List[Any] = field(default_factory=list)
    xposts: List[Any] = field(default_factory=list)
    generatedImages: List[GeneratedImage] = field(default_factory=list)
    imageAttachments: List[Any] = field(default_factory=list)
    fileAttachments: List[Any] = field(default_factory=list)
    cardAttachmentsJson: List[Any] = field(default_factory=list)
    fileUris: List[Any] = field(default_factory=list)
    fileAttachmentsMetadata: List[Any] = field(default_factory=list)
    isControl: bool = False
    steps: List[Any] = field(default_factory=list)
    mediaTypes: List[Any] = field(default_factory=list)

    def __init__(self, data: Dict[str, Any], cookies: Optional[str] = None):
        self.responseId = data.get("responseId", "")
        self.message = data.get("message", "")
        self.sender = data.get("sender", "")
        self.createTime = data.get("createTime", "")
        self.parentResponseId = data.get("parentResponseId", "")
        self.manual = data.get("manual", False)
        self.partial = data.get("partial", False)
        self.shared = data.get("shared", False)
        self.query = data.get("query", "")
        self.queryType = data.get("queryType", "")
        self.webSearchResults = data.get("webSearchResults", [])
        self.xpostIds = data.get("xpostIds", [])
        self.xposts = data.get("xposts", [])

        self.generatedImages = []
        for url in data.get("generatedImageUrls", []):
            self.generatedImages.append(GeneratedImage(cookies=cookies or "", url=url))

        self.imageAttachments = data.get("imageAttachments", [])
        self.fileAttachments = data.get("fileAttachments", [])
        self.cardAttachmentsJson = data.get("cardAttachmentsJson", [])
        self.fileUris = data.get("fileUris", [])
        self.fileAttachmentsMetadata = data.get("fileAttachmentsMetadata", [])
        self.isControl = data.get("isControl", False)
        self.steps = data.get("steps", [])
        self.mediaTypes = data.get("mediaTypes", [])


@dataclass
class GrokResponse:
    modelResponse: ModelResponse
    isThinking: bool
    isSoftStop: bool
    responseId: str
    newTitle: Optional[str] = None

    def __init__(self, data: Dict[str, Any], cookies: str):
        result = data.get("result", {})
        response_data = result.get("response", {})
        # Передаём cookies в конструктор ModelResponse
        self.modelResponse = ModelResponse(response_data.get("modelResponse", {}), cookies=cookies)
        self.isThinking = response_data.get("isThinking", False)
        self.isSoftStop = response_data.get("isSoftStop", False)
        self.responseId = response_data.get("responseId", "")
        title_data = result.get("title", {})
        self.newTitle = title_data.get("newTitle") if title_data else None
