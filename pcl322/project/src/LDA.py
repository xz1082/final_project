#Author: Yitong Wang
#Integrator: Po-Chih Lin

import warnings
warnings.simplefilter('ignore')
import re
import pandas as pd
import numpy as np
from gensim import corpora, models, similarities
from operator import itemgetter
import scipy as sp
from lexFeature import *

"""
Check the word is in the correct format
Input: a string
Return: true or false
"""
def is_word(word):
	#Check the format of the word using regular expression
	if re.match(r"^[a-z]+$", word) == None:
		return False
	return True


"""
Extract the words in the dataframe with filtering out symbols and stopwords
Input: the dataframe and the list of stopwords
Return: list of splitted words
"""
def cleanTexts(df, stoplist):
	
	#Use the whole dataframe as documents
	documents = df
	docs = []

	#Concatenate all records into a list of documents
	for i in range(len(documents)):
		sent = ""
		for feature in documents.columns.values:
			#Remove null
			documents[feature].replace(np.nan, ".", inplace = True)
			#Convert to lower case
			sent = (sent + str(documents[feature].values[i])).lower()
			#Remove symbols
			sentence = sent.replace("\\n","").replace("\"","").replace("\r","").replace("\t","")
			sentence = re.sub("<p>|</p>|<u>|</u>|<P>|</P>", "", sentence)
			sentence = re.sub("\W", " ", sentence)
		#Concatenation
		docs.append(sentence)

	#Remove the stopwords and tokenize each document
	texts = [[word for word in tokenize(doc) if word not in stoplist] for doc in docs]

	#Remove the words in wrong format
	texts = [[word for word in text if is_word(word)] for text in texts]

	#Return the cleaned and splitted words
	return texts


"""
Train the LDA model
Input: the list of words, the number of topics, and the output file path
Output: the lexicon of all topic words in LDA (written to the output file)
Return: none
"""
def topicModel(texts, n_topics, output):
	#Build the dictionary given the list of words
	dictionary = corpora.Dictionary(texts)
	
	#Build the coupus given list of words
	corpus = [dictionary.doc2bow(t) for t in texts]

	#Compute the TFIDF
	print "Extracting TFIDF..."
	tfidf = models.TfidfModel(corpus)
	corpus_tfidf = tfidf[corpus]

	#Train LDA model
	print "LDA Training..."
	lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=n_topics)

	#Output the results
	print "Writing the keyterm lexicon..."
	fp = open(output, "w")
	for i in range(0, n_topics):
		temp = lda.show_topic(i, 10)
		for term in temp:
			fp.write(term[1]+"\n")
	fp.close()
	
