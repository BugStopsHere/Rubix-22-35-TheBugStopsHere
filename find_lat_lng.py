import googlemaps

API_KEY = YOUR_API_KEY
gmaps = googlemaps.Client(key=API_KEY)

def find_lat_lng(location: str) -> tuple[float, float]:
    """
    Returns the latitude and longtitude of the given location.
    Location can be an address, a station, a city, or even a country
    but country isn't preferred.
    """
    geocode_result = gmaps.geocode(location)
    try:
        location = geocode_result[0]['geometry']['location']
    except IndexError:
        return None, None
    lat = location['lat']
    lng = location['lng']

    return lat, lng
