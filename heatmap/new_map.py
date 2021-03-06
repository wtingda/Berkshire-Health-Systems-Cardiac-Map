import random

import googlemaps
gmaps = googlemaps.Client(key="AIzaSyDE_MLUeIdpPgnCWEV-ZgscLCO1734Ax3w")


def calc_dist(start, end): # start and end are each a coordiate of (lat, long)
    d = gmaps.distance_matrix([str(start[0]) + " " + str(start[1])], [str(end[0]) + " " + str(end[1])], mode='walking')['rows'][0]['elements'][0]
    dist =  d['distance']['value']
    return {end: dist}

def find_nearest(patient_coord, topk=1):
    # dist = [geodesic(patient_coord, clinic).miles for clinic in clinics_coord]
    # dist = [calc_dist(patient_coord, clinic) for clinic in clinics_coord]
    dist = [calc_dist(patient_coord, clinic) for clinic in zip(clinics_lat, clinics_long)] # list of dicts
    # return sorted(dist)[:topk]
    return sorted(dist, key=lambda x: x.values()[0])

    
# tl = (42.745941, -73.264959)
# tr = (42.738711, -72.948854)
# print(calc_dist(tl, tr))

# # example
# origin_latitude = 12.9551779
# origin_longitude = 77.6910334
# destination_latitude = 28.505278
# destination_longitude = 77.327774
# distance = gmaps.distance_matrix([str(origin_latitude) + " " + str(origin_longitude)], [str(destination_latitude) + " " + str(destination_longitude)], mode='walking')['rows'][0]['elements'][0]
# print(distance)

# # geopy example
# from geopy.distance import geodesic
# newport_ri = (41.49008, -71.312796)
# cleveland_oh = (41.499498, -81.695391)
# print(geodesic(newport_ri, cleveland_oh).miles)

# from map import gmaps
# from map import patients_latitude, patients_longtitude, clinics_latitude, clinics_longtitude
# patients_coord = zip(patients_latitude, patients_longtitude)
# clinics_coord = zip(clinics_latitude, clinics_longtitude)
#
# # todo: could calculate once a 2d table/dict of distance btw each patient and each clinic
#
# def find_nearest(patient_coord, topk=1):
#     # dist = [geodesic(patient_coord, clinic).miles for clinic in clinics_coord]
#     return sorted(dist)[:topk]
#
# sample_patient = (42.073423320147626, -72.9493080716857)
# # sample_clinic =
# # print( find_nearest(sample_patient, 3) )
# for tup in clinics_coord:
#     print(tup)
