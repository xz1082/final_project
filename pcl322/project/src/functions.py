#Author: Po-Chih Lin

import pandas
from classLexicon import *
from lexFeature import *
from dataProcessing import *
from dataAnalysis import *
from classLexicon import *
from classSalaryPredictor import *
from ui import *
from exception import *
from LDA import *
from featureSummary import *
from plot import *

"""
Graphical analysis on the data interested by user
Show both bar and pie char of the top k (k<=30) retrieved items
Input: the data file and the lexicon file
Output: the plot saved as the file name specified by user
Return: none
"""
def graphicalAnalysis(data_file, lex_file):
	
	while True:

		print "Initializing Data..."
 
		try:
			#Initialze the dataset and the lexicon
			df, lex = init_dataset(data_file, lex_file)

		#Files do not exist
		except FileNotExistedErr as err:
			print err
			terminate()
		#File IO Error
		except IOError as err:
			print err.errno
			print err.strerror
			terminate()

		#Get the information specified by user
		feature, target, items_num = getAnalyTarget()

		print ">> Top %s of %s with highest %s will be shown" %(items_num, feature, target)
		
		#Do either number of positions or salary computation
		if target == "# Of Positions":
			series = numberOfPositions(df, feature)	
		else:
			series = salaryMedium(df, feature)

		#Plot
		try:
			output_file = barAndPiePlot(target, feature, series, items_num)
			print ">> File saved as \"%s\""%(output_file)
		#IO Error during drawing
		except IOError as err:
			print err.errno
			print err.strerror
			terminate()

		#Restart the function or quit
		if not restart():
			break



"""
Generate keyterm lexicon by using LDA model for the salary prediction.
The user will be asked to input the number of topics and the output file
path. The LDA model is an unsupervised training, clustering the words in
the corpus into groups of topics of the given number.

Input: the dataset file path, the stopwords list file path
Output: the keyterm lexicon (written to the user specified file path)
Return: none
"""
def genKeytermLexicon(data_file, stoplist_file):

	while True:
		#Get the number of topics and the ourput file path from user
		n_topic, output_file = getLexiconSetting()

		print "Initialing dataset and stopword list..."

		try:
			#Initilaze the dataset and the stopword list
			df = pd.DataFrame.from_csv(data_file).reset_index()
			stoplist = init_stoplist(stoplist_file)

		#IO Error when reading files
		except IOError as err:
			print err.errno
			print err.strerror
			terminate()

		#The three columns where the documents are retrieved to train the LDA model
		target_docs = ["Job Description","Minimum Qual Requirements","Preferred Skills"]

		print "Cleaning the documents..."
		#Remove unneccessary symbols
		texts = cleanTexts(df[target_docs], stoplist)

		#LDA training
		topicModel(texts, n_topic, output_file)
		print "Successfully done"
		print "Results have been written to \"%s\"" % ( output_file  )
			
		#Read the lexicon just generated
		try:
			new_lex = lexicon(output_file)
                #IO Error when reading files
		except IOError as err:
			print err.errno
			print err.strerror
			terminate()
	
		print "\nThe keyterms within %d topics discovered are " % new_lex.numTopics
		new_lex.show_keyterms()
		
		#Restart the function or quit
		if not restart():
			break


"""
Retrieve the relevant jobs and skills and predict the salary interval given user's resume
The retrieval and prediction are based on the keyterm lexicon given by user

Input: the dataset file path, the default lexicon file
Output: the retrival and prediction results (written to stdout)
Return: none
"""
def salaryPrediction(data_file, lex_file_default):

	#Get the lexicon file from user (return the default one if user skips)
	lex_file = getLexicon(lex_file_default)

	print "Initializing Data..."
 
	try:
		#Initialze the dataset and the lexicon
		df, lex = init_dataset(data_file, lex_file)

	#Files do not exist
	except FileNotExistedErr as err:
		print err
		terminate()
	#File IO Error
	except IOError as err:
		print err.errno
		print err.strerror
		terminate()
	#The columns of dataset where the documents are retrieved to train LDA
	job_description = ["Job Description", "Minimum Qual Requirements", "Preferred Skills"]

	#Transform the job descriptions into feature vectors given the keyterm lexicon
	feature_vectors = transformDocsToFeatures(df[job_description], lex)

	#The ground truth salary lower bound and upper bound for training 
	salary_lower = df["Salary Range From"]
	salary_upper =  df["Salary Range To"]

	print "Training Regression Model..."

	#Generate the SGD regressor to be the salary predictor using the training set and ground truth
	predictor = salaryPredictor(feature_vectors, salary_lower, salary_upper)

	while True:
		#Get user's resume
		resume = getResume()

		#Transform the resume into a feature vector given keyterm lexicon
		resume_feature_vector = genLexFeature(resume, lex)

		try:
			#Retrieve the matched jobs given user's resume
			jobs_and_scores = retrieveJobs(df["Business Title"],\
				feature_vectors, resume_feature_vector)
		#No job is matched
		except NoJobMatchedErr as err:
			print err
			continue

		#Retrive the skills (keyterms) that mostly shared by the given retrieved jobs
		skills_and_scores = retrieveSkills(df["Business Title"], feature_vectors, \
			jobs_and_scores[0], lex)

		#Use the pseudo relevance feedback to add relevent keyterms into the resume
		resume_feature_vector_PRF = resumePRF(resume_feature_vector, skills_and_scores, lex)

		#Predict the salary interval
		salary_interval = predictor.predict(resume_feature_vector_PRF)

		#Show all the prediction results
		showJobMatchingResults(jobs_and_scores[0], skills_and_scores[0], salary_interval)

		#Restart the function or quit
		if not restart():
			break


