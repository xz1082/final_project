"""
Creator: Wenxi Lei

Contributor: Sylvia Zhao, Tian Wang
"""
import pandas.io.data as web
import datetime
from retrieve_datacheck import *
from retrieve_dataexceptions import *

def get_data(stock, source, start, end):
    try:
        valid_input = gui_checkinput(stock, source, start, end)
        source = source.lower()
        if valid_input == 0:
            start_year=int(start.split('/')[0])
            start_month=int(start.split('/')[1])
            start_day=int(start.split('/')[2])
            end_year=int(end.split('/')[0])
            end_month=int(end.split('/')[1])
            end_day=int(end.split('/')[2])
            start=datetime.datetime(start_year, start_month, start_day)
            end=datetime.datetime(end_year, end_month, end_day)
            f=web.DataReader(stock, source, start, end)
            return f
    except (EmptyString, BadSource, ValueError, BadDate, BadTicker) as e:
        print e       
