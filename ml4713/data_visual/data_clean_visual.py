"""This file take user file path input and clean the data after correctly readin.
   Author: Mengfei Li (ml4713)
"""


import pandas as pd
import sys 
import os.path
from exception_files_visual import ReadFileError

__all__ = ['filePath_validation', 'clean_data_for_visual']

    
def filePath_validation(f_path):
    """Take file_inputFunc to assign the value to f_path
       Validate the input
    """
    f_path = "".join(f_path.split())
    if f_path == 'quit':
        sys.exit()
    elif os.path.isfile(f_path):
        valid_path = f_path
        return valid_path
    else:
        raise ReadFileError('Not correct file path')
    

def clean_data_for_visual(f_path):
    """Clean the dataset by assigning column names and modify the format of categorical values 
    """
    head = ['age','workclass','fnlwgt','education','education-num','martial-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','y']
    file_path_validated = filePath_validation(f_path)
    uncleaned_data = pd.read_csv(file_path_validated, header = None)       
    if uncleaned_data.shape == (32562,15): #make sure it is the correct dataset
       uncleaned_data.columns = head
       col_to_edit = ['workclass','education','martial-status','occupation','relationship','sex','native-country','race','y']
       for col in col_to_edit:
           uncleaned_data[col] = uncleaned_data[col].map(lambda x:str(x).strip()) #remove whitespace in categorical values
           cleaned_data = uncleaned_data[uncleaned_data['y']!='nan']
       return cleaned_data
    else:
       raise ReadFileError('Not correct dataset')

        
           
