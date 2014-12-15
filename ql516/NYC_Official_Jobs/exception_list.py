"""
User defined exceptions

Author: Qingxian Lai (ql516)

"""

## Exception in class interested_job_list ================
class invalid_ID_Exception(Exception):
    pass

# safely input ===========================================
class Wrong_dataset_exception(Exception):
    pass

class wrong_option_exception(Exception):
    pass

class no_related_jobs_exception(Exception):
    pass

class id_not_int_exception(Exception):
    pass