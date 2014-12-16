'''
Created on Dec 11, 2014

@author: Jiayi Lu, Minzi Ji, Lei Lu
'''
import pandas as pd
import numpy as np
import sys
import os
from ioprocess import *
from ioprocess.parsers import parseOptions, parseDates
import time


class UnixInterface():
    '''
    class definition of unix command line based UI
    >>>>
    In class UnixInterface:
    Internal Methods:
        1._cls : print system clear
    
    Public Methods:
        1.loading : print loading info
        2.done : print done when data preparation is finished
        3.welcome : print welcome message
        4.options : receive an integer as the option input (1-5 indicating different tasks)
        5.receiveDateRange : receives input for a date range
        6.finished : pop up user selection dialog when a task is accomplished

    '''
    def __init__(self):
        pass
    
    def _cls(self):
        os.system('clear')
    
    def loading(self):
        '''
        print a progress bar when operating on data
        '''
        self._cls()
        print 'Processing Data...'
        
    def done(self):
        print 'Done!'
            
    def welcome(self):
        '''
        print welcome message
        '''
        self._cls()
        try:
            f = open('./dat/welcome_unix_text.txt','r')
        except:
            print >> sys.stderr, 'Internal File Missing, Program Terminated!\n'
        try:
            welcome_page = f.readlines()
        except (EOFError,KeyboardInterrupt):
            print >> sys.stderr, 'File Reading Error\n'
        for line in welcome_page:
            print line
        
    def options(self):
        '''
        receive an integer as the option input, accepted values are 1-5
        '''
        option = safeInput('Your Input (Type exit or quit to terminate the program): ', ['exit','quit'],parseOptions)
        return option
    
    def receiveDateRange(self):
        '''
        receives input for a date range
        '''
        start_date = safeInput('Please Input The Start Date (MM-DD-YYYY): ', ['exit','quit'], parseDates)
        end_date = safeInput('Please Input The End Date (MM-DD-YYYY): ', ['exit','quit'], parseDates)
        return start_date, end_date
    
    def finished(self):
        '''
        pop up user selection dialog when a task is accomplished
        '''
        self._cls()
        print'Mission Accomplished! \nPress ctrl+C or ctrl+D to exit the program, press Enter key to return to the welcome window: \n'
        while True:
            key = safeInput('', ['exit','quit'], parseNothing)
            if key == '':
                return False
        return True