"""
Creator: Sylvia Zhao

Contributor: Wenxi Lei, Tian Wang
"""


import pandas.io.data as web
import datetime
import pandas as pd

from userfile_checks import *

def userfile_read(string, start, end):
    valid_userfile = userfile_checkinput(string, start, end)
    if valid_userfile == 0:
        df = pd.read_csv(string, index_col = 0).dropna()
        df = df[start:end]
        return df