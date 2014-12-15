"""
Author : Qingxian Lai (ql516)


"""
import sys
from exception_list import *
from Interested_job_list import interested_job_list, job



def job_list_analysis(df, kwd):
    """
    This function build up an interactive system letting the user to learn more
    about his interested jobs. Detail instructions will be shown at the
    beginning of the program.

    argument
    =========
    df: a dataframe
    kwd: string

    """

    df = interested_job_list(df, kwd)          # turn the data frame to a Interested job list object
    df.show_job_list()

    print_list_operator(df.keyword)

    while 1:
        try:
            key = option_input()
            if key == 'm':
                df.map_of_locations(75)
            if key == 'a':
                df.degree_pie_plot()
            if key == 'b':
                df.top_ten_agency()
            if key == 'c':
                df.top_demanding_jobs()
            if key == 'd':
                df.num_of_job_by_date()
            if key == 'e':
                skill_list = df.high_demand_skill()
                print "top demanded skills: "
                print skill_list
            if key == 'g':
                cjob = select_a_job(df)
                if cjob == 'b':
                    df.show_job_list()
                    print_list_operator(df.keyword)
                    continue
                view_job_info(cjob)
                df.show_job_list()
                print_list_operator(df.keyword)
        except wrong_option_exception:
            print "invalid option, please select from [m,a,b,c,d,e,f,g] or input 'q' to quit: "




def print_list_operator(kwd):
    """
    an user menu show at the beginning of the system

    Argument
    ========
    kwd: a string, the keyword user inputted

    """
    print ""
    print "================================  keyword:{}  =========================================".format(kwd)
    print ""
    print "                 You can choose to learn more about this job list: "
    print "              <m>  :  draw a map to show all the job location"
    print "              <a>  :  pie plot show the percentage of degree requirement"
    print "              <b>  :  bar plot show the most hiring agency"
    print "              <c>  :  bar plot show the most demanded positions"
    print "              <d>  :  line plot of the number of job vs date"
    print "              <e>  :  show the most demanded skills of all the related jobs"
    print "              <g>  :  select a job id to get more information about that job"
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
    options = list('mabcdefgq')
    if not(key in options):
        raise wrong_option_exception
    if key == 'q':
        print 'program shut down! bye!'
        sys.exit()
    return key




def select_a_job(df):
    """
    let the user input a id, then verify it. if Valid, return a job object

    Argument
    =======
    df: Dataframe, the job list

    Return:
    if the input id is valid, return a job object, or raise exception

    """
    while 1:
        try:
            job_id = raw_input("please input a Job ID of which you want to learn details: \n")
            if job_id == 'b':
                return 'b'
            id = select_id_job(job_id)
            Job = df.select(id)
            break
        except invalid_ID_Exception:
            print "job id not exist in this list, please try again or type 'b' to go back"
        except id_not_int_exception:
            print "job id should be integer, please try again"
    return Job                 # as described in class, this returns an object




def select_id_job(id_str):
    """
    convert the input string id to integer, if the input is not an integer,
    raise exception

    Argument
    ========
    id_str: the inputted id string

    Return
    ======
    integer

    """
    try:
        id = int(id_str)
    except:
        raise id_not_int_exception
    return id




def view_job_info(Job):
    """
    guide the user to learn more about the job:  detailed job descrption or location on the googlemap

    Argument
    ========
    Job:  a job object

    """
    print "successfully select job: {}".format(Job.id)

    print ""
    print "================================  jb ID:{}  ==========================================".format(Job.id)
    print ""
    print "                 You can choose to learn more about this job: "
    print "              <a>  :  show the detailed information"
    print "              <b>  :  draw the map of its location"
    print "              <q>  :  back to the job list"
    print ""
    print "==========================================================================================="

    while 1:
        try:
            key = job_key_input()
            if key == 'a':
                Job.description()
            if key == 'b':
                Job.location()
            if key == 'q':
                print "Go back to the job list: >>> \n \n >>>"
                break
        except wrong_option_exception:
            print "invalid option, please select from [a,b,q]: "






def job_key_input():
    """
    get the option selected by user, and verify it.

    Return
    ======
    return a verified option

    """
    key = raw_input("your_choice: ")
    options = list('abq')
    if not(key in options):
        raise wrong_option_exception
    return key
