#Author: Po-Chih Lin

import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from exception import *

"""
Train the Stochastic Gradient Descent Regressor
Input: feature vectors and labels
Return: the SGD regression model
"""
def SGD_train(X_train, Y_train):

	#Initialize the SGD model
	clf = linear_model.SGDRegressor()
	#Train
	clf.fit(X_train, Y_train)
	#Return the model
	return clf


"""
Test the model performance (used only when developing)
Input: model, feature vectors in testing set, and their ground truth
Return: the square root of the Mean Squared Error
"""
def validation(model, X_test, Y_test):
	#Prediction
	pred = model.predict(X_test)
	#Square root of MSE
	return np.sqrt(mean_squared_error(list(Y_test), list(pred)))


"""
Compute the Cos Similarity of vector a and vector b
Input: vector a and b
Return: cos theta of a and b
"""
def cosSimilarity(a, b):
	#cos theta = a dot b / ( |a| * |b| )
	return np.sum(a * b)/np.sqrt(np.sum(a*a)*np.sum(b*b))


"""
Retrive the mostly shared skills by the given jobs
Input: the column of all titles of jobs, and feature vecotrs of jobs,
       the list of retrieved jobs, and the lexicon
Return: the list of the top k shared skills
"""
def retrieveSkills(job_title, job_features, selected_jobs, lex):

	#Merge two dataframes of job_title and job_features and drop duplicated rows
	job_merged = job_features.copy()
	job_merged[job_title.name] = job_title
	job_merged.drop_duplicates(inplace=True)

	#Select only the rows with job title is in the selected_jobs
	selected_jobs_with_features = job_merged.select(lambda x : job_merged.loc[x][job_title.name] \
		in selected_jobs, axis = 0)

	#Retrieve all the keyterms (skills) that mostly appear among the selected jobs
	#and generate the pairs of each retrieved skills => (skill, word_counts)
	skills = {}
	for idx in selected_jobs_with_features.index:
		#Use i as an integer indicator
		i = 0
		for col in job_features.columns:
			#For each job, get the keyterm (skill) counts in the job description
			count = selected_jobs_with_features.loc[idx][col]

			#Pick only the skills appearing at least once
			if count > 0: 
				#If the skill is retrived the first time, set it as the initial value
				if lex.invMapping[i] not in skills:
					skills[lex.invMapping[i]] = count

				#If the skill has been retrieved, add the count
				else:
					skills[lex.invMapping[i]] = skills[lex.invMapping[i]] + count
			i = i + 1

	#Sort the skills by those counts 
	skills = sorted(skills.items(), key=lambda x: x[1], reverse=True)

	skills_top_k = [[], []]

	#Set the default number of skills to be presented as 10
	num_skills = 10
	#If the total number of skills is less than 10, present as much as it can
	if len(skills) < num_skills:
		num_skills = len(skills)

	#Structure the results
	for i in range(num_skills):
		skills_top_k[0].append(skills[i][0])
		skills_top_k[1].append(skills[i][1])

	#Return the results
	return skills_top_k


"""
Retrieve the matched jobs given user's resume feature vector
Input: the titles of jobs, the feature vectors of jobs, the feature vectors of user's resume
Return: the list of top k matched jobs
"""	
def retrieveJobs(job_title, job_features, resume_feature_vector):

	#If there is no keyterm in the resume, no job will be matched
	if np.sum(resume_feature_vector) == 0:
		raise NoJobMatchedErr("No skill keyterm is included\nPlease be more specific on your resume")

	#Get the names of each dimension of feature vectors
	feature_names =  job_features.columns

	#Convert the job title to lower case
	for idx in job_title.index:
		job_title.loc[idx] = job_title.loc[idx].lower()

	
	#Merge two dataframes of job_title and job_features and drop duplicated rows
	job_merged = job_features.copy()
	job_merged[job_title.name] = job_title
	job_merged.drop_duplicates(inplace=True)


	job_matching_score = []	
	score_sum = 0
	#For each jobs in the job pool
	for idx in job_merged.index:
		#Compute the similarity of each job and user's resume
		score = cosSimilarity(job_merged[feature_names].loc[idx], \
			np.array(resume_feature_vector))

		#Culmulate the scores
		score_sum =  score_sum + score

		#Generate the pair (job, score)
		job_matching_score.append( (job_merged.loc[idx][job_title.name], score) )

	#Sort the jobs by their scores
	job_matching_score = sorted(job_matching_score, key=lambda x: x[1], reverse=True)
	
	job_top_k = [[], []]

	#Set the default number of jobs to be presented as 10
	num_jobs = 10
	#If the total number of jobs is less than 10, present as much as it can
	if len(job_matching_score) < num_jobs:
		num_jobs = len(job_matching_score)

	#If the culumlative score is greater than zero, some jobs have been retrived
	if score_sum != 0:
		for i in range(num_jobs):
			#Structure the results and do normalization
			job_top_k[0].append(job_matching_score[i][0])
			job_top_k[1].append(float(job_matching_score[i][1]) / float(score_sum))
	#No job is matched
	else:
		raise NoJobMatchedErr("No job is matched")
		
	#Return the results
	return job_top_k



"""
Do the Pseudo Relevance Feedback on the feature vector of resume
Input: the feature vector of resume, the retrieved skills with scores, and the lexicon
Return: the corrected feature vector of resume after PRF
"""
def resumePRF(resume_feature_vector, skills_and_scores, lex):

	#Pick the max score as the normalizing denominator
	normalization_coef = float(np.max(skills_and_scores[1]))

	#Copy the feature vector of resume
	resume_PRF = list(resume_feature_vector)

	#Extract the skills and scores
	skills = skills_and_scores[0]
	scores = skills_and_scores[1]

	for i in range(len(skills)):
		#For each skill in the skill pool, add the feedback count in the resume feature vector
		resume_PRF[lex.mapping[skills[i]]] =\
			resume_PRF[lex.mapping[skills[i]]] + scores[i]/normalization_coef
	#Return the result
	return resume_PRF


