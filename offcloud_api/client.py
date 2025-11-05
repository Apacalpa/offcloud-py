import requests

from .exceptions import HTTPError, AuthError, NotFoundError, RateLimitError


class OffcloudAPI:
    def __init__(self, api_key: str = None):
        self.base_url = "https://offcloud.com/api"
        self.session = requests.Session()
        self.api_key = api_key

    def _params(self) -> dict:
        return {"key": self.api_key} if self.api_key else {}

    def _request(self, method: str, url: str, **kwargs):
        resp = getattr(self.session, method)(url, params=self._params(), **kwargs)
        code = resp.status_code
        if code == 401:
            raise AuthError(code, resp.text)
        if code == 404:
            raise NotFoundError(code, resp.text)
        if code == 429:
            raise RateLimitError(code, resp.text)
        if not resp.ok:
            raise HTTPError(code, resp.text)
        return resp

    # Authentication
    def login(self, username: str, password: str) -> dict:
        url = f"{self.base_url}/login"
        resp = self._request("post", url, data={"username": username, "password": password})
        return resp.json()

    def get_api_key(self) -> dict:
        url = f"{self.base_url}/key"
        resp = self._request("post", url)
        return resp.json()

    def check_login(self) -> dict:
        url = f"{self.base_url}/check"
        resp = self._request("get", url)
        return resp.json()

    # Download submissions
    def instant(self, url: str, proxy_id: str = None) -> dict:
        endpoint = f"{self.base_url}/instant"
        data = {"url": url}
        if proxy_id:
            data["proxyId"] = proxy_id
        resp = self._request("post", endpoint, data=data)
        return resp.json()

    def cloud(self, url: str) -> dict:
        endpoint = f"{self.base_url}/cloud"
        resp = self._request("post", endpoint, data={"url": url})
        return resp.json()

    def remote(self, url: str, remote_option_id: str = None, folder_id: str = None) -> dict:
        endpoint = f"{self.base_url}/remote"
        data = {"url": url}
        if remote_option_id:
            data["remoteOptionId"] = remote_option_id
        if folder_id:
            data["folderId"] = folder_id
        resp = self._request("post", endpoint, data=data)
        return resp.json()

    def get_proxies(self) -> dict:
        url = f"{self.base_url}/proxy"
        resp = self._request("post", url)
        return resp.json()

    def cloud_status(self, request_id: str) -> dict:
        url = f"{self.base_url}/cloud/status"
        resp = self._request("post", url, data={"requestId": request_id})
        return resp.json()

    def remote_status(self, request_id: str) -> dict:
        url = f"{self.base_url}/remote/status"
        resp = self._request("post", url, data={"requestId": request_id})
        return resp.json()

    def cache_info(self, hashes: list) -> dict:
        url = f"{self.base_url}/cache"
        resp = self._request("post", url, json={"hashes": hashes})
        return resp.json()

    def explore_cloud(self, request_id: str) -> dict:
        url = f"{self.base_url}/cloud/explore/{request_id}"
        resp = self._request("get", url)
        return resp.json()

    def list_cloud(self, request_id: str) -> dict:
        url = f"{self.base_url}/cloud/list/{request_id}"
        resp = self._request("get", url)
        return resp.json()

    def retry_cloud(self, request_id: str) -> dict:
        url = f"{self.base_url}/cloud/retry/{request_id}"
        resp = self._request("get", url)
        return resp.json()

    def retry_remote(self, request_id: str) -> dict:
        url = f"{self.base_url}/remote/retry/{request_id}"
        resp = self._request("get", url)
        return resp.json()