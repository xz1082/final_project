# -*- coding: utf-8 -*-
"""In order to use the dataset acorss the module, this file avoid the problem
   for data read in multiple times.
   Author: Mengfei Li (ml4713)
"""
__all__=['set_global_data']

from data_clean_visual import clean_data_for_visual
       
def set_global_data(f_path):
    """This function enable user to use the data globally across the modules
    """
    return clean_data_for_visual(f_path) 

visual_data = None 
#specify the category columns and numerical columns for future analysis       
cat_col = ['workclass','education','occupation','relationship','sex','native-country','y','race','martial-status']
num_col = ['age','capital-gain','capital-loss','hours-per-week']
