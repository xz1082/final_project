"""
Author: Qingxian Lai (ql516)

"""
import sys
from exception_list import *
from Job_list_overall import Job_data
from input_filter import filter_the_job

def overall_analysis(df):
    """
    This function used to display an interactive system letting the user to learn more
    about the offcial job market in NYC. Detail instructions will be shown at the
    beginning of the program.

    argument
    =========
    df: a dataframe

    return
    ======
    if the user choose to search a keyword. this function will return a dataframe contain
    all the ralated jobs.
    """

    df = Job_data(df)
    print_menu()

    while 1:
        try:
            key = option_input()
            if key == 'a':
                df.degree_pie_plot()
            if key == 'b':
                df.top_ten_agency()
            if key == 'c':
                df.top_demanding_jobs()
            if key == 'd':
                df.num_of_job_by_date()
            if key == 'e':
                df.scotter_level_salary()
            if key == 'f':
                df.preview_data()
            if key == 'g':
                while 1:
                    try:
                        job_list, keyword = search_keyword(df.data)
                        break
                    except no_related_jobs_exception:
                        print "Sorry, we cannot find jobs related to your keyword, please try another one, " \
                              "or you can input 'p' to go back: \n "
                if keyword == 'back':
                    print_menu()
                    continue
                break
        except wrong_option_exception:
            print "invalid option, please select from [a,b,c,d,e,f,g] or input 'q' to quit: "
    return job_list, keyword



def print_menu():
    """
    print the overall analysis menu

    """
    print "================================  NYC Official Job Analysis  =============================="
    print ""
    print "                 You can choose to learn more about the whole dataset: "
    print "              <a>  :  pie plot show the percentage of degree requirement"
    print "              <b>  :  bar plot show the most hiring agency"
    print "              <c>  :  bar plot show the most demanded positions"
    print "              <d>  :  line plot of the number of job vs date"
    print "              <e>  :  scatter plot show the relationship b/t level and salary"
    print "              <f>  :  get a preview about the whole dataset"
    print "              <g>  :  search for a keyword about jobs you interested in"
    print "              <q>  :  quit the program"
    print ""
    print "==========================================================================================="



def option_input():
    """
    get the option selected by user, and verify it.

    Return
    ======
    return a verified option

    """
    key = raw_input("your_choice: ")
    options = list('abcdefgq')
    if not(key in options):
        raise wrong_option_exception
    if key == 'q':
        print 'program shut down! bye!'
        sys.exit()
    return key


def search_keyword(df):
    """
    guide the user to input a keyword, and match it to the whole dataset to find related
    jobs. if find, return it as a dataframe or a Series; or raise a exception

    Argument
    ========
    df: the whole dataset

    Return
    ======
    a dataframe or a Series

    """
    keyword = raw_input("please input a keyword of the job you interested in: \n")
    if len(keyword) <= 1:
        raise no_related_jobs_exception
    if keyword == 'p':
        return 'stop', 'back'
    job_list = filter_the_job(df, keyword)
    if len(job_list) == 0:
        raise no_related_jobs_exception
    return job_list, keyword

