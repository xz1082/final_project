"""
Creator: Sylvia Zhao

Contributor: Wenxi Lei, Tian Wang
"""


import pandas.io.data as web
import datetime
from retrieve_dataexceptions import *

def gui_checkinput(stock, source, start, end):
    """
    This function checks that the dataset can be loaded given the user
    inputs for stock, source, start, and end, after the following
    conditions have been validated:
    - none of the inputs are empty strings
    - the source is valid
    - the start and end dates are valid standard dates
    return 0 if valid
    raises the BadTicker if dataset cannot be loaded
    """
    input_list = [stock, source, start, end]
    try:
        for x in input_list:
            valid_empty = empty_checkinput(x)
        if valid_empty == 0:
            valid_source = source_checkinput(source)
            valid_dates = dates_checkinput(start, end)
            if valid_source == valid_dates == 0:
                df = web.DataReader(stock, source, start, end)
                return 0
    except (EmptyString, BadSource, ValueError, BadDate, BadTicker) as e:
        print e

def empty_checkinput(string):
    """
    This function checks user inputs for stock, source, start, and end
    to make sure that none of the categories are empty strings.
    return 0 if no empty strings exist
    raise EmptyString if empty string is found
    """
    if len(string) == 0:
        raise EmptyString
    else:
        return 0
    
def source_checkinput(source):
    """
    This function checks that the user inputs a valid source (yahoo or google),
    after calling empty_checkinput to ensure that source is not an empty string.
    return 0 if source is valid
    raise BadSource exception if source is invalid
    """
    valid_source = ['yahoo', 'google']
    try:
        if source.lower() in valid_source:
            return 0
        else:
            raise BadSource
    except:
        raise BadSource

def dates_checkinput(start, end):
    """
    This function checks that the user inputs for start and end dates are valid standard dates
    in the format of yyyy/mm/dd,
    after calling empty_checkinput to validate that start and end inputs are not empty strings.
    If the start and end dates are in correct format and exist, then they are converted to
    datetime.datetime and saved to the variables startdate and enddate.
    Else, ValueError is raised.
    return 0 if date range is valid
    raise BadDate if date range is invalid
    """
    currentdate = datetime.datetime.now()
    try:
        startdate = datetime.datetime.strptime(start, '%Y/%m/%d')
    except:
        raise ValueError("Bad start date. Please input valid start date in yyyy/mm/dd format.")
    try:
        enddate = datetime.datetime.strptime(end, '%Y/%m/%d')
    except:
        raise ValueError("Bad end date. Please input valid end date in yyyy/mm/dd format.")
    if startdate == enddate:
        raise BadDate('Start and end dates cannot be the same.')
    if startdate > enddate:
        raise BadDate('Start date cannot be after end date.')
    elif enddate > currentdate:
        raise BadDate('End date cannot be after today\'s date.')
    else:
        return 0