'''
Created by: Maya Rotmensch
Modified by: Maya Rotmensch and Lucy Wang.
'''

import unittest
from userInterface.userInput import *



class TestUserInterface(unittest.TestCase):
    """ unittest class for user interaction functions in NearestWiFi program
    
    >>>>
        Attributes:
            1) user_input_valid1 : example of acceptable user input 
            2) user_input_valid2 : example of acceptable user input 
            3) user_input_invalid1 : example of unacceptable input for which we expect geocoder to find 0 results.
            4) user_input_invalid2 : example of unacceptable input for which we expect geocoder to find 0 results.
            5) user_input_invalid3: an example of input which the geocoder might be able to autocorrect, but will register as invalid. 
            6) user_input_invalid4: an example of input which the geocoder might be able to autocorrect, but will register as invalid.

        Methods:
            1) setUp
            2) test_parse_user_input
         
    """

    def setUp(self):
        """
        sets up class attributes for later use.
        """

        #correct input format
        self.user_input_valid1 = "304 east 93rd street" 
        self.user_input_valid2 =  "304 e 93rd st"

        #we expect the geocoder not to find any results --> geocoderError
        self.user_input_invalid1 = " "
        self.user_input_invalid2 = "easdjb"
        

        #we expect the geocoder to be able to find an address, however format is invalid --> Address_not_valid
        self.user_input_invalid3 = "4"
        self.user_input_invalid4 = "alabama"


    def test_parse_user_input(self):
        """  test the raised errors of string input by user"""

        convert_address(self.user_input_valid1)
        convert_address(self.user_input_valid2)

        self.assertRaises(GeocoderError, convert_address, self.user_input_invalid1)
        self.assertRaises(GeocoderError, convert_address, self.user_input_invalid2)

        self.assertRaises(Address_not_valid, convert_address, self.user_input_invalid3)
        self.assertRaises(Address_not_valid, convert_address, self.user_input_invalid4)
        



if __name__ == '__main__':
    unittest.main()