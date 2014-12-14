#Author: Meihao Chen
#Integrator: Po-Chih Lin

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

"""
Plot bar chart for a target(salary or number of positions) by feature
Input: the target value, the feature name, the number of top items
Output: the plot (saved to the corresponeding file)
Return: the file name of the plot
"""
def barAndPiePlot(target, feature, series, k):

	#Group the items not in top k and average those values
	series_add_other = plotPreparation(series, k)

	#Plot setting
	fig = plt.figure()
	fig.set_size_inches(30,10)

	ax0 = plt.subplot2grid((4, 10), (0, 0), colspan=5, rowspan=3)
	ax1 = plt.subplot2grid((4, 10), (0, 7), colspan=3, rowspan=4)

	series_integer_idx = np.arange(len(series_add_other))
	labels = [normalize_string(s) for s in  series_add_other.index]

	#Bar chart
	ax0.bar(series_integer_idx,  series_add_other)

	title = "The top "+str(k)+" "+feature+" "+"with highest "+target

	ax0.set_title(title)
	ax0.set_xticks(series_integer_idx)
        ax0.set_xticklabels(labels,  rotation=75)
        ax0.set_xlim([-1, len(series_add_other)+1])
	ax0.set_ylabel(target)

	#Pie chart
	explode = [0] * len(series_add_other)
	explode[0] = 0.1

	colors = np.random.rand(len(series_add_other), 3)

	ax1.pie( series_add_other, labels=labels, explode=explode, \
		colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
	ax1.axis('equal')

	#Output the plots
	output_file = "./plots/plot_"+target.replace(" ", "_")+"_"\
                +feature.replace(" ", "_")+"_top_"+str(k)+".png"

	plt.savefig(output_file)

	plt.close()

	#Return the name of the outputed file
	return output_file

"""
Truncate and formatted the string which is too long
Input: string
Return: the processed string
"""
def normalize_string(s):
	max_len = 25
	#Formatting
	s_modified = s.decode("utf8").upper()
	#If it is too long, truncate it
	if len(s) > max_len:
		#Return the formatted string
		return s_modified[:max_len]+"..."
	return s_modified

"""
Select the top k values in the series, and average the rest then save as others
Input: the series and the number of top items
Return: the modified series 
"""
def plotPreparation(series, k):
	#Pick only the top k
	top_k = series[:k]
	#Average it
	others = np.sum(series[k:])/len(series[k:])
	#Add another column called "OTHERS' AVERAGE"
	top = top_k.append(pd.Series(others, index = ["OTHERS' AVERAGE"]))
	#Formatting
	index = [x.decode('utf8').encode('ascii', 'replace') for x in top.keys()]
	return top


