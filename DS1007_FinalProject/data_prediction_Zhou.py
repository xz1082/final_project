'''
Author: Meina Zhou, contributor: Chris Zhou, Mengfei Li
This module is the main function, which uses all other files in the package to take user's input, parse input to pandas series, run the series using random forest model, and output the prediction for user's income. 
'''

from data_prediction import *
import pandas as pd

def main():

    #use readFile function to read a user input filepath into a cleaned dataframe
    while True:
       try:
          cleaned_data = readFile()
          break
       except cannot_open_file_exception as e:
          print e
       except pd.parser.CParserError:
           print "Not correct dataset!"
    
    #take and parse user input to prepare data for prediction
    try:
     age = secure_input(age_validation,'\nPlease enter your age: ', parse_func.parse_age) 
     education = secure_input(education_validation,'\nPlease enter your education (choose the best one that represents you: Doctorate, Masters, Bachelors, Associate, Prof-school, Below-12th): ', parse_func.parse_education)
     marital_status = secure_input(marital_validation,'\nPlease enter your marital status (choose the best one that represents you: Married, Married-spouse-absent, Separated, Divorced, Never-married, Widowed): ', parse_func.parse_marital_status)
     ocupation = secure_input(ocupation_validation,'\nPlease enter your occupation (choose the best one that represents you: Adm-clerical, Armed-Forces, Craft-repair, Exec-managerial, Farming-fishing, Handlers-cleaners, Machine-op-inspct, Other-service, Priv-house-serv, Prof-specialty, Protective-serv, Sales, Tech-support, Transport-moving): ', parse_func.parse_ocupation)
     capital_gain = secure_input(capital_gain_validation,'\nPlease enter your capital gain (between 0 and 100000): ', parse_func.parse_capital_gain)
     hours_per_week = secure_input(hours_per_week_validation,'\nPlease enter your working hours per week (between 0 and 100): ',parse_func.parse_hours_per_week) 
    except KeyboardInterrupt:
        sys.exit()
    #if a user inputs unknown for a variable above, we take the mean of the variable in our model data
    dictionary_map = {'age': age, 'education': education, 'martial-status': marital_status, 'ocupation': ocupation, 'capital-gain': capital_gain, 'hours-per-week': hours_per_week}
    #iterate through the dictionary, find which variables are assigned to 100 (unknown), and reassign them to the mean in model data
    for name, value in dictionary_map.items():
        if value == 100:
            value = np.mean(cleaned_data[name])
             
    #read data into panda series 
    data_to_predict = pd.Series(dictionary_map, index = ['age', 'education', 'martial-status', 'ocupation', 'capital-gain', 'hours-per-week'])
    print '\n-------------------------predicting your income level---------------------------'
    #put the serie of data into our random forest model to predict whether a person makes over 50k per year
    output = randomForest(data_to_predict, cleaned_data)
    #randomForest function returns np.ndarray(1), np.ndarray(0). if 1 in output, randomForest returns np.ndarray(1), income >= 50k    
    if 1 in output:
        print '\nAccording to our model prediction, you make over 50 thousands dollars per year.'
    else:
        print '\nAccording to our model prediction, you make less than 50 thousands dollars per year.'

    
if __name__ == '__main__':
    main()
