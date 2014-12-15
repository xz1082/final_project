'''
Created on 2014.12.1

@author: Fangyun Sun
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from StockClass import *
import matplotlib.cm as cm
from Utilities.Exceptions import *

def check_stock_names(stock_name_list):
    """
    Check whether the list of stock names is valid. Delete the duplicates of the stock names and null.
    """
    
    #Parse the stock name in its upper form.
    stock_name_list = [x.upper() for x in stock_name_list]
    unique_names = list(set(stock_name_list))
    if len(unique_names) == 1 and '' in unique_names:
        raise EmptyInputException()
    else:
        return [x for x in unique_names if x]
    
def multistocks_percentchange(stock_name_list,start,end):
    """
    Check the validity of the stock_name_list. Put every stock name into the StockClass.
    Use the function change_price_percent from StockClass to plot the percentage change of close price.
    """
    unique_stocks = check_stock_names(stock_name_list)
    length = len(unique_stocks)
    colors=cm.rainbow(np.linspace(0,1,length))
    stock_class_list = [Stock(stock,start,end) for stock in unique_stocks]
    i=0
    for item in stock_class_list:
        item.change_price_percent().plot(color =colors[i], label = item.stock)
        i = i+1
    plt.xticks(rotation=45)
    plt.legend()
    plt.xlabel('Date Time')
    plt.ylabel('Percent Change of Close Price')
    plt.title('The Percent Change Comparison between stocks')
    # Create the formatter using the function to_percent. This multiplies all the
    # default labels by 100, making them all percentages
    formatter = FuncFormatter(to_percent)
    
    # Set the formatter
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.show()
