import googlemaps
from urllib.parse import urlencode
import os

API_KEY = os.environ.get('API_KEY')
gmaps = googlemaps.Client(key=API_KEY)


def get_image_urls(photo_references: list) -> list:
    url = "https://maps.googleapis.com/maps/api/place/photo"
    image_urls = []

    for photo_ref in photo_references:
        params = {
            "photo_reference": photo_ref,
            "key": API_KEY,
            "maxwidth": 600,
            "maxheight": 600
        }
        encoded_params = urlencode(params)
        encoded_url = f"{url}?{encoded_params}"
        image_urls.append(encoded_url)

    return image_urls
