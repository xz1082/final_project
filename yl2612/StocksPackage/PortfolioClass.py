'''
Created on 2014.12.1

@author: Yunshi Li
'''

import numpy as np
import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
from Utilities.Inputfunctions import *
from Utilities.Exceptions import *
from Utilities.CheckInternet import *
from MarketClass import *
from StockClass import *
from collections import defaultdict
import matplotlib
from matplotlib.ticker import FuncFormatter

class Portfolio():
    '''
    Generate a class describe the portfolio containing several attributes and functions.
    
    '''
    
    def __init__(self,stock_company_list, start_date, end_date, amount_list):
        '''
        Constructor:
            
        Input:
            stock_company_list(list of strings): a list of the stock symbols from user input.
            start_date: the start date of the portfolio from user input.
            end_date: the end date of the portfolio from user input.
            amount_list = the trade amount of each stock
        
        Attributes:
            stock_company_list(list of strings): a list of the stock symbols.
            start_date(datetime): the start date of the portfolio.
            end_date(datetime): the end date of the portfolio.
            amount_list(list of strings): a list of the trade amount of each stock.
        '''
        
        self.stock_company_list = stock_company_list
        self.start_date = start_date
        self.end_date = end_date
        self.amount_list = amount_list
    
    def _pair_up(self):
        """
        This function is an internal function that only used in this class.
        Pair up the stocks with the amount,
        Return a dictionary that both stocks and trading volumes are not null.
        Raise EmptyPortfolioException when the stocks are all null and all the trading volumes are null or 0.
        """
        dictionary = dict(zip(self.stock_company_list, self.amount_list))
        delete_key_dictionary = {k: dictionary[k] for k in dictionary if not k==""} #delete stocks that are null
        delete_value_dictionary = {k: delete_key_dictionary[k] for k in delete_key_dictionary \
                                   if (delete_key_dictionary[k] != "" and ParseValidNum(delete_key_dictionary[k]) !=0)} #delete trading volumes that are null or 0.
        if IsEmptyPortfolio(delete_value_dictionary): #check if the portfolio is empty
            raise EmptyPortfolioException() 
        else:
            return delete_value_dictionary # return a dictionary that maps each stock and its trade amount.

    
    def _merge_same_stock(self):
        """
        This function is an internal function that only used in this class.
        This function takes a dictionary that maps the stocks and their trading volumes, adds the amount together if repetitive stock symbols exist.
        Return two list containing unique stock symbols and their corresponding trading volumes.
        """   
        raw_dictionary = self._pair_up()
        
        stock_amount_dictionary = defaultdict(int)
        for stock, amount in raw_dictionary.iteritems():
            stock_amount_dictionary[ParseStockName(stock)] += ParseValidNum(amount) #add the trade amount together if the two capitalized symbols are the same.
        unique_stock_company_list = stock_amount_dictionary.keys() #get a list of unique stocks
        trade_amount_list = stock_amount_dictionary.values() #get a list of trade amount corresponding to the stocks.
        return unique_stock_company_list, trade_amount_list
    
    def _get_portfolio_df(self):
        """
        This function is an internal function that only used in this class.
        Take a list of stock companies' symbols, a date range and the trade amount of each stock,
        return a dataframe showing each stock's and the total portfolio performance.
        """
        unique_stock_companies, trade_amount = self._merge_same_stock()
        stock_class_dict = {stock:Stock(stock,self.start_date,self.end_date) for stock in unique_stock_companies} #get valid stock symbols
    
        pricecols = {stock:stock_class.close_price for stock, stock_class in stock_class_dict.iteritems()} # get the closing price of each stock
        closed_price_df = pd.DataFrame(data=pricecols, columns=unique_stock_companies)
        portfolio = closed_price_df * np.array(trade_amount) # multiply each stock's price with its trading volume.
        portfolio_add_sum = portfolio.copy()
        portfolio_add_sum['Portfolio']= portfolio.sum(1) # create a column that adds up all the stock values, which is the portflio value.     
        return portfolio_add_sum

    def _portfolio_weight(self):
        """
        This function is an internal function that only used in this class.
        Calculate the weight of each stock in the portfolio each day by dividing each stock value by the portfolio value.
        """
        portfolio_df = self._get_portfolio_df()
        portfolio_weight_df = portfolio_df.div(portfolio_df['Portfolio'], axis='index')       
        return portfolio_weight_df
    
    def describe_portfolio(self):
        """
        Get descriptive statistics of the portfolio.
        """
        portfolio_df = self._get_portfolio_df()    
        describe_stat_df = portfolio_df.describe()
        describe_stat_df = describe_stat_df.rename(index = {'count':'trading days'})
        portfolio_weight_df = self._portfolio_weight()
        describe_stat_df.loc['start weight'] = portfolio_weight_df.ix[0]
        describe_stat_df.loc['end weight'] = portfolio_weight_df.ix[-1]
        
        stocks_return = portfolio_df.ix[-1] / portfolio_df.ix[0] -1
        describe_stat_df.loc['total return'] = stocks_return      
        return describe_stat_df
    
    def plot_portfolio(self):
        """
        Plot a graph showing the performance of the portfolio
        """
        portfolio_df = self._get_portfolio_df()
        plt.figure()
        portfolio_df['Portfolio'].plot(kind='line')
        plt.ylabel('Price')
        plt.title('Line plot for the overall portfolio performance')
        plt.show()
     
    def _percentage_change(self):
        """
        This function is an internal function that only used in this class.
	    Calculate the percentage change between the starting price and the daily price of the portfolio.
	    return a data frame of the percentage price change.
        """
        portfolio_df = self._get_portfolio_df()
        stock_firstday = portfolio_df.ix[0]
        percentage_change_df = (portfolio_df - stock_firstday)/stock_firstday
        return percentage_change_df
        
    def portfolio_value_change_compared_with_market(self):
        """
        Plot the percentage price change of the portfolio and of the actual market.
        """
        percentage_change_df = self._percentage_change()
        plt.figure()
        percentage_change_df['Portfolio'].plot(color = 'b',label = 'Portfolio')
        market = Market(self.start_date,self.end_date)
        market.change_price_percent().plot(color = 'r',label = 'Market')
        plt.legend()
        plt.xticks(rotation=45)
        plt.title('Portfolio performance compared with the market')
        plt.xlabel('Date')
        plt.ylabel('Percentage Change of Close Price')
        plt.show()
    
    def return_vs_risk(self):
        """
        Create a plot to examine the expected return and the risk tradeoff of each stock.
        Expected return is the average percentage change in price.
        Risk is the standard deviation of the percentage change over the period.
        """
        percentage_change_df = self._percentage_change()
        only_stocks_percentage_change_df = percentage_change_df[percentage_change_df.columns[:-1]]
        plt.figure()
        plt.scatter(only_stocks_percentage_change_df.std(), only_stocks_percentage_change_df.mean())
        plt.ylabel('Expected Return')
        plt.xlabel('Risk')
        for label, x, y in zip(only_stocks_percentage_change_df.columns, only_stocks_percentage_change_df.std(), only_stocks_percentage_change_df.mean()):
            plt.annotate(label, xy = (x, y),xytext = (10, 10), textcoords = 'offset points', horizontalalignment = 'right', verticalalignment = 'down', 
                         arrowprops = dict(arrowstyle = '<-'), bbox = dict(boxstyle = 'sawtooth', facecolor='red', alpha = 0.2)) #annotate each stock on the plot
        plt.title('Expected return versus risk')
        formatter = FuncFormatter(to_percent)
        plt.gca().yaxis.set_major_formatter(formatter) #make the y-axis in percentages.
        plt.show()
        plt.show()
         
    def stocks_value_change_corr(self):
        """
        get correlation of each stock's percentage price changes in the portflio.
        """
        percentage_change_df = self._percentage_change()
        stocks_price_change_corr = percentage_change_df[percentage_change_df.columns[:-1]].corr()
        return stocks_price_change_corr
    
    def heat_map(self):
        """
        Create a heat map to see the correlation among stocks in the portfolio.
        """
        stocks_price_change_corr = self.stocks_value_change_corr()
        plt.figure()
        #plt.imshow(stocks_price_change_corr, cmap='Blues', interpolation='none')
        plt.pcolor(stocks_price_change_corr,cmap='Blues')
        plt.colorbar()
        plt.xticks(np.arange(len(stocks_price_change_corr))+0.5, stocks_price_change_corr.columns)
        plt.yticks(np.arange(len(stocks_price_change_corr))+0.5, stocks_price_change_corr.columns)
        plt.title('Heat map of your portfolio stocks')
        plt.show()

    def moving_avg_50(self):
        """
        Plot a graph comparing the 50 days moving average price with the portfolio daily price.'
        """
        portfolio_df = self._get_portfolio_df()
        moving_average = pd.rolling_mean(portfolio_df['Portfolio'],50, min_periods=2)
        plt.figure()
        plt.plot(portfolio_df.index,moving_average, label='50 days moving average')
        plt.plot(portfolio_df.index,portfolio_df['Portfolio'], label='Portfolio daily price')
        plt.xticks(fontsize=6, rotation=45)
        plt.xlabel("Date")
        plt.ylabel('Price')
        plt.title('Moving average of 50 days V.S. portfolio price')
        plt.legend()
        plt.show()
