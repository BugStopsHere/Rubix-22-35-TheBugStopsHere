import requests
from urllib.parse import urlencode
from app import API_KEY


def extract_photo_references(places_id: list) -> list:
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    photo_references = []

    for place_id in places_id:
        params = {
            'place_id': place_id,
            'fields': 'photo',
            'key': API_KEY
        }

        encoded_params = urlencode(params)
        encoded_url = f"{url}?{encoded_params}"

        r = requests.get(encoded_url).json()
        res = r['result']
        photos = res['photos'][0] if 'photos' in res else None
        if photos:
            photo_references.append(
                photos['photo_reference']) if 'photo_reference' in photos else None

    return photo_references
