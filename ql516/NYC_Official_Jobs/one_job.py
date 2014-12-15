"""
Author: Qingxian Lai (ql516)

"""
import sys
from exception_list import *
from Interested_job_list import job



def one_job_info(Job):
    """
    This function used to display an interactive system letting the user to learn more
    about the only one job.

    argument
    =========
    df: a pandas Series with attributes as its index

    """

    Job = job(Job)         #turn it into a object
    print "successfully select job: {}".format(Job.id)

    print ""
    print "================================  jb ID:{}  ==============================".foramt(Job.id)
    print ""
    print "                 You can choose to learn more about this job: "
    print "              <a>  :  show the detailed information"
    print "              <b>  :  draw the map of its location"
    print "              <q>  :  quit the program"
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
                print "progarm shut down, bye!"
                sys.exit()
        except wrong_option_exception:
            print "invalid option, please select from [a,b,q]: "



def job_key_input():
    """
    get the option selected by user, and verify it.

    Return
    ======
    return a verified option

    """
    key = raw_input("your_choose: ")
    options = list('abq')
    if not(key in options):
        raise wrong_option_exception
    return key