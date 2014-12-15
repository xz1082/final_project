''' 
Author: Chris Zhou, Contributor: Meina Zhou
This module contains unittest functions. Those unittest functions test all the functions that have been used in this package.'
'''

import unittest
from user_input_process_prediction import *
from model_prediction import *
import mock 

class test_age_validation(unittest.TestCase):
    '''This class contains functions that test the functionality of age_validation function.'''
    
    def test_ageRange(self):
        self.assertFalse(age_validation('10'))
    
    def test_ageSpace(self):
        self.assertTrue(age_validation(' 20 '))
    
    def test_ageAlphabet(self):
        self.assertFalse(age_validation('abc'))
    
    def test_ageTrue(self):
        self.assertTrue(age_validation('30'))

class test_education_validation(unittest.TestCase):
    '''
    This class contains functions that test the functionality of the education_validation function.
    '''
    def test_educationIncorrectName(self):
        self.assertFalse(education_validation('college'))
    
    def test_educationNumbers(self):
        self.assertFalse(education_validation('123'))
    
    def test_educationSpace(self):
        self.assertTrue(education_validation(' Doctorate '))
    
    def test_educationTrue(self):
        self.assertTrue(education_validation('Associate'))

class test_marital_validation(unittest.TestCase):
    '''
    This class contains functions that test the functionality of marital_validation function.
    '''
    def test_maritalIncorrectName(self):
        self.assertFalse(marital_validation('single'))
    
    def test_maritalNumbers(self):
        self.assertFalse(marital_validation('123Married'))
    
    def test_maritalSpace(self):
        self.assertTrue(marital_validation(' Never-married '))
    
    def test_maritalTrue(self):
        self.assertTrue(marital_validation('Divorced'))
        
class test_ocupation_validation(unittest.TestCase):
    '''
    This class contains functions that test the functionality of ocupation_validation function.
    '''
    def test_ocupationIncorrectName(self):
        self.assertFalse(ocupation_validation('manager'))      
    
    def test_ocupationNumbers(self):
        self.assertFalse(ocupation_validation('123Sales'))
    
    def test_ocupationSpace(self):
        self.assertTrue(ocupation_validation('  Sales   '))
    
    def test_ocupation_True(self):
        self.assertTrue(ocupation_validation('Prof-specialty'))
        self.assertTrue(ocupation_validation('Farming-fishing'))
    
class test_capital_gain_validation(unittest.TestCase):
    '''
    This class contains functions that test the functionality of capital_gain_validation function.
    '''
    def test_capital_gain_Range(self):
        self.assertFalse(capital_gain_validation('-1'))
        self.assertFalse(capital_gain_validation('200000000'))
        
    def test_capital_gain_space(self):
        self.assertTrue(capital_gain_validation('     1000   '))
    
    def test_capital_gain_alphabet(self):
        self.assertFalse(capital_gain_validation('fdsfds'))
    
    def test_capital_gain_true(self):
        self.assertTrue(capital_gain_validation('1200'))
    
class test_hours_per_week_validation(unittest.TestCase):
    '''
    This class contains functions that test the functionality of hours_per_week_validation function.
    '''
    def test_hours_per_week_Range(self):
        self.assertFalse(hours_per_week_validation('-10'))
        self.assertFalse(hours_per_week_validation('200'))
    
    def test_hours_per_week_space(self):
        self.assertTrue(hours_per_week_validation('     50   '))

    def test_hours_per_week_alphabet(self):
        self.assertFalse(hours_per_week_validation('fdsfds'))
    
    def test_hours_per_week_true(self):
        self.assertTrue(hours_per_week_validation('30'))
    
class test_parsefunc(unittest.TestCase):
    '''
    This class contains functions that test the functionality all parse functions.
    '''
    def setUp(self):
        self.parse_object = parse_func()
    
    def test_parseAge(self):
        self.assertEqual(self.parse_object.parse_age('30'), 30)
    
    def test_parseEducation(self):
        self.assertEqual(self.parse_object.parse_education('Doctorate'), 1)
        self.assertEqual(self.parse_object.parse_education('Below-12th'), 6)
    
    def test_parseMaritalStatus(self):
        self.assertEqual(self.parse_object.parse_marital_status('Married-spouse-absent'), 2)
        self.assertEqual(self.parse_object.parse_marital_status('Widowed'), 4)
    
    def test_parseOcupation(self):
        self.assertEqual(self.parse_object.parse_ocupation('Adm-clerical'), 0)
        self.assertEqual(self.parse_object.parse_ocupation('Other-service'), 7)
    
    def test_parseCapitalGain(self):
        self.assertEqual(self.parse_object.parse_capital_gain('10000'), 10000)
        
    def test_parseHoursPerWeek(self):
        self.assertEqual(self.parse_object.parse_hours_per_week('40'), 40)
        
    def tearTown(self):
        self.parse_object = None

class test_secure_input(unittest.TestCase):
    '''
    This class contains functions that test the functionality of the secure_input function.
    '''
    
    def testSecureInput(self):
        with mock.patch('__builtin__.raw_input', return_value='20'):
            self.assertEqual(secure_input(age_validation, 'please enter your age: ', parse_func.parse_age), 20)
    
    def testSecureInputFalse(self):
        with mock.patch('__builtin__.raw_input', return_value='Masters'):
            self.assertEqual(secure_input(education_validation, 'please enter your education: ', parse_func.parse_education), 2)


if __name__ == '__main__':
    unittest.main()
    
    