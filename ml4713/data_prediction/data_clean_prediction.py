'''
Author: Chris Zhou, Contributor: Meina Zhou
This module cleans census data downloaded from UCI Machine Learning Repository, reads data into pandas dataframe, drops missing values, transforms data into catogorical variable, and return a cleaned dataframe ready to use in building prediction model.
'''

import pandas as pd
import numpy as np
import os.path
from sklearn import preprocessing 
from user_exceptions_prediction import cannot_open_file_exception
        
def clean_data_for_prediction(file_path):
    '''
    this function reads txt data into pandas dataframe, cleans uncessary data, transforms data into categorical variable, and return a cleaned dataframe.
    '''
    if os.path.isfile(file_path):
        #read data into pandas dataframe with column names
        dataframe = pd.read_csv(file_path)
        dataframe.columns = ['age','workclass','fnlwgt','education','education-num','martial-status','ocupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','y']
    
        #drop fnlwgt because we do not need to weight the observations in this project, drop education_num because it's perfectly correlated with education
        dataframe = dataframe.drop(['fnlwgt', 'education-num'], 1)
        dataframe = dataframe[pd.notnull(dataframe['y'])]
        dataframe = dataframe.drop_duplicates()
    
        #convert target variable y to binary variable: 1 for > 50k, 0 for <= 50k
        le_y = preprocessing.LabelEncoder()
        dataframe.y = le_y.fit_transform(dataframe.y)
    
        #drop values '?' in workclass column 
        dataframe['workclass'] = dataframe['workclass'].replace(' ?', np.nan)
        dataframe = dataframe[pd.notnull(dataframe['workclass'])]
        #combine government employed into one group, self-employed into one group, never-worked and without-pay into one group, and convert them to numerical values
        workclass_map = {' Never-worked': 4, ' Without-pay': 4, ' Local-gov': 1, ' State-gov': 1, ' Federal-gov': 1, ' Private': 2, ' Self-emp-not-inc': 3, ' Self-emp-inc': 3}
        dataframe['workclass'] = dataframe.workclass.map(workclass_map)
    
        #combine below college education into one group, associate degress into one group, and convert to numerical values
        education_map = {' Doctorate': 1, ' Masters': 2, ' Bachelors': 3, ' Assoc-acdm': 4, ' Assoc-voc':4, ' Some-college': 4, ' Prof-school': 5, ' 10th': 6, ' 11th': 6, ' 12th': 6, ' 1st-4th': 6, ' 5th-6th': 6, ' 7th-8th': 6, ' 9th': 6, ' Preschool': 6, ' HS-grad': 6}
        dataframe['education'] = dataframe.education.map(education_map)
    
        #combine married into one category, no spouse at the time into one category, and convert to categorical values
        martial_map = {' Married-AF-spouse': 1, ' Married-civ-spouse': 1, ' Married-spouse-absent': 2, ' Separated': 2, ' Divorced': 2, ' Never-married': 3, ' Widowed': 4}
        dataframe['martial-status'] = dataframe['martial-status'].map(martial_map)
    
        #drop missing values in ocupation column
        dataframe['ocupation'] = dataframe['ocupation'].replace(' ?', np.nan)
        dataframe = dataframe[pd.notnull(dataframe['ocupation'])]
        #assign categorical values to each ocupation, each race, and each gender 
        for variable in ['ocupation', 'race', 'sex']:
            new = 'le_' + variable
            new = preprocessing.LabelEncoder()
            dataframe[variable] = new.fit_transform(dataframe[variable])
    
        #combine husband and wife into one category, not in family currently into one category, own child is one category, and convert to category values
        relationship_map = {' Husband': 1, ' Wife': 1, ' Own-child': 2, ' Not-in-family': 3, ' Other-relative': 3, ' Unmarried': 3}
        dataframe['relationship'] = dataframe['relationship'].map(relationship_map)
    
        #drop missing values in native-country column
        dataframe['native-country'] = dataframe['native-country'].replace(' ?', np.nan)
        dataframe = dataframe[pd.notnull(dataframe['native-country'])]
        #group countries by income per capita rank by International Monetary Fund, and convert to categorical values
        country_map = {' United-States': 1, ' Hong': 1, ' Holand-netherlands': 1, ' Ireland': 1, ' Germany': 1, ' Canada': 1, ' Taiwan': 2, ' France': 2, ' Japan': 2, ' England': 2, ' Italy': 2, ' South': 2, ' Portugal': 3, ' Greece': 3, ' Poland': 3, ' Hungary': 3, ' Mexico': 4, ' Iran': 4, ' Thailand': 4, ' Cambodia': 5, ' China': 5, ' Columbia': 5, ' Cuba': 5, ' Dominican-Republic': 5, ' Ecuador': 5, ' El-Salvador': 5, 'Guatemala': 5, ' Haiti': 5, ' Honduras': 5, ' India': 5, ' Jamaica': 5, ' Laos': 5, ' Nicaragua': 5, ' Outlying-US(Guam-USVI-etc)': 5, ' Peru': 5, ' Philippines': 5, ' Puerto-Rico': 5, ' Scotland': 5, ' Trinadad&Tobago': 5, ' Vietnam': 5, ' Yugoslavia': 5}
        dataframe['native-country'] = dataframe['native-country'].map(country_map)
    
        cleaned_data = dataframe.dropna()
        return cleaned_data
        
    else:
        raise cannot_open_file_exception()

