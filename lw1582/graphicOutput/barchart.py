
'''
Created by Lucy Wang
'''


import matplotlib.pyplot as plt
import numpy as np
from Classes.location_class import *
from userInterface.userInput import get_manual_input, convert_address

def plot_barchart(DF):
  '''
  This function plots the number of free wifi spots in the five boroughs as a bar chart.

   Args:
    a pandas DataFrame of the cleaned dataset. available in the class NearestWifi.

    Returns:
      None. Saves the bar chart as a png in the main project folder.
  '''

  fig = plt.figure()
  ax = fig.add_subplot(111)

  plot_data = DF['Borough'].value_counts() 
  row_labels = list(plot_data.index)

  plot_data.plot(plot_data,kind='bar',figsize = (10,10), alpha = 0.5)

  ax.set_ylabel('Count of Wifi Spots')
  xtickNames = ax.set_xticklabels(row_labels)
  plt.setp(xtickNames, rotation=45, fontsize=12)
  ax.grid(False)
  ax.set_title('Count of Free WiFi Spots by Borough', fontsize = 14)
  
  fig.savefig('Free Wifi by Borough.png')
  plt.close()
