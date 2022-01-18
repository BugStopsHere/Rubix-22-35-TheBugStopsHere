import requests
from urllib.parse import urlencode

API_KEY = "YOUR_API_KEY"

def extract_information(places_id: list) -> tuple[list, list, list, list]:
    """
    Returns names, address ratings and phone number(if given) of all the places of which ids are given in places_id
    """
    names = []
    addresses = []
    ratings = []
    phone_nos = []
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

        names.append(res['name']) if "name" in res else None
        ratings.append(res['rating']) if "rating" in res else None
        addresses.append(res['formatted_address']
                         ) if "formatted_address" in res else None
        phone_nos.append(res['formatted_phone_number']
                         ) if "formatted_phone_number" in res else None

    return names, addresses, ratings, phone_nos
