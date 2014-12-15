"""
The overall data set class

Author: Qingxian Lai (ql516)

"""
import numpy as np
from pieplot import plot_educationLevel
from barplot import *
from input_filter import filter_the_job
from scotterplot import plot_scatter



class Job_data:
    """
    The class of the overall job dataset of New York City.

    Local Variables
    ==============
    .data  :  a dataframe contain all the information of NYC Jobs
    .attribute : a numpyt ndarray contain all the attributes of the dataset

    Methods
    =======
    .__init__              :  initialize the object
    .degree_pei_plot       :  pie plot showing the percentage of degree reguirement
    .top_demanding_jobs    :  bar plot showing the top demanding jobs
    .num_of_job_by_date    :  the number of jobs
    .top_ten_agency        :  bar plot showing top recruiting agencies
    .preview_data          :  randomly show part of the dataset
    .scotter_level_salary  :  scatter plot show the relation b/t level and salary
    .keyword_filter        :  match inputted keyword with dataset

    """

    def __init__(self, df):
        self.data = df
        self.attribute = df.columns.get_values()   #this is a numpy ndarray

    def degree_pie_plot(self):
        plot_educationLevel(self.data)

    def top_demanding_jobs(self):
        plot_DemandJob(self.data)

    def num_of_job_by_date(self):
        plot_NumJob_byDate(self.data)

    def top_ten_agency(self):
        plot_numPosition(self.data)

    def preview_data(self):
        job_features = ['Job ID', 'Business Title', 'Agency']
        df = self.data.loc[:, job_features]
        index = np.random.choice(len(df), size=50)
        print df.iloc[index, :]

    def scotter_level_salary(self):
        plot_scatter(self.data)

    def salary_range(self):
        show_salary_range(self.data)

    def keyword_filter(self, keyword):
        """
        match inputted keyword with dataset

        Argument
        ========
        keyword: String

        Return
        ======
        a dataframe

        """
        df = filter_the_job(self.data, keyword)
        return df

    def __repr__(self):
        return "NYC_OFFICIAL_JOB_DATASET Object"

