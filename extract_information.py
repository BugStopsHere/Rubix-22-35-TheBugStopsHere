import os
from typing import Optional, Iterable
import asyncio
import httpx

API_KEY = os.environ.get('API_KEY')
client = httpx.AsyncClient()

async def gmaps_request(
        method,
        endpoint: str,
        params: dict[str, str],
        location: tuple[float, float] = None,
        **kwargs) -> httpx.Response:
    base = "https://maps.googleapis.com/maps/api/"
    url = base + endpoint.removeprefix("/")
    params = dict(key=API_KEY, **params)
    if location is not None:
        params["location"] = f"{location[0]}%2C{location[1]}"

    return await client.request(method, url, params=params, **kwargs)


async def get_place_info(place_id) -> dict[str, Optional[str]]:
    params = {
        "place_id": place_id,
        "fields": "formatted_address,business_status,name,type,rating,formatted_phone_number,international_phone_number",
    }
    url_detail_endpoint = "/place/details/json"
    response = await gmaps_request("GET", url_detail_endpoint, params=params)
    res = response.json()["result"]
    return {
        "name": res.get("name"),
        "rating": res.get("rating"),
        "address": res.get("formatted_address"),
        "phone_no": res.get("formatted_phone_number")
    }


async def extract_information(places_id: Iterable) -> list[dict[str, Optional[str]]]:
    coros = [get_place_info(place_id) for place_id in places_id]
    return await asyncio.gather(*coros)
