'''
Created by Lucy Wang
Modified by: Maya Rotmensch and Lucy Wang

'''
import re
import sys
from pygeocoder import Geocoder
from pygeolib import GeocoderError

from geoCoding.geoCoding import user_location
from customExceptions.customExceptions import *


    
def get_manual_input():
  ''' this function takes an input from the user.
    Args:
      None.
    Returns:
      string of user input.
  '''
  address_input = raw_input('Address to search: ')
  if address_input == "":
    raise EmptyStringException

  if address_input == "exit":
    sys.exit(1)

  return address_input

def convert_address(address_input):
  ''' this function converts an inputed address into a geocoder formatted address and coordinates. user_location and get_coordinates are functions built in the geoCoding module.

    Args:
      address_input: string. user input.

    Returns:
      address: object. the corrected (and sometimes autocorrected) address ,that was originally inputed by the user, in a geoCoding format. The address will only be autocorrected if no matching address is found. the object contains other helpful attributes such as validity of address, city, state, etc.

  ''' 
  address = Geocoder.geocode(address_input)

  if address.valid_address != True:
    raise Address_not_valid(Exception)

  address = user_location(address_input)


  return address

     
