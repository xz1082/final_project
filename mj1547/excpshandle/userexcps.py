'''
Created on Nov 6, 2014

@author: Jiayi Lu
'''
from exceptions import *

class InvalidInputError(Exception):
    '''
    raised when invalid input is received
    '''
    pass

class FileExtensionError(Exception):
    '''
    raised when the extension format of the file is prohibited
    '''
    pass

class FileNamingError(Exception):
    '''
    raised when filename contains invalid chars
    '''
    pass

class DateRangeError(Exception):
    '''
    raised when invalid date range is detected, e.g. exceeding date range limit in the data set or start_date > end_date
    '''
    pass

class DateValueError(Exception):
    '''
    raised when invalid date input are received
    '''
    pass

class TypeClassError(Exception):
    '''
    raised where variable selection fails
    '''
    pass

class EmptyDataframeError(Exception):
    '''
    raised when an empty dataframe is generated
    '''
    pass