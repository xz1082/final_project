# -*- coding: utf-8 -*-
"""Programming for Data Science 
   Final Project Data Visualization
   Main file contains functions for user interactions and data visual display
   Author: Mengfei Li (ml4713)
"""


from data_visual import *
import pandas as pd
import sys


def main():
    #read data from file and store it across modules
    #Overview of data if corrected read in
    while True:
        try:
             user_input_filePath = raw_input('Please enter the file path: ')  
             config.visual_data = set_global_data(user_input_filePath)
             break
        except ReadFileError as e:
            print e
        except pd.parser.CParserError:
            print "Not correct file for this program!"
        except KeyboardInterrupt:
            sys.exit()
            
            
    print "\n\n--------DATA INFORMATION----------"
    print "DATA SHAPE: ", config.visual_data.shape 


    
    print "\n******************DATA VISUALIZATION******************"\
          "\n------------------------------------------------------"\
          "\n------------------------------------------------------"\
          "\n-------USER INPUT FOR SELECTED COLUMNS DISPLAY--------"\
          "\n------------------------------------------------------"\
          "\n------------------------------------------------------"\
          "\n******************DATA VISUALIZATION******************"          
    while True:
      try:
         print "\nChoose features from: ", str(['age', 'education', 'martial-status', 'occupation', 'capital-gain', 'capital-loss', 'hours-per-week', 'race', 'relationship'])
         print "\nChoose Category from: ", str(['y','sex'])
         print "\n FORMAT: ([a,b],c)"
         user_input = raw_input('Please enter 2 features and 1 category: ')
         user_input = "".join(user_input.split()) #remove whitespaces
         if user_input == 'quit':
           print "program stopped"
           sys.exit()
         else:
           try:
             fea_cat = feature_category(user_input)
             break
           except (NotValidForm, NotValidInfoAmount, EmptyError, NotValidFeature, NotValidCategory, AssertionError) as e:
                print e
      except KeyboardInterrupt:
        sys.exit()
        
        
        
    #Data Report chosen by user 
    print "\n-------------Data Display-------------------\n"
    fea_cat.data_display() 
    print "\n---------Data Statistics Summary------------\n"
    fea_cat.data_summary()  
    print "\n---------------Data Plots-------------------\n"          
    add_subcategory_for_plot(fea_cat) #user add additional information for more plots
          
    print "\n\n----------Additional Data Analysis-------------"
    print "\n-------------Pie Chart for Sex--------------\n"
    #Two pie chart for people who makes over 50K and less than 50K
    pie_chart(config.visual_data[config.visual_data.y == '>50K'],'sex')
    pie_chart(config.visual_data[config.visual_data.y == '<=50K'],'sex')
    
    #graphs for 'age' and 'working hours' and asking user's info for visual comparison 
    print "\n---------Age and Working Hours Plots--------\n"
    age_workinghours_plot()
    
    print "\n***************DATA VISUALIZATION ENDED***************"\
          "\n------------------------------------------------------"\
          "\n------------------------------------------------------"\
          "\n----------------------THANK YOU!----------------------"\
          "\n------------------------------------------------------"\
          "\n------------------------------------------------------"\
          "\n***************DATA VISUALIZATION ENDED***************"
    

if __name__ == "__main__" :
     main()
     
      

       
       
           
