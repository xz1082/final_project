import sys
import math as mt
import pandas as pd
import numpy as np
import urllib2
import csv
from pygeocoder import Geocoder

import sys

from Math_calculations.distance import *
from geoCoding.geoCoding import *
from customExceptions.customExceptions import *

class NearestWifi:
    """ 
    This class helps locate the nearest free WIFI spot to a given location.
    In class NearestWifi:
    >>>>
        Attributes:
            1) __file_name
            2) __data : a pandas DataFrame containing the raw form of the data from "NYC_Free_Public_Wifi.csv"
            3)clean_data : a pandas DataFrame containing the clean version of __data.
            4) __results_counter: a counter used for displaying final results.

        Methods:
            1) __cleanData
            2) __df_boro
            3) __find_loc
            4) search_results
        
    """  
    def __init__(self):
        """ Initialize the class by loading the WiFi Dataset into a pandas DataFrame. If Dataset is unable to load, an error is raised.
        Args:
            None.
        Returns:
            None.
            Creates the attribute self.__data containing the loaded DataFrame.
        """
        self.__file_name = "data/NYC_Free_Public_Wifi.csv"
        self.__results_counter = 0
        try:
            self.__data = pd.read_csv(self.__file_name)
        except:
            raise UnreadableData("File cannot load. Please make sure file exists")

    def __cleanData(self):
        """ Method cleans up the dataset.
        Args:
            None.
        Returns:
            None.
            Creates the attribute self.clean_data containing the cleaned DataFrame.
        """
        columns = ['Boro','Type','Provider','Name','Location','Lat','Long_','X','Y','Location_T','City','SSID']
        df_cut = self.__data[columns].copy()
        boro = {'BK': 'Brooklyn', 'MN': 'Manhattan', 'SI':'Staten Island', 'QU':'Queens', 'BX':'Bronx'}
        temp = df_cut['Boro'].apply(lambda name: boro[name])
        df_cut['Borough'] = temp
        df_cut2 = df_cut.drop('Boro',1)
        df_dropNaN = df_cut2.dropna(subset = ['Lat','Long_'])
        df_new = df_dropNaN.replace(np.nan,"Unknown")
        self.clean_data = df_new
        return 

    def __df_boro(self, address):
        """ creates a mask that return only the relevant portion of the DataFrame by selecting the relevant borough. 
        Args:
            Address: string. An address formatted by the Geocoder package.
        Returns:
            df_mask: a pandas DF that is t subset of self.clean_data
        """
        self.__cleanData()
        something_unknown = address.sublocality

        df_mask = self.clean_data.loc[(self.clean_data["Borough"] == address.sublocality)]
        return df_mask

    def __find_loc(self, address):
        """ calculates the distance between the address of interest and all the WiFi spots in the same borough.
        Args:
            Address: string. An address formatted by the Geocoder package.
        Returns:
            df_results: a dataframe of Wifi spots in the borough sorted by distance to the addres of interest.
        """
        
        address_info = Geocoder.geocode(address)
        self.lat, self.long_ = address_info.coordinates

        df = self.__df_boro(address_info).copy()

        df["distance"] = df.apply(lambda row: distance(self.lat, self.long_,row['Lat'], row['Long_']), axis=1)
        df_results = df.sort(columns = "distance")
        return df_results

 
    def search_results(self, address, reset = False):
        """ Method that calls the __find_loc() methos and displays the resulting dataframe, 5 results at a time.
        Args:
            Address: string. An address formatted by the Geocoder package.
            reset: Boolean. determined whether or not to reser self.__results_counter
        Returns:
            results_subset: 5 lines from the ordered results dataframe.
        """

        results = self.__find_loc(address)
        end_of_data = len(results.index)

        if reset!= False:
            self.results_counter = 0

        if self.__results_counter != (self.__results_counter)%end_of_data:
            print "There are no more WiFi locations to display."
            sys.exit()
        else:
            print "Closest WIFI locations (results %d to %d )" %(self.__results_counter, self.__results_counter+5)
            results_subset =  results.iloc[self.__results_counter:self.__results_counter+5]
            self.__results_counter +=5

        return results_subset







