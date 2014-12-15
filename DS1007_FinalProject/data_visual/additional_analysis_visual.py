# -*- coding: utf-8 -*-
"""This file is for deeper exploration of the dataset. It defines user_info class and plots functions 
   for the related age, working hours per week grahical information
   Author: Mengfei Li (ml4713)
"""

__all__=['user_info', 'pie_chart', 'statistics', 'scatterplot_AgeHours', 'dataPrep_for_plot', 'bar_chart', 'age_workinghours_plot', 'info_validation', 'user_info_scatterVisual']

import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import pandas as pd
import config
import sys
from exception_files_visual import*

unique_education_level=None

class user_info:
    """user_info class, initialized by providing a string input
       For Example: 
         '10,40,>50K'
         '45,30,<=50K'
         
       Attributes:
       age: user's age, type=int
       hours: user's working hours per week, type=int       
    """
    def __init__(self, info):
        try:
            assert(len(info.split(',')) == 3)
            age, hours, self.subcategory = info.split(',')
            if len(age) == 0 or  len(hours) == 0 or len(self.subcategory) == 0:
                raise NotEnoughInfo('Not enough info for analysis!')
            else:
               if self.subcategory in ['>50K', '<=50K']:
                  if '.' in list(age) or '.' in list(hours):
                     raise NotIntegerError('Please enter integers for age and hours')
                  else:
                     self.age = int(age)
                     self.hours = int(hours)
               else:
                 raise NotValidSubcategory(self.subcategory)
        except AssertionError:
            print "Please enter three values!"            
        except ValueError:
            print "Please enter a valid int number!"

        
    def __repr__(self):
        return str(self.age) + ',' + str(self.hours) + ',' + str(self.subcategory)
    
    
def info_validation(information):
    """After user's input, validate his/her age and workinghours 
       as in a resonable range to compare
    """
    if information.age <= 0 or information.age > 100:
        raise NotValidRange_age('Age should be in the range of (0,100]')
    elif information.hours <= 0 or information.hours > 100:
        raise NotValidRange_hours('Hours should be in the range of (0,100]')
    else:
        valid_info = information
        return valid_info
        

def pie_chart(dataset, col_to_plot):
    """pie chart for categorical columns
    """
    y_label = np.unique(dataset.y)[0]
    value_toPlot = dataset[col_to_plot]
    s = sum(value_toPlot.value_counts().values)
    labels = np.unique(value_toPlot)
    sizes = [val/float(s)*100 for val in value_toPlot.value_counts().values] 
    f=plt.figure()
    plt.pie(sizes, labels = labels,autopct = '%1.1f%%',shadow = True,startangle = 90)
    plt.axis('equal')
    plt.title(col_to_plot + ' percentage for people who make ' + y_label)
    plt.show()
    f.savefig('pie_chart for ' + col_to_plot + ' with ' + y_label + '.pdf', x = 0.5, y = 0.6 )
    

def statistics(dataset):
    """Accept a dataset to calculate age and hours-per-week means and standard error means
       based on different education levels.
    """
    age_mean = []
    workingHours_mean = []
    for education in np.unique(dataset.education):
        age_mean.append(np.mean(dataset.age[dataset.education == education]))
        workingHours_mean.append(np.mean(dataset['hours-per-week'][dataset.education == education]))

    age_sem = stats.sem(age_mean)
    workingHours_sem = stats.sem(workingHours_mean)
           
    return pd.Series(age_mean,name = 'age'), pd.Series(workingHours_mean,name = 'workinghours'), age_sem, workingHours_sem
    


def dataPrep_for_plot():
    """This function prepare the data for age_workinghours_plot function 
       return 4 values:
       
       age:Dataframe, columns=['>50K','<=50K'], each column contain the mean age for each education level
       workinghours:Dataframe, columns=['>50K','<=50K'], each column contain the mean workinghours for each education level
       age_sem:age standard error mean
       workinghours_se:workinghours standard error mean
       unique education level
    """
    global unique_education_level
    global age
    global workinghours
    larger_than_50 = config.visual_data[config.visual_data.y == '>50K']
    tmp = config.visual_data[config.visual_data.y == '<=50K']
    less_than_50 = tmp[tmp.education != 'Preschool'] #remove 'Preschool' because it doesn't exsit in larger_than_50
    
    unique_education_level = list(set(larger_than_50.education))
    
    age_mean_1, workingHours_mean_1, age_sem_1, workingHours_sem_1 = statistics(less_than_50)
    age_mean_2, workingHours_mean_2, age_sem_2, workingHours_sem_2 = statistics(larger_than_50)
    
    
    age = pd.concat([age_mean_1,age_mean_2],axis = 1)
    age.columns = ['>50K','<=50K']
    workinghours = pd.concat([workingHours_mean_1,workingHours_mean_2],axis = 1)
    workinghours.columns = ['>50K','<=50K']  
    
    
     #combine for analysis convinence
    age_sem = [age_sem_1,age_sem_2]
    workinghours_sem = [workingHours_sem_1,workingHours_sem_2]
    
    return age, workinghours, age_sem, workinghours_sem

    
    
def bar_chart(data, data_sem, name):
    """bar plot for the given data series
    """
    ind = np.arange(len(unique_education_level))
    width = 0.35
    f=plt.figure()
    f1 = plt.bar(ind, data['>50K'].values, width, color = 'b', yerr = data_sem[0])
    f2 = plt.bar(ind, data['<=50K'].values, width, color = 'r', yerr = data_sem[1], bottom = data['>50K'].values)
    plt.xticks(ind+width/2, unique_education_level, rotation = 90)
    plt.legend((f1[0],f2[0]), ('<=50K','>50K'), loc = 'upper right')
    plt.ylabel(name)
    plt.title('mean values for two categories: <=50K, >50K')   
    plt.show()
    f.savefig('mean_' + name + '.pdf')
    

def user_info_scatterVisual(user_info, database):
    """scatter plot for age as x-axis and working hours as y-axis
       Add user's information on the scatter plot
    """
    AGE = 0
    HOURS = 1
    N_level = len(unique_education_level)
    np.random.seed(52)
    fig=plt.figure()
    ax = fig.add_subplot(1,1,1)        
    plt.scatter(database[AGE], database[HOURS], c = np.random.rand(N_level), alpha = 0.6)
    plt.plot([user_info.age], [user_info.hours], 'g.', markersize = 30.)
    ax.annotate('This is you!',xy = (user_info.age, user_info.hours), xytext = (30,-30), textcoords = 'offset points', arrowprops = dict(arrowstyle = "->"))
    plt.xlabel('age')
    plt.ylabel('hours-per-week')
    plt.title('age VS workingHours for ' + user_info.subcategory)
    plt.show()
    fig.savefig('user_info on our dataset.pdf')
    
def scatterplot_AgeHours(age, hours):
    """This is the scatter plot function for age and hours variable 
       together with user's age and hours for comparison
    """
    while True:
        try:
            print "\n\nINFO INPUT FROM USER IN THE FORMAT OF age,hours,subcategory"
            print "\nFOR EXAMPLE: 35,40,>50K"
            user_input = raw_input('Please enter your age, working hours per week, category to compare(either >50K or <=50K): ')           
            user_input = "".join(user_input.split()) #remove whitespaces
            if user_input == 'quit':
                sys.exit()
            else:
                user_information = user_info(user_input)
                validated_info = info_validation(user_information)
                print "\n\n*******BIG GREEN DOT REPRESENTS YOUR INFORMATION********\n\n"
                if validated_info.subcategory == '>50K':
                  database = [age['>50K'], workinghours['>50K']]
                  user_info_scatterVisual(validated_info, database)
                else:
                  database = [age['<=50K'], workinghours['<=50K']]
                  user_info_scatterVisual(validated_info, database)
                break
        except (NotValidSubcategory, NotEnoughInfo, NotIntegerError, NotValidRange_age, NotValidRange_hours) as e:
           print e
        except AssertionError as e:
            print "Three values are not detected!"
        except AttributeError as e:
            print "Incorrect user info!"
        except ValueError as e:
            print "Please enter a valid number!" 
        except KeyboardInterrupt:
            sys.exit()

           
def age_workinghours_plot():
    """The main plot function for age and workinghours 
       includes bar plots and scatter plots
    """   
    #data preparation
    age, workinghours, age_sem, workinghours_sem = dataPrep_for_plot()    
    #bar_chart
    bar_chart(age, age_sem, 'age for each education level')
    bar_chart(workinghours, workinghours_sem, 'workinghours for each education level')      
    #scatterplot
    scatterplot_AgeHours(age, workinghours)
    
