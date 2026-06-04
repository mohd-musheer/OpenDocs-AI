
# HTTPConnection class - FastAPI

URL: https://fastapi.tiangolo.com/reference/httpconnection/

HTTPConnection
class¶
When you want to define dependencies that should be compatible with both HTTP and WebSockets, you can define a parameter that takes an HTTPConnection
instead of a Request
or a WebSocket
.
You can import it from fastapi.requests
:
from fastapi.requests import HTTPConnection
fastapi.requests.HTTPConnection
¶
HTTPConnection(scope, receive=None)
Bases: Mapping[str, Any]
, Generic[StateT]
A base class for incoming HTTP connections, that is used to provide
any functionality that is common to both Request
and WebSocket
.
Source code in starlette/requests.py
def __init__(self, scope: Scope, receive: Receive | None = None) -> None:
assert scope["type"] in ("http", "websocket")
self.scope = scope
url_for
¶
url_for(name, /, **path_params)
Source code in starlette/requests.py
def url_for(self, name: str, /, **path_params: Any) -> URL:
url_path_provider: Router | Starlette | None = self.scope.get("router") or self.scope.get("app")
if url_path_provider is None:
raise RuntimeError("The `url_for` method can only be used inside a Starlette application or with a router.")
url_path = url_path_provider.url_path_for(name, **path_params)
return url_path.make_absolute_url(base_url=self.base_url)
