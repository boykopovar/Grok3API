BASE_URL: str = "https://grok.com"
APP_VERSION: str = "1.1.65-release.00"

GRPC_CREATE_ANON_USER: str = "/auth_frontend.AuthFrontend/CreateAnonUser"
GRPC_CREATE_ANON_CHALLENGE: str = "/auth_frontend.AuthFrontend/CreateAnonUserChallenge"
GRPC_CHAT: str = "/grok_api.Chat/CreateConversationAndRespond"
GRPC_ADD_RESPONSE = "/grok_api.Chat/AddResponse"
