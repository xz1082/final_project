'''
Created on Dec 13, 2014

@author: Minzi Ji
'''
import unittest
from unixvis import *
from dtclean import *



class Test_UnixVisualizer(unittest.TestCase):
    '''
    provided tests for functions in UnixVisualizer
    '''


    def setUp(self):
        begin = time.time()
        self.test_data_reader = DataReader()
        self.test_cleaner = DataCleaner(cleanCollisionData)
        test_raw_data = self.test_data_reader.safeReadCsvLocal('data/NYPD_Motor_Vehicle_Collisions.csv')
        self.test_cleaner.clean(test_raw_data)
        self.test_object = UnixVisualizer(test_raw_data)
        end = time.time()
        print end-begin


    def tearDown(self):
        self.test_data_reader = None
        self.test_object = None
        self.test_cleaner = None

 
    def test_unixvis_vehicleTypes(self):
        self.test_object.unixvis_vehicleTypes('ggplot')
          
    def test_unixvis_top5Factors(self):
        self.test_object.unixvis_top5Factors('ggplot')
          
    def test_unixvis_regressionVehicleXFatalities(self):
        self.test_object.unixvis_regressionVehicleXFatalities('ggplot')
         
    def test_unixvis_collisonsAndFatalities(self):
        self.test_object.unixvis_collisonsAndFatalities()
        
    def test_unixvis_contributingFactors(self):
        self.test_object.unixvis_contributingFactors()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()