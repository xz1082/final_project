'''
Created on Dec 3, 2014

@author: Minzi Ji
'''
import unittest
from collisionvis import *
from ioprocess import *
import time
from dtclean import *


class TestCollisionVisualizer(unittest.TestCase):
    '''
    test class for functions in TestCollisionVisualizer
    
    In class tests for following functions are provided:
        1) _getVehicleTypes
        2) VehicleTypes
        3) regressionPlot
        4) getMaxFatalities
        5) _regression
        6) top5Factors
        7) collisionsByDateRange
        8) boroughFatalities
    '''

    def setUp(self):
        begin = time.time()
        self.test_data_reader = DataReader()
        self.test_cleaner = DataCleaner(cleanCollisionData)
        test_raw_data = self.test_data_reader.safeReadCsvLocal('../data/NYPD_Motor_Vehicle_Collisions.csv')
        self.test_cleaner.clean(test_raw_data)
        self.test_object = CollisionVisualizer(test_raw_data)
        end = time.time()
        print end-begin

    def tearDown(self):
        pass

    def test_getVehicleTypes(self):
        print self.test_object._getVehicleTypes()
          
    def test_VehicleTypes(self):
        print self.test_object._data
        self.test_object.VehicleTypes('8/10/2013', '2/8/2014')
          
    def test_regressionPlot(self):
        self.test_object.regressionPlot()
          
    def test_getMaxFatalities(self):
        print self.test_object.getMaxFatalities('8/10/2012', '7/1/2014')
           
    def test_regression(self):
        print self.test_object.regression()
           
    def test_top5Factors(self):
        print self.test_object.top5Factors('8/10/2012', '7/1/2014')
        
    def test_collisionsByDateRange(self):
        print self.test_object.collisionsByDateRange('8/10/2012', '8/25/2012')
        
    def test_boroughFatalities(self):
        print self.test_object.boroughFatalities('8/10/2012','7/1/2014')
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()