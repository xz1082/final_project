
'''
Created by : Maya Rotmensch

'''

import matplotlib.pyplot as plt
import numpy as np
from textwrap import *
from Classes.location_class import *
from userInterface.userInput import get_manual_input, convert_address



def heat_map(DF):
    '''
    This function creates a heat map depicting the number of available free Wifi connections in any given Borough for any given Internet provider.
    The figure shows the types of available Internet providers on the y axis, and the different Boroughs on the x axis.
    The strength of the color within box ij reflects the number of Internet connections for provider i in Borough j. The darker the color, the more Wifi connections there are available.
    Some of the ideas the this heat map implementation were taken from http://stackoverflow.com/questions/14391959/heatmap-in-matplotlib-with-pcolor.

    Args:
        a pandas DataFrame of the cleaned dataset. available in the class NearestWifi.

    Returns:
        None. Saves the heatmap figure as a pdf in the main project folder.
    '''
    Provider = DF.Provider
    Borough = DF.Borough

    #convert categorical variables into dummy variables for easier grouping and counting
    new_df = pd.get_dummies(Provider)
    new_df['Borough'] = Borough

    # find out how many wifi connections there are in every borough. 
    map_data = new_df.groupby('Borough').sum()


    map_data_trans = map_data.T

    fig, ax = plt.subplots()
    heatmap = ax.pcolor(map_data_trans, cmap=plt.cm.Blues)

    column_labels = map_data_trans.columns
    row_labels = map_data_trans.index
    row_labels = ['\n'.join(wrap(l.lower(),15)) for l in row_labels]

    # want a more natural, table-like display
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    #put the major ticks at the middle of each cell
    ax.set_xticks(np.arange(map_data_trans.shape[1])+0.5, minor=False)
    ax.set_yticks(np.arange(map_data_trans.shape[0])+0.5, minor=False)

    ax.set_xticklabels(column_labels, minor=False, fontsize  = 7)
    y = ax.set_yticklabels(row_labels, minor=False, fontsize = 7)

    fig.set_size_inches(7,9)

    plt.savefig("Heatmap showing the number of wifi connections in each borough.pdf")


