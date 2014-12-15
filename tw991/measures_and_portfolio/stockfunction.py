"""
Creator: Tian Wang

Contributor: Wenxi Lei, Sylvia Zhao
"""


import pandas as pd
import numpy as np
from stockexception import *
from stockfunction_supporting import *


def sma(series, length):
    """
    This function computes simple moving average(sma) with period = length and return a new series with name 'col(series)_sma_length'
    raise InvalidinputData exception when input is invalid
    raise MultipleCol excecption when input series has multiple columns
    raise MAinvalidlength exception when input length is not integer or it is larger than data length
    """
    if basic_checkinput(series, length) == 0:
        data = pd.DataFrame(series)
        time_length = len(data)
        sma_name = str(list(data.columns)[0]) + '_sma_' + str(length)
        data[sma_name] = np.nan
        for i in range(0, time_length - length+1):
            data[sma_name].ix[length-1+i] = np.mean(data[data.columns[0]].ix[i:i+length])
        return data[sma_name]


def std(series, length):
    """
    This function computes standard deviation(std) with period = length and return a new series with name 'col(series)_std_length'
    raise InvalidinputData exception when input is invalid
    raise MultipleCol excecption when input series has multiple columns
    raise MAinvalidlength exception when input length is not integer or it is larger than data length
    """
    if basic_checkinput(series, length) == 0:
        data = pd.DataFrame(series)
        time_length = len(data)
        std_name = str(list(data.columns)[0]) + '_std_' + str(length)
        data[std_name] = np.nan
        for i in range(0, time_length - length+1):
            data[std_name].ix[length-1+i] = np.std(data[data.columns[0]].ix[i:i+length])
        return data[std_name]


def boll(series, N=20, K=1):
    """
    This function computes Bollinger Bands for N days with K standard deviation factor. It returns a dataframe with
    three columns 'col(series)_boll_N_K_Upper', 'col(series)_boll_N_K_Lower' and 'col(series)_boll_N_K_Mean'
    Upper band at K times an N-period standard deviation above the N-period moving average
    Lower band at K times an N-period standard deviation under the N-period moving average
    N=20 and K=1 are most widely used
    """
    if boll_checkinput(series, N, K) == 0:
        data = pd.DataFrame(series)
        boll_mean_name = str(list(data.columns)[0]) + '_boll_' + str(N) + '_' + str(K) + '_Mean'
        boll_upper_name = str(list(data.columns)[0]) + '_boll_' + str(N) + '_' + str(K) + '_Upper'
        boll_lower_name = str(list(data.columns)[0]) + '_boll_' + str(N) + '_' + str(K) + '_Lower'
        data[boll_mean_name] = sma(series, N)
        data[boll_lower_name] = data[boll_mean_name] - K * std(series, N)
        data[boll_upper_name] = data[boll_mean_name] + K * std(series, N)
        return data[[boll_upper_name, boll_lower_name, boll_mean_name]]


def macd(series, slow, fast):
    """
    This function computes MACD indicator for slow period and fast period. It returns a series with name 'col(series)_macd_slow_fast'
    """
    if macd_checkinput(series, slow, fast) == 0:
        data = pd.DataFrame(series)
        macd_name = str(list(data.columns)[0]) + '_macd_' + str(slow) + '_' + str(fast)
        data[macd_name] = sma(series,fast) - sma(series, slow)
        return data[macd_name]


def daily_return(series):
    """
    This function computes daily return. It returns a series with name 'return'
    """
    if daily_return_checkinput(series) == 0:
        data = pd.DataFrame(series)
        data_name = list(data.columns)[0]
        time_length = len(data)
        return_name = 'return'
        data[return_name] = np.nan
        for i in range(1, time_length):
            data[return_name].ix[i] = float(float(data[data_name].ix[i]-data[data_name].ix[i-1])/data[data_name].ix[i-1])
        return data[return_name]


def sharpe(series, period):
    """
    This function takes in daily_return series and period to calculate sharpe ratio. It returns a series with name 'sharpe'
    """
    if sharpe_checkinput(series, period) == 0:
        data = pd.DataFrame(series)
        data_name = list(data.columns)[0]
        time_length = len(data)
        sharpe_name = 'sharpe'
        data[sharpe_name] = np.nan
