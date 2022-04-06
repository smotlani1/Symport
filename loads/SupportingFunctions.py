from http import server
import googlemaps
from django.conf import settings


# get_distance_zips uses a google API to return a distance, in miles, when provided with a start and destination zip code
# in string format. 

def get_distance_zips(origin_zip, dest_zip):
    #return api key store in local directory
    api_dir = settings.GOOGLE_API_KEY
    with open(api_dir) as f:
        api_key = f.readline()
        print(api_key)
        f.close

    gmaps = googlemaps.Client(key=api_key)
    distanceMatrix = gmaps.distance_matrix(origin_zip, dest_zip)
    distance_text = distanceMatrix['rows'][0]['elements'][0]['distance']['text'] #referncing the distance field from the matrix#
    distance = float(distance_text.split()[0].replace(',', ''))
    distance = distance * .621 #converts distance to miles#

    return distance


