#Author: Po-Chih Lin

import pandas as pd
import numpy as np
from dataAnalysis import *
from lexFeature import *
from sklearn.cross_validation import train_test_split

"""
The class of predictor for salary
self.model_lower: the Stochastic Gradient Descent Regressor of salary's lower bound
self.model_upper: the Stochastic Gradient Descent Regressor of salary's upper bound
"""
class salaryPredictor:
	"""
	Initialize the SGD models for lower and upper bounds with the given data
	Input: the lexicon feature vector of the resume, the ground truth salary lower and upper bounds
	"""
	def __init__(self, feature_vectors, salary_lower, salary_upper):

		#Split the data into training set and testing set for two models
		features_train, features_test, salary_lower_train, salary_lower_test, \
			salary_upper_train, salary_upper_test = \
			train_test_split(feature_vectors.values, salary_lower, salary_upper, \
			test_size=0.1, random_state=42)

		#Train the models
		self.model_lower = SGD_train(features_train, salary_lower_train)
		self.model_upper = SGD_train(features_train, salary_upper_train)

	"""
	Compute the prediction of the given feature vector of resume
	Input: the lexicon feature vector of the resume
	Return: the predicted salary interval
	"""
	def predict(self, resume_feature_vector):
		#Predict the salary interval with the pre-trained models
		return list(self.model_lower.predict(resume_feature_vector))+\
			list(self.model_upper.predict(resume_feature_vector))

