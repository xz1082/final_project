
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
  fig.set_size_inches(10,8)
  ax = fig.add_subplot(111)

  plot_data = DF['Borough'].value_counts() 
  row_labels = list(plot_data.index)
  row = np.arange(len(row_labels))

  ax.bar(row,plot_data, width = 0.8,alpha = 0.5)

  ax.set_ylabel('Count of Wifi Spots')
  pos = row + 0.4
  ax.set_xticks(pos)
  ax.set_xticklabels(row_labels)

  ax.grid(False)
  ax.set_title('Count of Free WiFi Spots by Borough', fontsize = 14)
  
  fig.savefig('Free Wifi by Borough.png')
  plt.close()
