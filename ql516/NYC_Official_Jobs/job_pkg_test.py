"""
Author : Qingxian Lai (ql516)

"""

import unittest
from input_func import get_input
from exception_list import *
from Interested_job_list import interested_job_list
from input_filter import filter_the_job
from job_list_analysis import select_id_job
from Dataloading import Clean_df
import pandas as pd


class TestInputFuntions(unittest.TestCase):

    def setUp(self):
        self.df = pd.read_csv("../NYC_Jobs.csv")

    def test_testcase_1(self):
        self.assertRaises(IOError,get_input, 'aldsfjalf')

    def test_testcase_2(self):
        df = get_input("../NYC_Jobs.csv")
        self.assertEqual(pd.DataFrame, type(df))


class TestClassJobListMethod(unittest.TestCase):

    def setUp(self):
        self.df = Clean_df(pd.read_csv("../NYC_Jobs.csv"))
        self.job_list = filter_the_job(self.df,'data')
        self.job_obj = interested_job_list(self.job_list,'data')
        self.id = 160045
        self.job_str = 'Information Modeler (Data Architect)'

    def test_case1(self):
        self.assertRaises(invalid_ID_Exception, self.job_obj.select, 523159)

    def test_case2(self):
        job = self.job_obj.select(self.id)
        self.assertEqual(self.job_str, job.title)


class TestFunctionSelectIdJob(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(150023, select_id_job('150023'))

    def test_case2(self):
        self.assertRaises(id_not_int_exception, select_id_job, 'dafsaf')


if __name__ == "__main__":
    unittest.main()
