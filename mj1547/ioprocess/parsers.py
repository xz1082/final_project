'''
Created on Dec 11, 2014

@author: Jiayi Lu, Minzi Ji, Lei Lu
'''
import re
from excpshandle.userexcps import InvalidInputError, DateValueError
from pandas.index import Timestamp
import pandas as pd

def parseOptions(input_string):
    '''
    Validate option input and returns an integer indicating the operation to be accomplished, valid input includes number 1-4 with blank prefix or suffix of any length
    '''
    if re.match(re.compile(r'^\s*[1234]\s*$'),input_string):
        return int(input_string)
    else:
        raise InvalidInputError()
        return None

def parseDates(input_string):
    '''
    validate date input and returns an Timestamp
    '''
    #check if input string is a valid date
    date_string = pd.to_datetime(input_string)
    if type(date_string) == str:
        raise DateValueError()
    else:
        return date_string
        
def parseNothing(input_string):
    '''
    used for accepting arbitrary input to return to the welcome page after a task is accomplished
    '''
    return input_string