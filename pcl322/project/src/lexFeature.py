#Author: Po-Chih Lin

import sys
import os 
import pandas as pd
import numpy as np


"""
Tokenize the given document
Input: document (a long string)
Return: documents without symbols and in lower case
"""
def tokenize(doc):
	#Format the doc
	tokenized_doc = doc.decode("utf8").lower()
	#The set of symbols to be removed
	symbols = ["\\\n", "\\n", "\\r", "<p>", "</p>","<u>", "</u>", \
		"\t", "\n", "\r", ".", ";", ",", "(", ")", "[", "]",\
		 "\"", "\'", "-", "_", "=", "\\", "/"]
	#Removal
	for s in symbols:
		tokenized_doc = tokenized_doc.replace(s, " ")

	return tokenized_doc.split(" ")


"""
Generate the lexicographic feature of the given document
Input: document (a long string) and the lexicon object
Return: the lex feature vector (in a list)
"""
def genLexFeature(doc, lex):
	#Initialize the feature vector
	feature = [0 for i in range(lex.size)]
	#Remove useless symbols and format the string
	toks = tokenize(doc)


	for t in toks:
		#If the word is a keyterm
		if t in lex.mapping:
			#Count one in that keyterm feature dimension
			feature[lex.mapping[t]] =  feature[lex.mapping[t]] + 1
	return feature


"""
Read the lexicon file
Input: lexicon file path
Return: the lexicon with each id mapping
"""
def readLex(filename):
	fp = open(filename, "r")

	i = 0
	keytermLex = {}
	while True:
		line = fp.readline().rstrip("\n")
		if not line:
			break
		#If the keyterm has not been read, add it in the lexicon
		if line not in keytermLex:
			keytermLex[line] = i
			i = i + 1
	fp.close()

	return keytermLex


"""
Transform the documents (in a dataframe) into lexicographic feature vectors
Input: dataframe with documents and lexicon object
Return: the dataframe with lex feature vectors
"""
def transformDocsToFeatures(df, lex):
	#Initialize the lexicon feature dataframe
	lexFeatureDF = pd.DataFrame(index=df.index, columns=[ "keyterm_%d"%(i) for i in range(lex.size)])


	for idx in df.index.values:
		#Prevent NaN 
		df.loc[idx].replace(np.nan, ".", inplace=True)
		#Initialize the feature vecotr
		features = [0 for i in range(lex.size)]

		for col in df.columns.values:
			#For each document in each column adn each index in df
			#generate the lex feature vector and sum up all vectors
			#across columns within the same idx
			#E.g., feature[5] = genLeXFeat(df[5]["A"])+genLeXFeat(df[5]["B"])
			features = [sum(x) for x in zip(features, \
				genLexFeature(df.loc[idx][col], lex))]
		#Assign the computed vector to the result dataframe
		lexFeatureDF.loc[idx] = features

	return lexFeatureDF



