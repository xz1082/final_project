'''
December 4, 2014

@author: Lucy Wang
'''

from pygeocoder import Geocoder
from pygeolib import GeocoderError
import __builtin__

def user_location(address):
  '''
    This function uses the pygeocoder.Geocoder module to reformat an user input into the suggested format by Google  
      The format is as follow: House_Number Street_Address, City, State Zip_Code, Country

    Args: 
      address: string, user input address
    
    Returns:
      address_state.formatted_address: string, reformatted address
  '''
  # if original string does not contain variation of NY, add in the string to make sure the addressed searched for is definitely in NYC.
  state_city = set(['new york','New York','ny','NY','Ny','New york','new York'])
  if __builtin__.any(keyword in address for keyword in state_city):
    address_state = Geocoder.geocode(address)
  else:
    address_state = Geocoder.geocode(address + "New York")
  
  return address_state.formatted_address


