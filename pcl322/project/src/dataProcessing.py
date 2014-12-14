#Author: Meihao Chen
#Integrator: Po-Chih Lin

import os
import pandas as pd
import numpy as np
from classLexicon import *
from exception import *

"""
Initialize the stopwords list
Input: the stopwords file path
Return: the list of stopwords
"""
def init_stoplist(file_name):

	fp = open(file_name, "r+")
	stoplist = []

	#Read each line in the stopwords file
	while True:
		stop = fp.readline().replace("\n", "")
		if not stop:
			break
		#Append every stopwords into a list
		stoplist.append(stop)

	fp.close()

	return stoplist


"""
Initialize the dataset and the lexicon
Input: datset file path and lexicon file path
Return: the filtered dataframe and lexicon object
"""
def init_dataset(data_file, lex_file):

	#Test the files exist or not
	fp = open(data_file, "r")
	fp.close()
	fp = open(lex_file, "r")
	fp.close()	

	#Read the dataframe
	df = pd.read_csv(data_file)
	#Select only the jobs with annual salary
	df_annual = df[df["Salary Frequency"] == "Annual"].reset_index()

	#Initialize the lexicon
	lex = lexicon(lex_file)

	return df_annual, lex


