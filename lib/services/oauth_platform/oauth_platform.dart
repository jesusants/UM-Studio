export 'oauth_flow_exception.dart';
export 'oauth_platform_stub.dart'
    if (dart.library.js_interop) 'oauth_platform_web.dart';

import 'oauth_platform_stub.dart'
    if (dart.library.js_interop) 'oauth_platform_web.dart';

OAuthPlatformDelegate createOAuthPlatform() => getOAuthPlatformDelegate();
