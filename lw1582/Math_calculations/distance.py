'''
Created by: Lucy Wang
Modified: Maya Rotmensch and Lucy Wang

referenced codes from http://www.johndcook.com/blog/python_longitude_latitude/
'''

import numpy as np


def distance(lat1, long1, lat2, long2):
    """ 
      The following function calculates the distance between two points based on each point's latitude and longitude.The distance is relative to Earth's radius, in miles.
      Args:
      lat1: string. latitude of user inputed address.
      long1: string. longitude of user inputed address.
      lat2: string. latitude for wifi connection we want to assess. 
      long2: string. longitude for wifi connection we want to assess. 

      Returns:
        arc: the distance between the two points given relative to the earth's radius.

        
    """ 
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = np.pi/180.0

    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
        
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
    cos = (np.sin(phi1)*np.sin(phi2)*np.cos(theta1 - theta2) + 
           np.cos(phi1)*np.cos(phi2))
    arc = np.arccos( cos ) * 3960
    
    return arc
