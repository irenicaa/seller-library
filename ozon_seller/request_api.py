import json
from typing import Optional

import requests

from . import credentials


def request_api_raw(
    method: str,
    endpoint: str,
    credentials: credentials.Credentials,
    data: Optional[str],
) -> requests.models.Response:
    session = requests.Session()
    response = session.request(
        method,
        "https://api-seller.ozon.ru" + endpoint,
        headers=credentials.to_headers(),
        data=data,
    )
    response.raise_for_status()
    return response
