"""
Creator: Sylvia Zhao

Contributor: Wenxi Lei, Tian Wang
"""

import pandas.io.data as web
import datetime
from retrieve_dataexceptions import *
from retrieve_datacheck import *
from userfile_exceptions import *
import pandas as pd


def userfile_checkinput(string, start, end):
    """
    check if a valid input of the csv file and dates exists
    """
    input_list = [string, start, end]
    try:
        for x in input_list:
            valid_empty = empty_checkuser(x)
        if valid_empty == 0:
            valid_dates = dates_checkinput(start, end)
            valid_header = header_checkuser(string)
            if valid_dates == valid_header == 0:
                df = pd.read_csv(string, index_col = 0).dropna()
                df = df[start:end]
                return 0
    except (EmptyString, UserEmptyString, CannotRead, MissingHeader, ValueError, BadDate, BadTicker) as e:
        print e

def empty_checkuser(string):
    """
    check if a csv file exists
    """
    if len(string) == 0:
        raise UserEmptyString
    else:
        return 0

def read_checkuser(string):
    """
    try convert the csv file into pandas dataframe
    """
    try:
        df = pd.read_csv(string).dropna()
        return 0
    except:
        raise CannotRead
        
def header_checkuser(string):
    """
    check if they have the same header as online data
    """
    needed_headers = ['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
    missing = []
    if read_checkuser(string) == 0:
        df = pd.read_csv(string)
        try:
            col_headers = list(df.columns.values)
            for val in needed_headers:
                if val not in col_headers:
                    missing.append(val)
            if len(missing) == 0:
                return 0
            else:
                raise MissingHeader
        except:
            raise MissingHeader

