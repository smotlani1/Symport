from lib2to3.refactor import get_fixers_from_package
import os
import googlemaps
from googlemaps import distance_matrix
from datetime import datetime


# get_distance_zips uses a google API to return a distance, in miles, when provided with a start and destination zip code
# in string format. 

def get_distance_zips(origin_zip, dest_zip):
    #return api key store in local directory
    with open('/Users/sm/Desktop/comp sci/personal projects/APIkeys/GoogleAPI.txt') as f:
        api_key = f.readline()
        print(api_key)
        f.close

    gmaps = googlemaps.Client(key=api_key)
    distanceMatrix = gmaps.distance_matrix(origin_zip, dest_zip)
    distance_text = distanceMatrix['rows'][0]['elements'][0]['distance']['text'] #referncing the distance field from the matrix#
    distance = float(distance_text.split()[0].replace(',', ''))
    distance = distance * .621 #converts distance to miles#

    return distance


