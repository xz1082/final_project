"""
interested job list class

Author: Qingxian Lai

"""

from Job_list_overall import Job_data
from input_filter import filter_the_job
from map_of_location import plot_the_location_map, plot_one_job_location
from jobDescription import show_job_infomation_s, show_job_infomation_df
from exception_list import invalid_ID_Exception
from display_preferred_skill import display_preferred_skill


class interested_job_list(Job_data):

    """
    The class of the user interested job

    parent
    ======
    Job_data class

    Local Variables
    ==============
    .data  :  a dataframe
    .keyword : string
    .attribute : a numpyt ndarray contain all the attributes of the dataset


    Methods
    =======
    .__init__              :  initialize the object
    .degree_pei_plot       :  pie plot showing the percentage of degree reguirement
    .top_demanding_jobs    :  bar plot showing the top demanding jobs
    .num_of_job_by_date    :  the number of jobs
    .top_ten_agency        :  bar plot showing top recruiting agencies
    .scotter_level_salary  :  scotter plot show the relation b/t level and salary
    .keyword_filter        :  match inputted keyword with dataset
    .show_job_list         :  printting job id and job title of all the jobs on the list
    .high_demand_skills    :  most popular skill through all the jobs on the list
    .map_of_location       :  draw a map showing all the jobs' location
    .select                :  select a certain job from the list using job id

    """


    def __init__(self, df, kwd):
        self.data = df
        self.keyword = kwd
        self.attribute = df.columns.get_values()   #this is a numpy ndarray

    def map_of_locations(self, num):
        """
        Argument
        =======
        num: the maximum number of location shown on one map
        """
        plot_the_location_map(self.data, num, self.keyword)

    def filter_kwd(self):
        self.data = filter_the_job(self.data,self.keyword)

    def show_job_list(self):
        show_job_infomation_df(self.data)

    def high_demand_skill(self):
        skill_list = display_preferred_skill(self.data)
        return skill_list

    def _verify(self, job_id):
        """
        verify the job_id user inputted, if it is invalid, raise exception

        Argument
        ========
        job_id: integer

        """
        if not(job_id in self.data.loc[:, 'Job ID'].values):
            raise invalid_ID_Exception

    def select(self, job_id):
        """
        select a job on the list using job_id

        Argument
        ========
        job_id: integer

        Return
        ======
        a job object

        """
        self._verify(job_id)            # if invalid, raise an exception
        selected_job = self.data[self.data['Job ID'] == job_id].iloc[0, :]
        return job(selected_job)

    def __repr__(self):
        return "Job list corresponding to keyword '{}'".format(self.keyword)


class job:
    """
    job class

    Local variable
    ==============
    .data   :    a series with attributes as its index
    .id     :    the job's id
    .title  :    the job's title

    Methods
    =======
    .description :  showing the detailed information about this job
    .location    :  showing this job's location on a map

    """
    def __init__(self,job):
        self.data = job                 # job should be a pandas Series with attributes as its index
        self.id = job['Job ID']
        self.title = job['Business Title']

    def description(self):
        show_job_infomation_s(self.data)

    def location(self):
        plot_one_job_location(self.id)

    def __repr__(self):
        return "Detailed information about job '{}'".format(self.title)




