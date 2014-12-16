'''
Created on Dec 2, 2014

@author: Jiayi Lu, Minzi Ji, Lei Lu
'''
from dtclean import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from excpshandle import *
from dtclean.dropmissinglocations import dropMissingLocations
import sys
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import statsmodels.api as sm

class CollisionVisualizer():
    '''
    class definitions for basic operations on NYPD motor vehicle collisions dataset
    >>>>
    In class CollisionVisualizer
    Internal Attributes:
        1. _data : a pandas dataframe to load the 'NYPD_Motor_Vehivle_Collisions.csv' file

    Internal Methods:
        1. __getData    : get self._data
        2. _isValidDateRange : check if the date range is valid, that is 2012-07-01 < start_date < end_date < 2014-11-29
        3. _getVehicleTypes : returns the list for all vehicle type names that has been recorded in case needed, might be deleted in the next version
        4. _selectByDateRange : returns a dataframe containing entries from start_date to end_date
        5. _safeSelectByDateRange : try select date by range, includes exception handling
        6. _movingAverage : compute an n period moving average, average_type has option 'linear' and 'exponential
        7. _adaptiveAverageLength : returns a length to calculate moving average based on the length of the period, returns 7,14 or 28
        8. _selectByTypeclass : select dataframe by total, injured or deaths
        9. _safeSelectByTypeclass : select dataframe by total, injured or dead with exception handling
        10. _regression : generate a summary table about the parameters from the regression analysis
        
    Public Methods:
        1. Vehicle Types : returns a dataframe for all recorded vehicle types, counts and percentages within date range (start,end)
        2. regressionVehicleXFatalities : generates a scatter plot of normalized raw data with a fitted regression line
        3. collisionsByDateRange : return a Dataframe with the Date and how many collosions happend that day, columns [DATE, HAS collisions happen]
        then use numpy np.mean to find the mean value of has collisions happen as well as provide a weekly moving average reference line
        4. boroughFatalities : return a table with borough and number of kill and injured, columns=['BOROUGH','HAS KILLED','HAS INJURED'] 
        5. fatalitiesByTime : return a table with TIME and number of kill and injured, columns=['TIME','HAS INJURED OR KILLED'] 
        6. fatalitiesByDateRange : return a table with TIME and number of kill and injured, columns=['DATE','HAS INJURED OR KILLED'] 
        7. getMaxFatalities : generate a data frame that reports the maximum number of fatalities during a time frame given as parameters
        8. top5Factors : returns the top 5 contributing factor for accidents in the given date range and plot a pie Chart
    '''

    '''
    Internal Methods
    '''
    def __init__(self, init_dataframe):
        '''
        Constructor
        '''
        self._data = init_dataframe
        
    def __getData(self):
        '''
        returns self._data, for test purposes only!
        '''
        return self._data
    
    def _isValidDateRange(self,start_date,end_date):
        '''check if the date range is valid, that is
            2012-07-01 < start_date < end_date < 2014-11-29
        '''
        start_date_timestamp = pd.to_datetime(start_date)
        end_date_timestamp = pd.to_datetime(end_date)
        return (start_date_timestamp >= self._data.index[0]) & (end_date_timestamp <= self._data.index[-1]) & (start_date_timestamp < end_date_timestamp)
         
    def _getVehicleTypes(self):
        '''
        returns the list for all vehicle type names that has been recorded in case needed, might be deleted in the next version
        ''' 
        columns_list = ['VEHICLE TYPE CODE {}'.format(x) for x in range(1,6)]
        vehicle_type_set = set()
        for type_code in columns_list:
            vehicle_type_set.update(list(self._data[type_code].dropna().unique()))
        return list(vehicle_type_set)
    
    def _selectByDateRange(self,start_date=None,end_date=None):
        '''
        returns a dataframe containing entries from start_date to end_date
        '''
        if self._isValidDateRange(start_date,end_date):
            return self._data[start_date:end_date]
        else:
            raise DateRangeError()
        
    def _safeSelectByDateRange(self,start_date=None,end_date=None):
        '''
        try select date by range, includes exception handling
        '''
        try:
            date_ranged_data = self._selectByDateRange(start_date, end_date)
            return date_ranged_data
        except (DateRangeError):
            print >> sys.stderr, 'Invalid Date Range!\n'
            return None
        
    def _movingAverage(self,input_data,n,average_type='linear'):
        '''
        compute an n period moving average, average_type has option 'linear' and 'exponential
        '''
        x = np.asarray(input_data)  #convert input series or dataframe to nparray
        if type == 'linear':
            weights = np.ones()
        else:
            weights = np.exp(np.linspace(-1.,0.,n))
        weights /= weights.sum()
        moving_average = np.convolve(x,weights,mode='full')[:len(x)] #returns the convolution of weight array and input data
        moving_average[:n] = moving_average[n]
        return moving_average
    
    def _adaptiveAverageLength(self,start_date,end_date):
        '''
        returns a length to calculate moving average based on the length of the period, returns 7,14 or 28
        '''
        days_difference = (pd.to_datetime(end_date)-pd.to_datetime(start_date)).days
        return max(int(days_difference/70)*7,1)
    
    def _selectByTypeclass(self,input_dataframe,typeclass='total'):
        '''
        select dataframe by total, injured or deaths
        '''
        if typeclass == 'total':
            output = input_dataframe
        elif typeclass == 'deaths':
            output = input_dataframe[input_dataframe['TOTAL DEATHS']>0]
        elif typeclass == 'injuries':
            output =  input_dataframe[input_dataframe['TOTAL INJURIES']>0]
        else:
            raise TypeClassError()
            return None
        if output.empty:    #in case if there are no qualified items in the dataframe
            raise EmptyDataframeError()
            return None
        else:
            return output
        
    def _safeSelectByTypeclass(self,input_dataframe,typeclass='total'):
        '''
        select dataframe by total, injured or dead with exception handling
        '''
        try:
            output = self._selectByTypeclass(input_dataframe, typeclass)
        except (TypeClassError,EmptyDataframeError):
            print >> sys.stderr, 'No Data Is Available by class {}\n'.format(typeclass)
            return pd.DataFrame()
        return output         
                
    '''
    Public Methods
    '''
    def VehicleTypes(self,start_date=None,end_date=None):
        '''
        returns a dataframe for all recorded vehicle types, counts and percentages within date range (start,end)
        '''
        date_ranged_data = self._safeSelectByDateRange(start_date,end_date)
        record_vehicle_types = pd.Series(date_ranged_data[['VEHICLE TYPE CODE {}'.format(x) for x in range(1,6)]].values.ravel()).dropna()
        collisions_count_by_type = record_vehicle_types.value_counts()
        others_count = collisions_count_by_type.sum()-collisions_count_by_type.head().sum()
        collisions_count_by_type = collisions_count_by_type.head(5)
        collisions_count_by_type['OTHERS'] = others_count 
        collisions_count_by_type = pd.DataFrame(collisions_count_by_type,columns=['COUNTS'])
        collisions_count_by_type['%'] = collisions_count_by_type['COUNTS']/collisions_count_by_type['COUNTS'].sum() #calculate percentage
        return collisions_count_by_type
#     
#     def listNearbyCollisions(self,start_date=None, end_date=None, longitude = None, latitude = None, proximity_range = None):
#         '''
#         returns a table listing all the collisions in the nearby area of (longitude, latitude) from start_date to end_date, the table has
#         columns [DATE, TIME, DISTANCE FROM, NUMBER OF INJURIES AND DEATHS]
#         '''
#         #delete all entries without geographical information
#         geographical_cleaner = DataCleaner(dropMissingLocations)
#         data_with_location = geographical_cleaner.clean(self._safeSelectByDateRange(start_date, end_date))
#         data_with_location.apply()

    def regressionVehicleXFatalities(self):
        '''
        generates a scatter plot of normalized raw data with a fitted regression line
        '''
        df = self._data
        Y = self._data['TOTAL FATALITIES']  # response
        X = self._data['VEHICLES INVOLVED']  # predictor
        X = sm.add_constant(X)  # Adds a constant term to the predictor
        est = sm.OLS(Y, X)
        est = est.fit()
 
        X_prime = np.linspace(X['VEHICLES INVOLVED'].min(), X['VEHICLES INVOLVED'].max(), 5)[:, np.newaxis]
        X_prime = sm.add_constant(X_prime)  # add constant as we did before
        
        plt.ylim([0,35])
        y_hat = est.predict(X_prime)
        return X['VEHICLES INVOLVED'], Y, X_prime[:,1], y_hat

    def collisionsByDateRange(self,start_date=True,end_date=True):
        '''
        return a Dataframe with the Date and how many collosions happend that day
        columns [DATE, HAS collisions happen]
        then use numpy np.mean to find the mean value of has collisions happen as well as provide a weekly moving average reference line
        '''
        
        date_range_data=self._safeSelectByDateRange(start_date, end_date)
        date_happen=date_range_data.groupby(date_range_data.index)
        date_happened={'date':[],'happen':[]}
        for date, group in date_happen:
            happen=len(group)
            date_happened['date'].append(date)
            date_happened['happen'].append(happen)
        df_happen=pd.DataFrame.from_dict(date_happened['happen'])
        df_date=pd.DataFrame.from_dict(date_happened['date'])    
        df_date.columns=['date']
        df_happen.columns=['NUMBER OF COLLISIONS']   
        df_date_happen=df_date.join(df_happen)  
        df_date_happen=df_date_happen.set_index('date')
        mean_collision=np.mean(df_date_happen['NUMBER OF COLLISIONS'])  
        df_date_happen.index.name=None
#         ndays = self._adaptiveAverageLength(start_date, end_date) #calculate an adaptive average timespan
#         moving_average = self._movingAverage(df_date_happen['NUMBER OF COLLISIONS'], ndays, 'linear')
#         df_date_happen['WEEKLY AVERAGE'] = pd.Series(moving_average,index=df_date_happen.index)
        return df_date_happen,mean_collision
    
    def boroughFatalities(self,start_date=True,end_date=True):  #convert to big-small pie
        '''
        return a table with borough and number of kill and injured
        columns=['BOROUGH','HAS KILLED','HAS INJURED'] 
        '''
        new_data=self._safeSelectByDateRange(start_date, end_date)
        boro=new_data.groupby('BOROUGH')
    
        injured_killed={'borough':[],'injured_killed':[]}
        for borough,group in boro:
            group=group[['TOTAL DEATHS','TOTAL INJURIES']]
            #b_group=group.set_index('Date')
            x_sum=group.sum(axis=0)
            #print borough
            #print x_sum
            injured_killed['borough'].append(borough)
            injured_killed['injured_killed'].append(x_sum)
     

        df_boro=pd.DataFrame.from_dict(injured_killed['borough'])#, orient='columns', dtype=None)
        df_kill=pd.DataFrame.from_dict(injured_killed['injured_killed'])
        df_boro_kill=df_boro.join(df_kill)
        df_boro_kill.columns=['BOROUGH','HAS KILLED','HAS INJURED']
        df_boro_kill=df_boro_kill.set_index('BOROUGH')
        return df_boro_kill
     
    def fatalitiesByTime(self,start_date=True,end_date=True):
        '''
         return a table with TIME and number of kill and injured
        columns=['TIME','HAS INJURED OR KILLED'] 
        '''
        new_data=self._safeSelectByDateRange(start_date, end_date)
        
        new_data['TIME'] = pd.to_datetime(new_data['TIME'],format='%H:%M')
        dd=new_data.sort('TIME',ascending=1)
        time_group=dd.groupby('TIME')
        time_injured_killed={'time':[],'injured_killed':[]}
        for time,t_group in time_group:
            t_group=t_group[['TIME','TOTAL FATALITIES']]
            time_sum=t_group['TOTAL FATALITIES'].sum(axis=0)
            time_injured_killed['time'].append(time)
            time_injured_killed['injured_killed'].append(time_sum)
        df_time=pd.DataFrame.from_dict(time_injured_killed['time'])#, orient='columns', dtype=None)
        df_kill_t=pd.DataFrame.from_dict(time_injured_killed['injured_killed'])
        df_time.columns=['time']
        df_kill_t.columns=['HAS INJURED OR KILLED']
        #print df_date
        #print df_kill_d
        df_time_kill=df_time.join(df_kill_t)
        #df_date_kill.columns=['Date','HAS INJURED OR KILLED']
        df_time_kill=df_time_kill.set_index('time')
        return df_time_kill

    def fatalitiesByDateRange(self,start_date=None,end_date=None):
        '''
         return a table with TIME and number of kill and injured
        columns=['DATE','HAS INJURED OR KILLED'] 
        '''
        new_data=self._safeSelectByDateRange(start_date, end_date)
        date_g=new_data.groupby(new_data.index)
        date_injured_killed={'Date':[],'injured_killed':[]}
        for date,group in date_g:
            date_sum=group['TOTAL FATALITIES'].sum(axis=0)
            date_injured_killed['Date'].append(date)
            date_injured_killed['injured_killed'].append(date_sum)

        df_date=pd.DataFrame.from_dict(date_injured_killed['Date'])#, orient='columns', dtype=None)
        df_kill_d=pd.DataFrame.from_dict(date_injured_killed['injured_killed'])
        df_date.columns=['Date']
        df_kill_d.columns=['HAS INJURED OR KILLED']
        df_date_kill=df_date.join(df_kill_d)
        df_date_kill=df_date_kill.set_index('Date')
        return df_date_kill

    def _regression(self):
        '''
        generate a summary table about the parameters from the regression analysis
        '''
        mask = np.random.rand(len(self._data)) < 0.75
        train = self._data[mask]
        test = self._data[~mask]
        ols = sm.OLS(train['TOTAL FATALITIES'], train.drop('TOTAL FATALITIES', 1))
        result = ols.fit()
        return result.summary()
            
    def getMaxFatalities(self, start_date, end_date):
        ''' 
        generate a data frame that reports the maximum number of fatalities during a time frame given as parameters
        '''
        date_ranged_data = self._safeSelectByDateRange(start_date,end_date)
        max_fatality_point = date_ranged_data[date_ranged_data['TOTAL FATALITIES']==date_ranged_data['TOTAL FATALITIES'].max()]
        max_fatality_point = max_fatality_point[['TIME','TOTAL FATALITIES','BOROUGH','ZIP CODE','LATITUDE','LONGITUDE']]
        return max_fatality_point

    def top5Factors(self,start_date,end_date,typeclass='total'):
        '''
        returns the top 5 contributing factor for accidents in the given date range and plot a pie Chart
        '''
        date_ranged_data = self._safeSelectByTypeclass(self._safeSelectByDateRange(start_date, end_date), typeclass)
        if not date_ranged_data.empty:
            factors_list = pd.Series(date_ranged_data[['CONTRIBUTING FACTOR VEHICLE {}'.format(x) for x in range(1,6)]].values.ravel()).dropna()
            factor_counts = factors_list.value_counts()
            others_count = factor_counts.sum()-factor_counts.head().sum()
            top5_factors = factors_list.value_counts().head()   #keep only the top 5
            top5_factors['Others/Unspecified']=others_count
            return top5_factors
        else:
            return date_ranged_data #which is a empty dataframe according to exception handling
    
        