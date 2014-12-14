#####################################################
#
#PROJECT NYC JOBS ANALYSIS
#Date: Dec 2014
#Author: Meihao Chen, Po-Chih Lin, Yitong Wang
#Email: mc5283@nyu.edu, pcl322@nyu.edu, yw652@nyu.edu
#
#####################################################
from src.functions import *

"""
This project utilizes the NYC Jobs dataset from NYC Open Data to
gain the deep insight of the posted jobs at NYC during 2012 to 2014.
Several interactions between the program and the user are provided,
including user's salary prediction, retrieval of keyterms in job
description, and the plot drawing for graphical analysis with
controllable options. 
"""
def main():

	data_file = "./data/NYC_Jobs.csv" 
	lex_file_default = "./data/NYC_Jobs.lex"
	stoplist_file = "./data/stopwords/english"


	welcome()

	while True:
		flag = choosingFunctions()

		if flag == "1":
			print "\n>> SALARY PREDICTION"
			salaryPrediction(data_file, lex_file_default)

		elif flag == "2":
			print "\n>> KEYTERM LEXICON GENERATION"
			genKeytermLexicon(data_file, stoplist_file)

		elif flag == "3":
			print "\n>>  GRAPHICAL ANALYSIS"
			graphicalAnalysis(data_file, lex_file_default)
		else:
			break

	goodbye()


if __name__ == "__main__":
	main()
