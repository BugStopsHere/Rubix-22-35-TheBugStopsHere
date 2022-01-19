import requests
from urllib.parse import urlencode
from functools import lru_cache
from app import API_KEY


@lru_cache(maxsize=10)
def extract_information(places_id: list) -> list:
    """
    Returns a list of dictionaries containing information about name, address,
    rating and phone number
    """
    info = []
    url_detail_endpoint = "https://maps.googleapis.com/maps/api/place/details/json"

    for place_id in places_id:
        params_detail = {
            'place_id': place_id,
            'fields': 'formatted_address,business_status,name,type,rating,formatted_phone_number,international_phone_number',
            'key': API_KEY}

        encoded_detail_params = urlencode(params_detail)
        encoded_url_detail = f"{url_detail_endpoint}?{encoded_detail_params}"

        r = requests.get(encoded_url_detail).json()
        res = r['result']
        info_dict = {"name": res.get('name'), "rating": res.get('rating'),
                     "address": res.get('formatted_address'),
                     "phone_no": res.get('formatted_phone_number')}
        info.append(info_dict)

    return info
