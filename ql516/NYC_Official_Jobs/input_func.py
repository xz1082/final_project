"""
checking the loaded dataset

Author: Qingxian Lai (ql516)

"""
import pandas as pd
import sys
from exception_list import *

def safely_input():
    """
    used at the start of main function. safely input the data set from the external csv file.
    Raise exception when input failed

    return
    ======
    a verified DataFrame

    """
    print "Welcome! \n"
    path = "NYC_Jobs.csv"
    while 1:
        try:
            raw_data = get_input(path)
            break
        except IOError:
            path = raw_input( "Can not locate the dataset file, type in a valid path or type 'quit' to exit \n")
        except Wrong_dataset_exception:
            path = raw_input( "Load a wrong dataset, please type in a valid path or type 'quit' to exit \n")
        if path == 'quit':
            sys.exit()
    return raw_data


def get_input(path):
    """
    given a file path, verify the input dataset

    argument
    ========
    path: string showing the path of .csv file

    return
    ======
    checked dataframe

    """
    df = pd.read_csv(path)
    attri = [u'Job ID', u'Agency', u'Posting Type', u'# Of Positions', u'Business Title', u'Civil Service Title',
             u'Title Code No', u'Level', u'Salary Range From', u'Salary Range To', u'Salary Frequency',
             u'Work Location', u'Division/Work Unit', u'Job Description', u'Minimum Qual Requirements',
             u'Preferred Skills', u'Additional Information', u'To Apply', u'Hours/Shift', u'Work Location 1',
             u'Recruitment Contact', u'Residency Requirement', u'Posting Date', u'Post Until', u'Posting Updated',
             u'Process Date']

    for i in df.columns:
        if not(i in attri):
            raise Wrong_dataset_exception
    return df