from lib2to3.refactor import get_fixers_from_package
import os
import googlemaps
from googlemaps import distance_matrix
from datetime import datetime


def get_distance_zips(origin_zip, dest_zip):
    with open('/Users/sm/Desktop/comp sci/personal projects/APIkeys/GoogleAPI.txt') as f:
        api_key = f.readline()
        print(api_key)
        f.close

    gmaps = googlemaps.Client(key=api_key)
    distanceMatrix = gmaps.distance_matrix(origin_zip, dest_zip)
    distance_text = distanceMatrix['rows'][0]['elements'][0]['distance']['text']
    distance = float(distance_text.split()[0].replace(',', ''))
    distance = distance * .621

    return distance


