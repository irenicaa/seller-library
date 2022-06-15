from dataclasses import dataclass, field
from typing import Optional, Generator
import datetime

from dataclasses_json import dataclass_json, Undefined, config, CatchAll
from marshmallow import fields

import request_api
import credentials
import returns_fbs

# Request

@dataclass_json
@dataclass
class CountryFilter:
    name_search: Optional[str] = None

# Response

@dataclass_json
@dataclass
class GetPostingFBSProductCountryListResponseResult:
    name: str
    country_iso_code: str

@dataclass_json
@dataclass
class GetPostingFBSProductCountryListResponseResultWrapper:
    result: list[GetPostingFBSProductCountryListResponseResult]

def get_posting_fbs_product_country_list(
    credentials: credentials.Credentials,
    data: CountryFilter,
) -> GetPostingFBSProductCountryListResponseResultWrapper:
    response = request_api.request_api_raw(
        'POST',
        '/v2/posting/fbs/product/country/list',
        credentials,
        data.to_json(),
    )
    return GetPostingFBSProductCountryListResponseResultWrapper.schema().loads(response)
