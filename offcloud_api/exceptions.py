class OffcloudError(Exception):
    pass

class HTTPError(OffcloudError):
    def __init__(self, status_code: int, message: str):
        super().__init__(f"HTTP {status_code}: {message}")
        self.status_code = status_code
        self.message = message

class AuthError(HTTPError):
    pass

class NotFoundError(HTTPError):
    pass

class RateLimitError(HTTPError):
    pass
