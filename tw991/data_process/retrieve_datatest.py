"""
Creator: Sylvia Zhao

Contributor: Wenxi Lei, Tian Wang
"""

from retrieve_data import *
from retrieve_dataexceptions import *
from retrieve_datacheck import *
from userfile_checks import *
from userfile_exceptions import *
import unittest

class test_data_process(unittest.TestCase):
    """
    Test tretrieve_data and userfile functions
    """
    def setUp(self):
        self.validstock = 'F'
        self.invalidstock = 'badstock'
        self.validsource1 = 'google'
        self.validsource2 = 'yahoo'
        self.invalidsource = 'badsource'
        self.string = 'user.csv'
        self.istring = 'blah.csv'
        self.validstart = '2012/2/29'
        self.validend = '2012/5/1'
        self.invalidend1 = '2012/2/30'
        self.invalidend2 = '2010/1/1'
        self.invalidend3 = '3000/1/1'
        self.sameend =  '2012/2/29'
        self.empty = ''
        
    def test_empty_checkinput(self):
        self.assertEqual(empty_checkinput(self.validstock), 0)
        self.assertEqual(empty_checkinput(self.invalidstock), 0)
        self.assertRaises(EmptyString, empty_checkinput, self.empty)
    
    def test_source_checkinput(self):
        self.assertEqual(source_checkinput(self.validsource1), 0)
        self.assertEqual(source_checkinput(self.validsource2), 0)
        self.assertRaises(BadSource, source_checkinput, self.invalidsource)
    
    def test_dates_checkinput(self):
        self.assertEqual(dates_checkinput(self.validstart, self.validend), 0)
        self.assertRaises(BadDate, dates_checkinput, self.validstart, self.sameend)
        self.assertRaises(BadDate, dates_checkinput, self.validstart, self.invalidend2)
        self.assertRaises(BadDate, dates_checkinput, self.validstart, self.invalidend3)
        self.assertRaises(ValueError, dates_checkinput, self.validstart, self.invalidend1)

    def test_gui_checkinput(self):
        self.assertEqual(gui_checkinput(self.validstock, self.validsource1, self.validstart, self.validend), 0)
    
    def test_empty_checkuser(self):
        self.assertEqual(empty_checkuser(self.string), 0)
        self.assertEqual(empty_checkinput(self.istring), 0)
        self.assertRaises(UserEmptyString, empty_checkuser, self.empty)
