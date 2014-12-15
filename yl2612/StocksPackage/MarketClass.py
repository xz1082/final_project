'''
@author: Fangyun Sun
'''

import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt

class Market():
    '''
    Generate a class that can describe the market, 
    providing the percent change of close price for the comparison with stock.
    
    '''
    def __init__(self, starttime,endtime):
        '''
        Constructor:
        We use the input of start date and end date to obtain the market data from yahoo finance.
        In this case, the dates are all valid. Because we only use market class in the stock class functions.
        stock.starttime and stock.endtime has been checked.
        
        Input:
            starttime(datetime): the start time of date range
            endtime(datetime): the end time of date range
        
        Attributes:
            marketsymbol(string): the symbol of market used in the yahoo finance data.
            dataframe(pandas.dataframe): extract the data from the yahoo finance
            close_price(pandas.series): the column 'Adj Close' in the dataframe
        '''
        self.marketsymbol = '%5EGSPC'
        self.dataframe = web.DataReader(self.marketsymbol,'yahoo',starttime,endtime)
        self.close_price = self.dataframe['Adj Close']
    
    def change_price_percent(self):
        """
        Generate the percent change of daily close price.
        In this case, we compute the difference ratio between daily close price and first day price, 
        as the percentage of close price change.
        """
        market_firstday = self.close_price[0]
        self.dataframe['market_%chg'] = (self.close_price - market_firstday)/market_firstday
        change_price_percent = self.dataframe['market_%chg']
        return change_price_percent
    