"""
function used to clean the raw dataset

Author: Jianming Zhou (jz1584)

"""

import pandas as pd
import warnings


def Clean_df(df):
    """
    clean the raw dataset, convert date type drop duplicate, drop invalid entries

    argument
    ========
    df: the raw dataframe

    return
    ======
    a cleaned dataframe

    """
    warnings.filterwarnings('ignore')
    df['Posting Date'] = pd.to_datetime(df['Posting Date'])         # converted to 'date' type

    #remove duplicate since some jobs opening to internal and external share the same job id
    df1 = df.drop_duplicates(cols=['Job ID'])

    #number of open position should not be more than 100 for each job id,otherwise it's abnormal
    df2 = df1[df1['# Of Positions'] < int(100)]

    return df2