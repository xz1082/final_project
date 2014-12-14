#Author: Meihao Chen

import pandas as pd
import numpy as np

"""
Summarize no. of positions by feature, return the feature name and series
Input: dataframe and the feature to be analyzed
Return: the retrived series
"""
def numberOfPositions(data_frame, input_string):
    
	feature = input_string
	#Select the data corresponding to the feature
	feature_df = data_frame[[feature, '# Of Positions']]
	#Get the unique items in the feature column
	keys = feature_df[feature].value_counts().keys()
	feature_counts = []
	#Generate the series
	for key in keys:
		feature_counts.append(np.sum(feature_df[feature_df[feature] == key]['# Of Positions']))

	s = pd.Series(feature_counts, index = list(keys))    
	s.sort(ascending = False)
	return s

"""
Summarize the salary medium by feature, return feature name and series
Input: dataframe and the feature to be analyzed
Return: the retrived series
"""
def salaryMedium(data_frame, input_string):

	feature = input_string
	feature_df = data_frame[[feature, 'Salary Range From', 'Salary Range To']]
	keys = feature_df[feature].value_counts().keys()

	salary_min = []
	salary_max = []
	for key in keys:
		#Get the minimum value and maximum value of salary of different items in a feature
		salary_min.append(feature_df[feature_df[feature] == key]['Salary Range From'].min())
		salary_max.append(feature_df[feature_df[feature] == key]['Salary Range To'].max())
	min_ = pd.Series(salary_min, index = keys)
	max_ = pd.Series(salary_max, index = keys)
    
	#Compute the medium value of salary as average of max  and min
	salary_medium = (max_+min_)*0.5
	salary_medium.sort(ascending = False)
    
	return salary_medium

