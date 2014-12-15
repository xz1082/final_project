# -*- coding: utf-8 -*-
"""UnitTest Files to test modules related to data visualization
   Author: Mengfei Li (ml4713)
"""
from analysis_visual import *
from additional_analysis_visual import *
from exception_files_visual import *
from data_clean_visual import *
from config import *
import unittest


class test_filePath_validation(unittest.TestCase):
    """This test is aimed for testing the filePath_validation function
       1. Test ReadFileError: file path incorrect
    """

    def test_ReadFileError1(self):
        fake_path1 = '/Users/mengfeili/downloads/adult.txt'
        self.assertRaises(ReadFileError, filePath_validation, fake_path1)
    def test_ReadFileError2(self):
        fake_path2 = 'thisisnotevenapath'
        self.assertRaises(ReadFileError, filePath_validation, fake_path2)
        
        
class test_feaCat_class(unittest.TestCase):
    """This test is aimed to test class feature_category in visual_data_functions
       file.
       1. Test for two exceptions: NotValidForm, Empty Error
       2. Test class's methods: self.f and self.c
    """
    def test_form_1(self):
        trial = '[a,b],c'
        self.assertRaises(NotValidForm, feature_category, trial)
    def test_form_2(self):
        trial = '(a,b,)'
        self.assertRaises(NotValidForm, feature_category, trial)
    def test_form_3(self):
        trial = '[a,b,c],e'
        self.assertRaises(NotValidForm, feature_category, trial)
    def test_emptyError1(self):
        trial = '#!'
        self.assertRaises(EmptyError, feature_category, trial)
    def test_emptyError2(self):
        trial = '()'
        self.assertRaises(EmptyError, feature_category, trial)
    def test_methods1(self):
        trial = feature_category('([age,education],y)')
        self.assertEqual(trial.f, ['age','education'])
        self.assertEqual(trial.c, 'y')
        
class test_inputValidation(unittest.TestCase):
    """This test is aimed for testing the input_validation functions in 
       visual_data_functions file.
       1. Test the return boolean value either with the true feature/category 
          or invalid feature/category
    """        
    def test_bool1(self):
        valid_input_feature = ['age', 'workclass']
        valid_input_category = 'y'
        self.assertTrue(input_validation(valid_input_feature, valid_input_category))
    def test_bool2(self):
        invalid_input_feature = ['error1','error2']
        valid_input_category = 'y'
        self.assertRaises(NotValidFeature, input_validation, invalid_input_feature, valid_input_category)
    def test_bool3(self):
        invalid_input2_feature = ['age','error1']
        valid_input2_category = 'sex'
        self.assertRaises(NotValidFeature, input_validation, invalid_input2_feature, valid_input2_category)
    def test_bool4(self):
        valid_input3_feature = ['age', 'education']
        invalid_input3_category = 'relationship'
        self.assertRaises(NotValidCategory, input_validation, valid_input3_feature, invalid_input3_category)
        

class test_subcategoryValidation(unittest.TestCase):
    """This test is aimed for testing Subcategory_validation function
       in visual_data_functions file
       1. Test the Exceptions: NotValidSubcategory
    """
    def test_notValidSubcategry(self):
        self.assertRaises(AssertionError, subcategory_validation, 'y', '>=50K')
        self.assertRaises(AssertionError, subcategory_validation, 'sex', '>50K')

class test_userInfo(unittest.TestCase):
    """This test is aimed for testing user_info class in additional_analysis file
       1. Exceptions Test: NotIntegerError, NotEnoughInfo
       2. Test the class's attributes: age, hour, subcategory
    """
    def test_NotIntegerError1(self):
        fake_info1 = '10.22,30,>50K'
        self.assertRaises(NotIntegerError,user_info, fake_info1)
    def test_NotIntegerError2(self):
        fake_info2 = '30,5.4,>50K'
        self.assertRaises(NotIntegerError,user_info, fake_info2)
    def test_Attributes(self):
        real_info = '20,30,>50K'
        self.assertEquals(user_info(real_info).age, 20)
        self.failUnlessEqual(user_info(real_info).hours, 30)
        self.failUnlessEqual(user_info(real_info).subcategory,'>50K')
        
class test_infoValidation(unittest.TestCase):
    """This test is aimed for testing info_validation function in additional_analysis file
       1. Exceptions Tests: NotValidRange_age, NotValidRange_hours
       2. Valid Value returned
    """    
    def test_NotValidRange(self):
        invalid_age1 = user_info('300,50,>50K')
        invalid_age2 = user_info('-20,50,>50K')
        invalid_hours1 = user_info('40,300,>50K')
        invalid_hours2 = user_info('40,-50,>50K')
        self.assertRaises(NotValidRange_age, info_validation, invalid_age1)
        self.assertRaises(NotValidRange_age, info_validation, invalid_age2)
        self.assertRaises(NotValidRange_hours, info_validation, invalid_hours1)
        self.assertRaises(NotValidRange_hours, info_validation, invalid_hours2)
        


if __name__=='__main__':
    unittest.main()
