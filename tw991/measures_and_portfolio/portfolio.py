"""
Creator: Tian Wang

Contributor: Wenxi Lei, Sylvia Zhao
"""

from stockfunction import *
from portfoliofunction import *
from stockexception import *
import datetime
from data_process.retrieve_data import get_data


class portfolio():
    """
    This class defines a stock investment portfolio and calculates its return over a period of time.

    Parameters:
    stock_ticker_list: list (eg. ['ADBE','F'])
        Used to specify the stocks used in portfolio

    starting_cash: float (default = 10000)
        Amount of money used in portfolio

    Attributes:
    stock_ticker_list: list (eg. ['ADBE','F'])
        Used to specify the stocks used in portfolio

    start_price_list: pandas.DataFrame
        Used to store the close price of all stocks in the portfolio on the start day

    end_price_list: pandas.DataFrame
        Used to store the close price of all stocks in the portfolio on the end day

    start_value: float
        Used to store the amount of invested money in the portfolio

    end_value: float
        Used to store the amount of money after the simulation is run over a period of time

    position: list
        Used to store the percentage of money invested on each stock after set_position() method is called.

    start_time: datetime
        Used to store the datetime of starting day of the portfolio

    end_time: datetime
        Used to store the datetime of end day of the portfolio


    Methods:
    simulate(position_list, start_time, end_time):
        Simulate return of a portfolio over a period of time.
        It will buy the stocks in portfolio according to position_list on the start_time, and sell all of them on the
        end_time.

        Parameters:
            position_list: list, length = number of stocks
                The input list of the percentage of money invested in each stock
                eg: [0.2, 0.8]

            start: string, 'year/month/day'
                Used to specify the starting date of portfolio.
            end: string, 'year/month/day'
                Used to specify the end date of portfolio.

        Returns:
            end_value: float
                The value of portfolio on the end date.




    """
    def __init__(self, stock_ticker_list, starting_cash = 10000):
        self.stock_ticker_list = stock_ticker_list
        self.start_price_list = []
        self.end_price_list = []
        self.start_value = float(starting_cash)
        self.end_value = 0
        self.position = False
        self.start_time = False
        self.end_time = False

    def _position_checkinput(self, position_list, ticker_list):
        #check whether position input is a valid list of allocation percentage of money in each stock
        if len(position_list) != len(ticker_list):
            raise Invalidposition
        if np.sum(position_list) > 1:
            raise Invalidposition
        return 0

    def _get_portfolio_data(self):
        #get Close price in starting day and end day for each stock in portfolio
        for stock in self.stock_ticker_list:
            temp_data = get_data(stock, 'yahoo', '%d/%d/%d' %(self.start_time.year, self.start_time.month, self.start_time.day), '%d/%d/%d' %(self.end_time.year, self.end_time.month, self.end_time.day))
            start_data = temp_data['Close'].ix[0]
            end_data = temp_data['Close'].ix[len(temp_data)-1]
            self.start_price_list.append(start_data)
            self.end_price_list.append(end_data)
        self.start_price_list = pd.DataFrame(self.start_price_list, index = self.stock_ticker_list)
        self.end_price_list = pd.DataFrame(self.end_price_list, index = self.stock_ticker_list)

    def _set_simulatetime(self, start, end):
        #set start_time and end_time by valid datetime
        self.start_time, self.end_time = get_simulate_date(start, end)

    def _set_position(self, position_list):
        #set position attribute with a valid position list
        if self._position_checkinput(position_list, self.stock_ticker_list) == 0:
            self.position = pd.DataFrame(position_list, index = self.stock_ticker_list)

    def simulate(self, position_list, start, end):
        #Simulate return of a portfolio over a period of time.
        #It will buy the stocks in portfolio according to position_list on the start_time, and sell all of them on the
        #end_time.
        self._set_position(position_list)
        if not len(self.position):
            raise Undefinedposition
        self._set_simulatetime(start, end)
        self._get_portfolio_data()
        share_list = (self.position * self.start_value)/self.start_price_list
        end_value_list = share_list*self.end_price_list
        self.end_value = float(end_value_list.sum())
        return self.end_value






