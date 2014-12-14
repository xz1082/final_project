'''
Created on 2014.12.1

@author: Fangyun Sun
'''
import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from MarketClass import *
from Utilities.Exceptions import *
from Utilities.Inputfunctions import *


class Stock():
    '''
    Generate a class that can describe the stock containing several attributes and functions.
    
    '''

    def __init__(self, stock,start,end):
        '''
        Constructor:
        Do a few checking the input with Utilities.inputfunctions.
        1. Check whether stock, start, end are null. If true, raise EmptyInputException.
        2. Check whether start and end date is a valid date form. If false, raise DateInputException.
        3. Check whether end date is before the current time. If false, raise EndDateException.
        4. Check whether end date is more than start date. If false, raise DateRangeException. 
           If the dates satisfy 2,3,4, we can parse the start and end date.
        5. Check whether stock is a valid stock name between the start date and end date, 
           which could be found in the yahoo finance data.
           If true, parse the stock into its upper form. Otherwise, raise StockNameInputException.
                
        Input:
            stock(string): the name of stock, can be read into pandas.io.data.DataReader
            start(string): the start time of date range from user input
            end(string): the end time of date range from user input
        
        Attributes:
            stock(string): the name of stock
            starttime(datatime): the start time of date range 
            endtime(datatime): the end time of date range 
            dataframe(pandas.dataframe): extract the data from the yahoo finance
            close_price(pandas.series): the column 'Adj Close' in the dataframe
        '''
        
        if IsEmptyInput(stock,start,end):
            raise EmptyInputException()
        else:
            if IsValidDate(start) and IsValidDate(end):
                if IsValidEndDate(end):
                    if IsValidDateRange(start,end): 
                        pass
                    else:
                        raise DateRangeException()
                    self.starttime = ParseDate(start)
                    self.endtime = ParseDate(end)
                else:
                    raise EndDateException()                
            else:
                raise DateInputException() 
            if IsValidStockName(stock,start,end):
                self.stock = ParseStockName(stock)
            else:
                raise StockNameInputException()  
                
        self.dataframe = web.DataReader(stock,'yahoo',start,end)
        self.close_price = self.dataframe['Adj Close']
        
    def change_price_percent(self):
        """
        This function is an internal function, only used in this class.
        Generate the percentage change of daily close price.
        In this case, we compute the difference ratio between daily close price and first day price, 
        as the percentage of close price change.
        """
        stock_firstday = self.close_price[0]
        self.dataframe['stock_%chg'] = (self.close_price - stock_firstday)/stock_firstday
        change_price_percent = self.dataframe['stock_%chg']
        return change_price_percent
    
    def plot_close_price(self):
        """
        Plot the stock close price over time.
        """
        fig = plt.figure()
        self.close_price.plot(color = 'b',label = self.stock)
        plt.legend()
        plt.xticks(rotation=45)
        plt.title('The Close Price of {} '.format(self.stock))
        plt.xlabel('Date Time')
        plt.ylabel('Close Price')
        plt.show()
    

    def plot_changeprice_comparison(self):
        """
        Compare and plot the percentage change of the stock close price and that of the actual market over time.
        """
        fig = plt.figure()
        self.change_price_percent().plot(color = 'b',label = self.stock)
        market = Market(self.starttime,self.endtime)
        market.change_price_percent().plot(color = 'r',label = 'S&P 500')
        plt.legend()
        plt.xticks(rotation=45)
        plt.title('The Comparison between {} and S&P 500 close price '.format(self.stock))
        plt.xlabel('Date Time')
        plt.ylabel('Percent Change of Close Price')
        
        # Create the formatter using the function to_percent. This multiplies all the
        # default labels by 100, making them all percentages
        formatter = FuncFormatter(to_percent)
        
        # Set the formatter
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.show()
        
    def close_price_describe(self):
        """
        Obtain all the statistics about stock close price, for example, min, max, mean etc..
        """
        return self.close_price.describe()
    
def to_percent(y, position):
    """
    Parse the y label in the plot to the percentage form.
    """
    
    s = str(100 * y)

    if matplotlib.rcParams['text.usetex'] == True:
        return s + r'$\%$'
    else:
        return s + '%'
    