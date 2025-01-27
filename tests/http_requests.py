"""Docstring."""

from fastapi.testclient import TestClient


def do_post_request(
        app: TestClient,
        url: str,
        data: dict,
        token: str = "") -> tuple[int, dict | str]:
    """
    Make a POST request to the given URL with the given data and token.

    Parameters
    ----------
    app : TestClient
        The FastAPI application client.
    url : str
        The URL to make the POST request to.
    token : str, optional
        The JWT token to use in the request.
    data : dict
        The data to send in the request body.

    Returns
    -------
    status_code : int
        The HTTP status code of the response.
    json_data : dict | str
        The JSON data returned in the response.
    """
    try:
        headers = {"Authorization": f"Bearer {token}"}
        r = app.post(url, headers=headers, json=data)
        return r.status_code, r.json()
    except (ValueError, TypeError, ConnectionError) as e:
        return 500, {"error": str(e)}
