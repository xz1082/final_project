'''
Created on Dec 13, 2014

@author: Jiayi Lu, Minzi Ji, Lei Lu
'''
from collisionvis import CollisionVisualizer
import matplotlib.pyplot as plt
import matplotlib.animation as mam
import matplotlib.patches as patches
import pandas as pd
import numpy as np
from userinterface import *
from ioprocess import *
from excpshandle import *

class UnixVisualizer(CollisionVisualizer,UnixInterface):
    '''
    Class definition for plotting data with matplotlib and listing dataframes on the screen, this class is derived from CollisionVisualizer and UnixInterface
    
    In class UnixVisualizer:
    Internal methods:
        1._isStyleAvailable:check if the plotting style setting is avaliable in the current matplotlib release
        2._safeGetDateRange: safely get date range from user input
        3._plotNAN: plot a N sign when data is not applicable
    
    Public methods:
        1.unixvis_vehicleTypes:provide solutions for visualizing top5Factor() data, lists all recorded vehicle types and their counts, plot the top 5
        2.unixvis_regressionVehicleXFatalities:draws the linear regression result for vehicle involved against fatalities
        3.unixvis_collisionAndFatalities:draws number of collisions and fatalities day by day 
        4.unixvis_contributingFactors:plot 3 pie chart indicating the top 5 contributors of all collisions, injuries-involved collisions and deaths-involved collisions
    '''


    def __init__(self,init_dataframe):
        '''
        Constructor
        '''
        CollisionVisualizer.__init__(self, init_dataframe)  #initializing base class
        
    def _isStyleAvailable(self,style):
        '''
        check if plot style is available in current matplotlib version
        '''
        if style in plt.style.available:
            return True
        else:
            return False
        
    def _safeGetDateRange(self):
        '''
        safely get a date range from user input
        '''
        while True:
            start_date,end_date = self.receiveDateRange()
            if self._isValidDateRange(start_date, end_date):
                return start_date,end_date
            else:
                print 'Invalid Date Range, Please Re-enter:\n'
                
    def _plotNAN(self,axes):
        '''
        plot a N sign when data is not applicable
        '''
        image_file = 'dat/GradesN.png'
        try:
            image = plt.imread(image_file)
        except:
            print >> sys.stderr, 'Internal File Import Error!'
            sys.exit()
        im = axes.imshow(image)
        axes.axis('off')
                
        
    def unixvis_vehicleTypes(self,plot_style='ggplot'): #plot2
        '''
        provide solutions for visualizing top5Factor() data, lists all recorded vehicle types and their counts, plot the top 5
        '''
        self._cls()
        start_date, end_date = self._safeGetDateRange()
        self.loading()
        received = self.VehicleTypes(start_date, end_date)
        self.done()
        #displaying dataframe
        print 'The Recorded Vehicle Types and Their Stats Are Shown Below:\n'
        print received
        #plotting and saving
        if self._isStyleAvailable(plot_style):
            plt.style.use(plot_style)
        plt.title('Collisions By Vehicle Types, From {} to {}'.format(start_date,end_date),fontsize=12,color='k')
        received['COUNTS'].plot(kind='pie',legend=False,autopct='%1.1f%%')
        plt.ylabel('')
        plt.tight_layout()
        fig = plt.gcf()
        plt.show()          
        #saving figures
        ifSaveFigure(fig, 'piechart_vehicletypes_{}-{}'.format(start_date,end_date), 'png')
        
    def unixvis_regressionVehicleXFatalities(self,plot_style='ggplot'):
        '''
        draws the linear regression result for vehicle involved against fatalities
        '''
        self.loading()
        X_involved, Y, X_prime1, y_hat = self.regressionVehicleXFatalities()
        self.done()
        if self._isStyleAvailable(plot_style):
            plt.style.use(plot_style)
            
        plt.scatter(X_involved,Y,alpha = 0.3)
        plt.xlabel('Number of Vehicles Involved')
        plt.ylabel('Total Fatalities')
        plt.title('Linear Regression Model of Fatalities vs. Vehicles Involved',fontsize=12,color='k')
        plt.plot(X_prime1,y_hat,'r',alpha=0.9)
        fig = plt.gcf()
        plt.show()
        ifSaveFigure(fig, 'regression', 'png')
        
    def unixvis_collisonsAndFatalities(self,plot_style='ggplot'):
        '''
        draws number of collisions and fatalities day by day 
        '''
        self._cls()
        start_date,end_date = self._safeGetDateRange()
        self.loading()
        collisions_by_date, mean = self.collisionsByDateRange(start_date, end_date)
        fatalities_by_date = self.fatalitiesByDateRange(start_date, end_date)
        fatalities_by_borough = self.boroughFatalities(start_date, end_date)
        self.done()
        #plotting
        if self._isStyleAvailable(plot_style):
            plt.style.use(plot_style)
        fig = plt.figure(figsize=(17.5,10))
        upper_plotting_area = [0.1,0.3,0.5,0.6] #left,bottom,width,height
        lower_plotting_area = [0.1,0.1,0.5,0.15]
        rightdown_plotting_area = [0.7,0.1,0.2,0.35]
        rightup_plotting_area = [0.7,0.55,0.2,0.35]
        fig.suptitle('Collisions And Fatalities From {} to {}'.format(start_date,end_date),fontsize=12)
        ax1 = fig.add_axes(upper_plotting_area)
        ax2 = fig.add_axes(lower_plotting_area)
        ax3 = fig.add_axes(rightup_plotting_area)
        ax4 = fig.add_axes(rightdown_plotting_area)
        
        ax1.set_ylabel('Collisions',fontsize=12)
        ax2.set_ylabel('Fatalities',fontsize=12)
        ax1.set_xlabel('')
        ax2.set_xticklabels('Date')
        ax2.set_ylim(0,750)
        ax2.set_yticks([250,500])
        
        collisions_by_date.plot(ax=ax1,legend=False)
        fatalities_by_date.plot(kind='bar',ax=ax2,legend=False,use_index=False,xticks=[])
        fatalities_by_borough['HAS KILLED'].plot(kind='pie',ax=ax3,legend=False,autopct='%1.1f%%')
        fatalities_by_borough['HAS INJURED'].plot(kind='pie',ax=ax4,legend=False,autopct='%1.1f%%')
        ax3.set_title('Borough Percentage',fontsize=12)
        plt.show()
        ifSaveFigure(fig, 'collision_fatalites_{}-{}'.format(start_date,end_date), 'png')
        
    def unixvis_contributingFactors(self,plot_style='ggplot'):
        '''
        plot 3 pie chart indicating the top 5 contributors of all collisions, injuries-involved collisions and deaths-involved collisions
        '''
        self._cls()
        start_date,end_date = self._safeGetDateRange()
        self.loading()
        total_factors = self.top5Factors(start_date, end_date)
        death_factors = self.top5Factors(start_date, end_date,'deaths')
        injuries_factors = self.top5Factors(start_date, end_date, 'injuries')
        self.done()
        
        if self._isStyleAvailable(plot_style):
            plt.style.use(plot_style)
        fig = plt.figure(figsize=(15,10))
        total_plotting_area = [0.1,0.15,0.46,0.7]
        injuries_plotting_area = [0.7,0.6,0.2,0.3]
        deaths_plotting_area = [0.7,0.1,0.2,0.3]
        fig.suptitle('Top 5 Contributing Factors of Collisions From {} to {}'.format(str(start_date.date()),str(end_date.date())))
        ax_left = fig.add_axes(total_plotting_area)
        ax_rightup = fig.add_axes(injuries_plotting_area)
        ax_rightdown = fig.add_axes(deaths_plotting_area)        
        # if no data in the range plot a N sign
        if  not total_factors.shape[0] < 2:
            total_factors.plot(ax=ax_left,kind='pie',legend=False,title='Total',autopct='%1.1f%%')
        else:
            self._plotNAN(ax_left)
        if not death_factors.shape[0] < 2:
            death_factors.plot(ax=ax_rightup,kind='pie',legend=False,title='Deaths',autopct='%1.1f%%')
        else:
            self._plotNAN(ax_rightup)
        if  not injuries_factors.shape[0] <2:
            injuries_factors.plot(ax=ax_rightdown,kind = 'pie',legend=False,title='Injuries',autopct='%1.1f%%')
        else:
            self._plotNAN(ax_rightdown)
            
        ax_left.set_title('Total',fontsize=12)
        ax_rightdown.set_title('Injuries',fontsize=12)
        ax_rightup.set_title('Deaths',fontsize=12)
        
        plt.show()
        ifSaveFigure(fig, 'top_factors_{}-{}'.format(start_date,end_date), 'png')
        
        

        
        