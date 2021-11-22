import httpx

from typing import Dict, Any, Optional


class HTTPClient:
    def request(
        self, method: str, endpoint: str, body: Dict[str, Any] = None
    ) -> httpx.Response:
        pass


class UserServiceHTTPClient(HTTPClient):
    def __init__(self, client: httpx.Client):
        self._client = client

    def request(
        self, method: str, endpoint: str, body: Dict[str, Any] = None
    ) -> Optional[Dict[str, Any]]:
        response = self._client.request(method=method, url=endpoint, json=body)
        if response.is_error:
            return None
        return response.json()
