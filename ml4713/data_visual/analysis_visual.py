# -*- coding: utf-8 -*-
"""Visual Data functions defines feature_category class to functions to perform necessary analysis
   Author: Mengfei Li (ml4713)
"""

__all__ = ['feature_category', 'input_validation', 'plot_function', 'prompt_for_subcategory', 'subcategory_validation', 'add_subcategory_for_plot']

import re
import sys
from exception_files_visual import *
import config
import matplotlib.pyplot as plt
        
        
        
def input_validation(feature, category):
    """This function seperately validates the user input as valid features
       and category, return the values if valid.
    """
    valid_fea = ['hours-per-week','age','education','martial-status','workclass','race','relationship','occupation','capital-gain','capital-loss','native-country']
    valid_cat = ['y','sex']
    #validation for feature input
    for elem in feature:
        if elem not in valid_fea:
            raise NotValidFeature(elem)
    #validation for category input
    if category not in valid_cat:
        raise NotValidCategory(category)
    else:
        valid_feature = feature
        valid_category = category
        return valid_feature, valid_category
                          
        
        

class feature_category:
      """feature_category class, initialized by providing a string input
       For Example:
       ([age,education],y)
       ([workclass,hours-per-week],sex)
       
       Attributes:
          f: type=list, length=2,represents two features user entered in
          c: type=string, represents category user entered in
         
       Methods:
          data_display: display the first 10 rows of selected features
                        and unique values counts for category
          data_summary: statistics report for features and category
      """
      def __init__(self,rep):
          lfbrack, middle, rtbrack = rep[0],rep[1:-1],rep[-1]
          if middle == '':
              raise EmptyError('Not enough information!')
          
          try:
              assert ( lfbrack == '(' )
              assert ( rtbrack == ')' )
              assert ( middle[0] == '[')
              occur = 2
              #split the middle into two parts
              indices = [x.start() for x in re.finditer (",", middle)]
              if len(indices) != 2:
                  raise NotValidInfoAmount('Please enter two features, one cateogry')
              assert ( middle[indices[occur-1]-1] == ']')
              f = middle[0:indices[occur-1]]
              f_tmp = [f.split(',')[0][1:], f.split(',')[1][:-1]]
              c_tmp = middle[indices[occur-1]+1:] 
              #store into class after validation
              self.f, self.c = input_validation(f_tmp, c_tmp)
          except AssertionError: 
             raise NotValidForm(rep)

       
       
      def __repr__(self):
        return lfbrack + str(self.f) + ',' + self.c + rtbrack
        
        
      def data_display(self):
          print "\nFirst 10 rows in selected features: "
          print config.visual_data[self.f[0]][:10]
          print config.visual_data[self.f[1]][:10]
          print "\nUnique Values for selected Category: "
          print config.visual_data[self.c].value_counts()
              
      def data_summary(self):
          feature_summary = [config.visual_data[elem].describe() for elem in self.f] 
          category_summary = config.visual_data[self.c].describe()                 
          print feature_summary, category_summary 
              
        
        
def plot_function(fea_cat, sub_category):
    """This function plots user input features according to its datatype with 
       corresponding sub_category.
    """
    #construct the sub dataset 
    data_cat = config.visual_data[config.visual_data[fea_cat.c] == sub_category]

    for elem in fea_cat.f:
        data_fea = data_cat[elem]
        if elem in config.num_col:  #plot histogram if it is a numerical data
           f1 = plt.figure()
           ax1 = f1.add_subplot(111)
           ax1.hist(data_fea.values)  
           plt.xlabel(elem)
           plt.ylabel(elem+' frequency')
           plt.title('histogram for ' + elem + ' with ' + sub_category)  
           plt.show()
           f1.savefig('histogram_' + elem + ' with ' + sub_category + '.pdf')
        elif elem in config.cat_col: #plot bar graph if it is a categorical value
            ind = range(len(set(data_fea)))
            f2 = plt.figure()
            ax2 = f2.add_subplot(111)
            ax2.bar(ind, data_fea.value_counts())
            plt.xlabel(elem)
            plt.ylabel(elem + ' frequency')
            plt.xticks(ind, data_fea.value_counts().index, rotation = 90)
            plt.title('bar plot for '+ elem + ' with ' + sub_category)
            plt.show()
            f2.savefig('bar_plot_'+ elem + ' with '+ sub_category + '.pdf')
                       

def prompt_for_subcategory(user_category):
    """Ask user for sub category 
    """
    if user_category == 'y':
       return raw_input("Choose from >50K or <=50K (Upper Case): " )
    else:
       return raw_input("Choose from 'Female' or 'Male': ")
    
    

def subcategory_validation(category, input_func_result):
    """This function validate the subcategory entered by user
    """
    sub_tobe_evaluated = input_func_result
    sub_tobe_evaluated = "".join(sub_tobe_evaluated.split())
    if sub_tobe_evaluated == 'quit':
        sys.exit()
    else:
       if category == 'y':
          assert(sub_tobe_evaluated in ['>50K', '<=50K']) 
          valid_sub = sub_tobe_evaluated
          return valid_sub
       elif category == 'sex':
          assert (sub_tobe_evaluated in ['Female','Male'])
          valid_sub = sub_tobe_evaluated
          return valid_sub

        
    
            
def add_subcategory_for_plot(fea_cat):
    """Plot the selected features after validation for subcategory based on 
       category
    """
    
    while True:
          try:
              sub_cat = subcategory_validation(fea_cat.c, prompt_for_subcategory(fea_cat.c))
              plot_function(fea_cat, sub_cat)
              break
          except AssertionError:
              print "Not Valid Subcategory for corresponding category"
          except KeyboardInterrupt:
              sys.exit()

