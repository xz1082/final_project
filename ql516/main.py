"""
This is the main module of the project, all the functions are imported from package NYC_Official_Jobs

Author: Qingxian Lai (ql516)

"""

import pandas as pd
from NYC_Official_Jobs import *
import sys


def main():
    """
    The whole project start here.
    """

    # start at loading the dataset
    raw_data = safely_input()
    print "dataset loaded successfully >>>"
    print ">>>",

    # Then clean the data
    job_data = Clean_df(raw_data)
    print "data cleaned >>>"

    # search for interested jobs
    job_list, keyword = overall_analysis(job_data)
    "Matching >>>"

    # analysis this job list
    if type(job_list) == pd.DataFrame:
        job_list_analysis(job_list, keyword)
    elif type(job_list) == pd.Series:
        one_job_info(job_list)
    # program end

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        sys.exit()

