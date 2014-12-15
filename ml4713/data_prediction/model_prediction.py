'''
Author: Chris Zhou, Contributor: Mengfei Li
This module builds a random forest model based on cleaned dataframe from data_clean_prediction.py; the model's target variable is y (income), and a few variables are dropped because they do not have significant feature importance when feature importances from the model is sorted. The module then applies the random forest model to predict income for new data. The module also includes readFile function to ensure the program clean the correct dataset. 
'''

from data_clean_prediction import *
from sklearn.ensemble import RandomForestClassifier
import sys

def randomForest(pred_data, model_data):
    '''
    this function takes a panda serie of input data, builds a Random Forest model on our census data, and outputs the target value calculated via the Random Forest model
    the Random Forest model excludes native-country, sex, race, workclass, capital-loss, and relationship because they do not have significant feature importance    
    '''
    data = model_data
    rf = RandomForestClassifier(n_estimators=150, min_samples_split=1)
    rf.fit(data.drop(['y', 'native-country', 'sex', 'race', 'workclass', 'capital-loss', 'relationship'], axis =1), model_data['y']) 
    income = rf.predict(pred_data)
    return income


def readFile():
    '''
    this function asks for user input, determines which file to apply clean_data_for_prediction, cleans the dataset, and returns the cleaned dataset.
    '''
    try:   #take user input file path to clean data
        file_path = raw_input('Please enter your file path: ')
        file_path = "".join(file_path.split())
    except KeyboardInterrupt:
        print '----------Keyboard Interrupt. Ending---------------'
        sys.exit()
    if file_path in ['Exit', 'End', 'Quit', 'exit', 'end', 'quit','EXIT','END','QUIT']:
        print '----------Exiting---------------'            
        sys.exit()
    else:
        cleaned_data = clean_data_for_prediction(file_path)
    
    return cleaned_data