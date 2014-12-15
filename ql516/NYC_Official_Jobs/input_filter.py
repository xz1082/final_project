"""
Function used to match keyword with the dataset

Author: Qingxian lai (ql516)

"""

import pandas as pd


def filter_the_job(df, keyword):
    """
    input a datafame and a keyword, return all the job that related to this keyword
    return type: datafame

    Argument
    ========
    df: DataFrame
    keyword : string

    Return
    ======
    a filtered DataFrame

    """

    keyword = keyword.lower()
    keyword1 = keyword[0].upper() + keyword[1:]
    filtered = df[df.apply(lambda x:(keyword in x[u"Business Title"]) \
                                    or (keyword1 in x[u"Business Title"])\
                                    or (keyword in df[u"Job Description"])\
                                    or (keyword1 in df[u"Job Description"]), axis=1)]
    return filtered
