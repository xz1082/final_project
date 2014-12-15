# -*- coding: utf-8 -*-
"""User defined Exceptions for Data Visualiation `
   Author: Mengfei Li (ml4713)
"""

__all__=['NotValidForm', 'NotEnoughInfo', 'EmptyError', 'NotValidInfoAmount', 'NotValidFeature', 'NotValidCategory', 'ReadFileError', 'NotValidSubcategory', 'NotIntegerError', 'NotValidRange_age', 'NotValidRange_hours']



class ReadFileError(Exception):
    """This exception will be raised if file path is not correct,
       either wrong dataset file path or non-exsit file
    """
    pass


class NotValidForm(Exception):
    """This exception will be raised if user's input for feature,category is not in the 
       format of ([feature1,feature2],category)
    """
    def __init__(self,rep):
        self.rep = rep
    def __str__(self):
        return "{} is not a valid input. Correct input should in the format of ([a,b],c)".format(self.rep)


class EmptyError(Exception):
    """This exception will be raised if user entered informaion is not enough
       for analysis.
    """
    pass
 
        
class NotValidFeature(Exception):
    """This exception will be raised if feature is not valid, either doesn't exsit or
       should in a category set
    """
    def __init__(self,feature):
         self.feature = feature
    def __str__(self):
         return "{} is not a valid feature in this program".format(self.feature)
         
class NotValidCategory(Exception):
    """This exception will be raised if category is not valid, either doesn't exsit or
       should in a feature set
    """
    def __init__(self,c):
        self.c = c
    def __str__(self):
        return "{} is not a valid category in this program".format(self.c)
 
 
class NotValidSubcategory(Exception):
    """This exception will be raised if user doesn't enter >50K or <=50K
       for analysis
    """
    def __init__(self,subcat):
        self.subcat = subcat
    def __str__(self):
        return "{} is not a valid subcategory! please enter either >50K or <=50K".format(self.subcat)


class NotIntegerError(Exception):
    """This exception will be raised if the user's information for age
       and hours is not an integer
    """
    pass
 
class NotValidRange_age(Exception):
    """This exception will be raised if user's age is not in the range of
       (0,100]
    """
    pass


class NotValidRange_hours(Exception):
    """This exception will be raised if user's working hours is not in the
       range of (0,100]
    """
    pass


class NotEnoughInfo(Exception):
    """This exception will be raised if user's info is not sufficient
    """
    pass


class NotValidInfoAmount(Exception):
    """This exception will be raised if user's input for feature_category class incorrect amount of information
    """
    pass
