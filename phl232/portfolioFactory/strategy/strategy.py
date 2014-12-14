
"""
Strategy is a module that defines the strategy class

Author: Israel Malkin
"""



import pandas as pd
import numpy as np
import warnings
import portfolioFactory
from ..utils import customExceptions as customExceptions
from ..utils.utils import setParameters


class strategy(object):
    ''' Strategy is a class to represent investment strategies. 
    
    This class contains returns generated by the strategy and associated metadata.
    
    A strategy is defined by:
        - the investment universe on which the strategy is defined
        - the signal used to make investment decisions (user supplied)
        - the selection rule which defines which investments to buy based on the signal 
        - these 3 components are used to generate the value of that
        
    
    Public Attributes:
        Data attributes:
        - signal: dataframe containing the signal used to select stocks (example: rolling returns)
        - selection: dataframe of zeros and ones to identify the selected investments
        - weights: dataframe containing the weights allocated to each selected investment
        - strategy: dataframe with the value of each investment and the total value ('value')
        - parameters: dictionary containing metadata
        
        Parameters Dictionary:
        - universe: the name of universe object on which the strategy is defined
        - signalPath: path to pickled dataframe with signal data
        - rule: the cutoff point for selecting investments
        - window: size of window between rebalancing 
        
     Example Config File:
         name = Name of strategy  (string)
         signalPath = Path specifying location of signal data (string)
         rebalanceWindow = The number of period between rebalancing the investments (int)
         rule = The number of investments to buy in each period (int)
         
                If rule is positive --> Buy the top X investments based on the signal
                If rule is negative --> Buy the bottom X investments based on the signal
        
    '''
    
    def __init__(self,universe,configPath):
        ''' Method to intialize a strategy object
        
            1) Reads in parameters from configPath      
            2) Sets signal as attribute
            3) Selects investments based on signal and sets as attribute
            4) Calculates weights ands sets as attribute
            5) Calculates strategy values and sets as attribute
            
        Args:
            configPath (str): location of config file
            universe (universe): universe on which the strategy is defined 
          
        '''
        
        # pull parameters from config file
        self.parameters = setParameters(configPath)
        self.parameters['universe']=universe.name
        
        
        # verify input
        self.__verifyUserInput(universe)
        
        # pull signal data
        self.__pullSignal()
        
        # check date overlap between returns and signal data
        self.__checkOverlap() 
        
        # set attributes 
        self.__makeSelection()
        self.__setWeights()
        self.__calcRebalance()
        
    def __verifyUserInput(self,universe):
        """ Method to verify the user input via the config file is proper
        
            Ensure that:
            - universe (first argument) passed is a universe object
            - config file has all the required inputs
            - config file does not have any unexpected inputs
            - rebalanceWindow parameter is a positive integer
            - rule parameter is an integer
            
            If any of these checks fail, the proper exception is raised informing the user of the issue.
        
        """
        
        # 1) make sure that passed universe is a universe object
        if isinstance(universe,portfolioFactory.universe.universe.universe)==False:
            raise customExceptions.notUniverseObject
        else:
            self._fullReturns = universe.assetReturns.copy()
            
            # print universe info
            print "\nUniverse for this strategy contains "+str(universe.assetReturns.shape[1])+" stocks... \n"
            
        # 2) make sure config file has necessary inputs
        expectedInputs = ['name','signalPath', 'rule','rebalanceWindow','universe']
        
        for inp in expectedInputs:
            if str(inp) not in self.parameters.keys():
                raise customExceptions.missingInput(inp) 
                
        for inp in self.parameters.keys():
            if str(inp) not in expectedInputs:
                raise customExceptions.unexpectedInput(inp)
                
        # 3) ensure window is numeric
        try:
            self._window = int(self.parameters['rebalanceWindow'])
        except ValueError:
            raise customExceptions.windowNotInt()
            
        if self._window<1:
            raise customExceptions.windowNegative(self._window)
            
        # 3) ensure rule is numeric
        try:
            self._rule = int(self.parameters['rule'])
        except ValueError:
            raise customExceptions.ruleNotInt(self.parameters['rule'])
            
        # print confirmation of input
        print "Inputs specified in strategy config file have been verified... \n"
        
        # print porfolio setup 'textbox'
        print "\n ==================== CALCULATING STRATEGY ======================= \n"
        print " universe         : "+self.parameters['universe']
        print " strategy name    : "+self.parameters['name']
        print " signal file      : "+self.parameters['signalPath']
        print " rebalance window : "+self.parameters['rebalanceWindow']
        if self._rule<0:
            print " selection rule   : "+"bottom "+self.parameters['rule']
        else:
            print " selection rule   : "+"top "+self.parameters['rule']
        print "\n ================================================================= \n"
        
            
    def __pullSignal(self):
        """ Method to set self.signal
        
            Returns the pickled dataframe containing signal data from the location (signalPath) specified in the config file.
            Returns an error if the file is not found in the specified path.
        
        """
        
        try:  
            self._fullSignal = pd.read_pickle(self.parameters['signalPath'])
            print "The signal data frame has been loaded... \n"
        except IOError:
            raise customExceptions.invalidSignalPath(self.parameters['signalPath'])
        
    def __checkOverlap(self):
        """ Method to extract overlap between signal and assetReturns data
        
           Result:
           Sets self.signal as a dataframe with the signal data for the dates and tickers where assetRetruns and signal data overlap.
           If there is no overlap between the two datasets either in terms of dates or ticker, an exception is raised.
           
        """
        
        # obtain dates of overlap (ensure intersection exists)
        beginOverlap = (self._fullSignal.index).intersection(self._fullReturns.index).min()
        endOverlap = (self._fullSignal.index).intersection(self._fullReturns.index).max()
        if isinstance(beginOverlap,pd.tslib.NaTType) or isinstance(beginOverlap,pd.tslib.NaTType):
            raise customExceptions.noTimeOverlap
        
        # obtain overlapping ticker  (ensure intersection exists)
        tickerOverlap = list(set(self._fullSignal.columns).intersection(set(self._fullReturns.columns)))
        if len(tickerOverlap)==0:
            raise customExceptions.noTickerOverlap
            
        
        
        self._tickers = tickerOverlap
        self._returns = self._fullReturns.ix[beginOverlap:endOverlap][self._tickers]
        self._rebalanceDates = self._returns.index[::self._window]
        self.signal = self._fullSignal.ix[self._rebalanceDates][self._tickers]
        
        #print overlap info
        print "The universe and signal data have "+str(len(tickerOverlap))+" stocks in common, for "+str(len(self.signal))+" rebalancing dates... \n"
                
 


      
    def __makeSelection(self):
        """ Method to set self.selection
        
            Selects investments picking the top/bottom X investments based on the signal.
            If the specified 'rule' parameter is positive --> the top X investments are choosen
            If the specified 'rule' parameter is negative --> the bottom X investments are choosen
            
            Result:
            Sets self.selection as a dataframe of zeros and ones to identify which investments are selected on a given date.
            If there isn't sufficient signal data to make a selection at a particular date, an exception is raised.
        
        """
        
        # Case 1: cutoff rule is positive
        if self._rule > 0:
            mask = self.signal.rank(axis=1)<=(self._rule)*(self.signal.notnull())
        # Case 2: cutoff rule is negative    
        if self._rule < 0:
            mask = (-1*self.signal).rank(axis=1)<=(np.abs(self._rule))*(self.signal.notnull())
        
        # Check to make sure there are enough non-Nan values
        diff = np.abs(self._rule)*mask.shape[0] - mask.sum(axis=1).sum()
        if diff > 0:
            raise customExceptions.notEnoughSignals(diff)
            
        self.selection = 1*mask
        
        # print selection confirmation
        print str(self._rule)+" stocks have been selected for each of the "+str(self.selection.shape[0])+" rebalancing dates... \n"
            
         
         
         
            
    def __setWeights(self):
        """ Method to set self.weights
            
            Calculates equal weighting across the selected investments.
            
            Result:
            Sets self.weights as a dataframe with the weights placed across investments (for each rebalancing date)
        
        """
        
        rawWeights = pd.DataFrame(1,index=self._rebalanceDates,columns=self._tickers)*self.selection
        sumWeights = rawWeights.sum(axis=1).replace(0,1)
        normWeights = rawWeights.div(sumWeights,axis=0)
        self.weights = normWeights
        
        
        
        
    def __calcRebalance(self):
        """ Method to set self.strategy
        
            Calculates the returns of the strategy.
            
            Since investment selections are calculated every 'rebalanceWindow' periods, the amount invested in
            each security must be rebalanced every 'rebalanceWindow' periods.
            
            Result:
            Sets self.values with the value of each investment and the overall value of the strategy
            Sets self.strategyReturns as a series with the returns generated by the strategy
        """
        
        #print message that rebalacing is taking place
        print "Now going through rebalancing calculation... \n"
        
        # set parameters and lists to prepare for merge        
        weights = self.weights.copy()
        weightTickers = [str(x)+'_w' for x in weights.columns]
        weights['rebalance'] = 1
         
        # merge the returns dataframe with the weights dataframe and forward fill weight data
        merged = pd.merge(self._returns,weights,how='left',left_index=True,right_index=True,suffixes=['_r','_w'])
        merged['block'] = None
        merged.loc[merged.rebalance==1,['block']] = np.arange((merged.rebalance==1).sum())
        merged['block'] = merged['block'].fillna(method='ffill')
        merged = merged.drop('rebalance',axis=1)
        merged[weightTickers] = merged[weightTickers].fillna(method='ffill')
         
        # before grouping by block (time span between rebalancing), set a global to 0.
        # this global is used to carry infomation (value on previous day) across the groups/blocks.
        global portValueGlobal
        portValueGlobal=0
        rebalanced = merged.groupby('block').apply(strategy.rebalancingProcedure,tickers=self._tickers)
         
        # keep the values of interest and calculate returns
        columnsToKeep = self._tickers[:]
        columnsToKeep.extend(['block','value'])
        self.values = rebalanced[columnsToKeep]
        strategyReturns = (self.values).pct_change()['value']
        strategyReturns.iloc[0]= (self.values.value[0])-1
        self.strategyReturns = strategyReturns




    @ staticmethod
    def rebalancingProcedure(block,tickers):
        """ Method to perform the rebalancing procedure
            To be passed to an apply method on a grouped dataframe of returns and weights.
            Each group should represent one rebalancing window
            
            Args:
            - block (df) : A dataframe which is one piece of a grouped dataframe 
            - ticker (list) : a list of the tickers (column names) for all the possible investments
            
            Returns:
            - block (df): The original df with the value of each investment and the overall value of the strategy appended
        """
        
        global portValueGlobal
        
        for t in tickers: 
            block[t] = ((1+block[t+'_r']).cumprod())*(block[t+'_w'])*portValueGlobal
        block['value'] = block[tickers].sum(axis=1)
        
        # chunk of code below where the global tracking is if/elsed is
        # due to a bug in pandas groupby. See warning at url below.
        # http://pandas.pydata.org/pandas-docs/dev/groupby.html
        
        if portValueGlobal==0:
            portValueGlobal=1
        else:
            portValueGlobal = block['value'].iloc[-1]
            
        return block



        