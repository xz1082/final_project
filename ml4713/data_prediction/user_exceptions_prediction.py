'''
Author: Meina Zhou, Contributor: Chris Zhou
This module contains all the user exception classes for all files in this package.  
'''

class cannot_open_file_exception(Exception):
    '''
    Raise exception when the file path doesn't exist or cannot be opened.
    '''
    def __str__(self):
        return 'Incorrect file path. The file cannot be opened.'

class invalid_input_exception(Exception):
    '''
    Raise exception when unable to read user's keyboard input.
    '''
    def __str__(self):
        return 'The user input cannot be read.'

class invalid_age_exception(Exception):
    '''Raise exception when the input of age is not a valid integer.'''
    def __str__(self):
        return 'The input of age is not a valid integer.' 

class out_of_range_age_exception(Exception):
    '''Raise exception when the input of age is out of the range [18,70].'''
    def __str__(self):
        return 'The input of age is out of the range [18,70].'
    

class invalid_capital_gain_exception(Exception):
    '''Raise exception when the input of capital gain is not a valid integer.'''
    def __str__(self):
        return 'The input of capital gain is not a valid integer.'
        
class out_of_range_capital_gain_exception(Exception):
    '''Raise exception when the input of capital gain is out of the range [0,100000].'''
    def __str__(self):
        return 'The input of capital gain is out of the range [0,100000].'

class invalid_hours_per_week_exception(Exception):
    '''Raise exception when the input of hours per week is not a valid integer.'''
    def __str__(self):
        return 'The input of hours per week is not a valid integer.'
        
class out_of_range_hours_per_week_exception(Exception):
    '''Raise exception when the input of capital gain is out of the range [0,100].'''
    def __str__(self):
        return 'The input of capital gain is out of the range [0,100].'

class unable_to_parse_exception(Exception):
    '''
    Raise exception when inputs are unable to parse.
    '''
    def __str__(self):
        return 'Cannot parse string'


        