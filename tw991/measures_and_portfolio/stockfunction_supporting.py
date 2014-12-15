"""
Creator: Tian Wang

Contributor: Wenxi Lei, Sylvia Zhao
"""


from stockexception import *
import pandas as pd
import numpy as np


def basic_checkinput(series, length=0):
    """
    This function checks input series for sma function. When input is valid, it will return 0.
    raise InvalidinputData exception when input is invalid
    raise MultipleCol excecption when input data has multiple columns
    raise MAinvalidlength exception when input length is not a positive integer or it is larger than data length
    """
    try:
        data = pd.DataFrame(series)
        time_length = len(data)
    except:
        raise InvalidinputData
    if length != 0:
        if len(data.columns) > 1:  # input data has multiple columns
            raise MultipleCol
        elif length > time_length:  # input period length larger than data length
            raise Invalidperiodlength
        elif length <= 0 or not isinstance(length, int):  # input period is not a positive integer
            raise Invalidperiodlength
        else:
            return 0
    else:
        data_positive = (data >= 0)
        if len(data.columns) > 1:  # input data has multiple columns
            raise MultipleCol
        elif time_length > int(np.sum(data_positive)):
            raise Negativevalue
        else:
            return 0

def boll_checkinput(series, N, K):
    """
    This function checks input series for boll(series, N, K) function. When input is valid, it will return 0.
    raise InvalidInputData exception when input stock data is invalid.
    raise MultipleCol exception when input stock data has multiple columns
    raise BollinvalidN exception when N is not a positive integer
    raise BollinvalidK exception when K is not a positive number
    """
    if basic_checkinput(series, N) == 0:
        if not (isinstance(K, int) or isinstance(K, float)):  # input K is not a number
            raise BollinvalidK
        elif K < 0:  # input K is a negative number
            raise BollinvalidK
        else:
            return 0


def macd_checkinput(series, slow, fast):
    """
    This function checks input series for macd(series, slow, fast) function. When input is valid, it will return 0.
    """
    if basic_checkinput(series, slow) == 0 and basic_checkinput(series, fast) == 0:
        if fast >= slow:  # fast period is larger than slow period
            raise Macdinvalidperiod
        else:
            return 0


def daily_return_checkinput(series):
    """
    This function checks input series for daily_return(series) function. When input is valid, it will return 0.
    """
    if basic_checkinput(series) == 0:
        return 0


def sharpe_checkinput(series, period):
    """
    This function checks input series for sharpe(series, period) function. When input is valid, it will return 0.
    """
    if basic_checkinput(series, period) == 0:
        return 0