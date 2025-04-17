# offcloud_api

`offcloud_api` is a lightweight Python client for the Offcloud API, providing easy programmatic access to Offcloud’s download and proxy endpoints.

## Features
- (Optionally) authenticate via username/password and retrieve API key
- Start instant, cloud, or remote downloads
- Check download status and list archive links
- Handle errors with clear, typed exceptions (`AuthError`, `HTTPError`, etc.)

## Installation

```bash
pip install offcloud_api
# or editable during development
pip install -e .
```

## Quickstart

```python
from offcloud_api import OffcloudAPI
from offcloud_api.exceptions import OffcloudError

client = OffcloudAPI()
try:
    client.login("username", "password")
    key_data = client.get_api_key()
    client.api_key = key_data["key"]

    # start an instant download
    job = client.instant("https://example.com/file.zip")
    request_id = job.get("id")

    # poll for completion
    status = client.cloud_status(request_id)
    if status.get("status") == "finished":
        print(client.list_cloud(request_id))

except OffcloudError as e:
    print(f"Error: {e}")
```

## Using an existing API key

If you already have an API token, you can skip the login steps and instantiate the client directly:
```python
from offcloud_api import OffcloudAPI
from offcloud_api.exceptions import OffcloudError

client = OffcloudAPI(api_key="your_api_key_here")
try:
    # start an instant download right away
    job = client.instant("https://example.com/file.zip")
    print(job)

except OffcloudError as e:
    print(f"Error: {e}")
```
## Exceptions
All errors inherit from `OffcloudError`. Common subclasses:
- `AuthError` (401)
- `NotFoundError` (404)
- `RateLimitError` (429)
- `HTTPError` (other non-2xx)

## Development & Testing
- working on getting pytests!
- better error handling.
- etc.

## Contributing

1. Fork the repo
2. Create a feature branch
3. Submit a pull request

## License

This project is licensed under the **Non‑Commercial MIT License**.  
You are free to use, copy, modify and distribute this library **only for non‑commercial purposes**.  
Derivative works that add substantial new content may be licensed (and sold) separately.  
See [LICENSE](LICENSE) for full terms.

