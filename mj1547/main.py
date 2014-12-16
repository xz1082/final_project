'''
Created on Dec 2, 2014

@author: Lei Lu
'''
from ioprocess import *
from dtclean import *
from collisionvis import *
from userinterface.ui_unix import UnixInterface
from dtclean.cleancollisiondata import cleanCollisionData
from utilities import *
from unixvis import UnixVisualizer


def main():
    '''
    entrance to all the functionalities provided with terminal command 
    In main program following actions are to be executed:
        1: print a welcome windows and options instruction to guide users select different kind of analysis
        2: run analysis
        3: ask user to exit the program or to go back to the welcome page
    '''
    #unix command line 
    terminal_ui = UnixInterface()
    terminal_ui.loading()
    #read and clean data
    dataframe_reader = DataReader()
    raw_data=dataframe_reader.safeReadCsvLocal('./data/NYPD_Motor_Vehicle_Collisions.csv')
    cleaner = DataCleaner(cleanCollisionData)
    cleaner.clean(raw_data)
    collision_vis_unix = UnixVisualizer(raw_data)
    executeAnalysis(collision_vis_unix,terminal_ui)
    
if __name__ == '__main__':
    main()