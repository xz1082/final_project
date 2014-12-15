''''
Created by: Maya Rotmensch.
Modified by: Maya Rotmensch and Lucy Wang.
'''

class EmptyStringException(Exception):
    """Exception for when the user tries to input an empty string """
    pass

class UnreadableData(Exception):
    """ Exception for when the data file from NYC Open Data cannot be loaded. """
    pass

class NotInNYException(Exception):
    """ An exception for when the user attempts to search for an address outside of NYC. This exception may also be raised if the user searches for an invalid address that is auto corrected by geocoder to an address that's outside of NYC"""
    pass

class InvalidInputException(Exception):
    """ A general exception for when the user inputs an invalid address. Example of invalid input: 'sodufgbf'. """
    pass

class Address_not_valid(Exception):
    """This exeption is raised when the address the user provides can either not be converted or was found by the geocoder API to not be valid."""
    pass


