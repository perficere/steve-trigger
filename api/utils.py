import json

import requests
from requests import RequestException, Response

import env

DEFAULT_HEADERS = {
    "Internal-Key": env.INTERNAL_KEY,
}


def get_response_data(response: Response):
    """
    Returns the body of the response if it’s status code is 2xx.
    Else, raises an exception.
    """
    if response.ok:
        return response.json() if response.text else ""

    raise RequestException(
        f"Request to '{response.url}' failed" f" with status code {response.status_code}."
    )


def api_request(method: str, path: str = "", headers: dict = {}):
    """
    Encapsulates the logic of a simple request.
    """
    url = f"{env.API_BASE_URL}{path}"
    headers = {**DEFAULT_HEADERS, **headers}

    return requests.request(method=method, url=url, headers=headers)


def as_handler(func):
    """
    Converts a function that calls an API into a simple serverless handler.
    """

    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        data = get_response_data(response)

        return {
            "statusCode": response.status_code,
            "body": json.dumps(data),
        }

    return wrapper
