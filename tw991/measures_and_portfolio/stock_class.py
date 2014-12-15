"""
Creator: Wenxi Lei

Contributor: Tian Wang, Sylvia Zhao
"""


import pandas as pd
import numpy as np
from stockexception import *
from stockfunction_supporting import *


class stock:
    """
    Method:
        sma(series, length):
            It calculates simple moving average of a number series with period=length.

            Parameters:
                series: pandas.Series
                    The input number series
                length: int
                    The period to calculate simple moving average

            Returns:
                A series with name = series.name + '_sma_' + str(length), index = series.index.


        std(series, length):
            It calculates moving standard deviation of a number series with period=length.

            Parameters:
                series: pandas.Series
                    The input number series
                length: int
                    The period to calculate moving standard deviation

            Returns:
                A series with name = series.name + '_std_' + str(length), index = series.index


        boll(series, series, N=20):
            It computes Bollinger Bands for N days with 1 standard deviation factor. Upper band at 1 standard deviation
            above the N-period moving average. Lower band at 1 standard deviation under the N-period moving average.

            Parameters:
                series: pandas.Series
                    The input number series
                N: int (default = 20)
                    The period to calculate Bollinger Bands

            Returns:
                a dataframe with three columns 'col(series)_boll_N_K_Upper', 'col(series)_boll_N_K_Lower'
                and 'col(series)_boll_N_K_Mean'


        macd(series):
            It computes MACD indicator with slow period=20 and fast period=5.

            Parameters:
                series: pandas.Series
                    The input number series

            Returns:
                Series with name 'col(series)_macd_20_5'


        daily_return(series):
            It computes daily return by calculating (close[day]-close[day-1])/close[day-1]

            Parameters:
                series: pandas.Series
                    The input number series

            Returns:
                Series with name 'return'


        sharpe(series, period):
            It computes moving sharpe ratio in a time period by calculating return(period)/std(daily_return(period))

            Parameters:
                series: pandas.Series
                    The input number series
                period: int
                    The period to use to calculate sharpe ratio

            Returns:
                Series with name 'sharpe'

    """
    def __init__(self, name):
        self.name=name
    
    def sma(self, series, length):
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


    def std(self, series, length):
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


    def boll(self, series, N=20):
        """
        This function computes Bollinger Bands for N days with K standard deviation factor. It returns a dataframe with
        three columns 'col(series)_boll_N_K_Upper', 'col(series)_boll_N_K_Lower' and 'col(series)_boll_N_K_Mean'
        Upper band at K times an N-period standard deviation above the N-period moving average
        Lower band at K times an N-period standard deviation under the N-period moving average
        N=20 and K=1 are most widely used
        """
        K=1
        if boll_checkinput(series, N, K) == 0:
            data = pd.DataFrame(series)
            boll_mean_name = str(list(data.columns)[0]) + '_boll_' + str(N) + '_' + str(K) + '_Mean'
            boll_upper_name = str(list(data.columns)[0]) + '_boll_' + str(N) + '_' + str(K) + '_Upper'
            boll_lower_name = str(list(data.columns)[0]) + '_boll_' + str(N) + '_' + str(K) + '_Lower'
            data[boll_mean_name] = self.sma(series, N)
            data[boll_lower_name] = data[boll_mean_name] - K * self.std(series, N)
            data[boll_upper_name] = data[boll_mean_name] + K * self.std(series, N)
            return data[[boll_upper_name, boll_lower_name, boll_mean_name]]


    def macd(self, series):
        """
        This function computes MACD indicator for slow period and fast period. It returns a series with name 'col(series)_macd_slow_fast'
        """
        slow=20 
        fast=5
        if macd_checkinput(series, slow, fast) == 0:
            data = pd.DataFrame(series)
            macd_name = str(list(data.columns)[0]) + '_macd_' + str(slow) + '_' + str(fast)
            data[macd_name] = self.sma(series, slow) - self.sma(series, fast)
            return data[macd_name]


    def daily_return(self, series):
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


    def sharpe(self, series, period):
        """
        This function takes in daily_return series and period to calculate sharpe ratio. It returns a series with name 'sharpe'
        """
        if sharpe_checkinput(series, period) == 0:
            data = pd.DataFrame(series)
            close_column = list(data.columns)[0]
            d_return = self.daily_return(series)
            time_length = len(data)
            sharpe_name = 'sharpe'
            data[sharpe_name] = np.nan
            for i in range(0, time_length - period + 1):
                period_return = float((data[close_column].ix[period-1+i] - data[close_column].ix[i]))/float(data[close_column].ix[i])
                period_return_std = np.std(d_return[i+1:period+i])
                data[sharpe_name].ix[period-1+i] = round(period_return/period_return_std, 3)
            return data[sharpe_name]

    