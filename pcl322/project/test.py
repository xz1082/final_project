#Author: Po-Chih Lin

import unittest
from src.utility import *
from src.lexFeature import *

"""
Test for the valid_interger() in src.utility
"""
class TestValidInteger(unittest.TestCase):

	def setUp(self):
		self.input1 = "0"
		self.input2 = "-99"
		self.input3 = "123abc456"
		self.input4 = "qqq"
		self.input5 = "0806449+"
		self.input6 = "100"

	#Test if the number is zero
	def test_zero(self):
		self.assertRaises(IntegerErr, valid_integer, self.input1)
	#Test if the number is less than zero
	def test_negative(self):
		self.assertRaises(IntegerErr, valid_integer, self.input2)
	#Test if number is in wrong format
	def test_invalid_format(self):
		self.assertRaises(IntegerErr, valid_integer, self.input3)
		self.assertRaises(IntegerErr, valid_integer, self.input4)
		self.assertRaises(IntegerErr, valid_integer, self.input5)
	#Test if the number is valid
	def test_correct_format(self):
		self.assertEqual(valid_integer(self.input6),True)	

"""
Test for valid_string() in src.utility
"""
class TestValidString(unittest.TestCase):

	def setUp(self):
		self.input1 = "abcdefg"
		self.input2 = ""
	#Test if the string is empty
	def test_enter(self):
		self.assertRaises(StringErr, valid_string, self.input2)
	#Test if the string is valid
	def test_correct_format(self):
		self.assertEqual(valid_string(self.input1), True)
"""
Test for valid_code() in src.utility
"""
class TestValidCode(unittest.TestCase):
	
	def setUp(self):
		self.codes = ["a", "b", "c"]
		self.input1 = "b"
		self.input2 = "z"
	#Test if the code is not in the code pool
	def test_not_in_codes(self):
		self.assertRaises(CodeErr, valid_code, self.input2, self.codes)
	#Test if the code is valid
	def test_correct_format(self):
		self.assertEqual(valid_code(self.input1, self.codes), True)

"""
Test for the valid_binary() in src.utility 
"""
class TestValidBinary(unittest.TestCase):

        def setUp(self):
                self.input1 = "xyz"
                self.input2 = "-1"
		self.input3 = "0"
		self.input4 = "1"
	#Test if the input is a string
	def test_a_string(self):
		self.assertRaises(BinaryErr, valid_binary, self.input1)
	#Test if the input is negative
	def test_negative(self):
		self.assertRaises(BinaryErr, valid_binary, self.input2)
	#Test if the input is valid
	def test_correct_format(self):
		 self.assertEqual(valid_binary(self.input3), True)
		 self.assertEqual(valid_binary(self.input4), True)
"""
Test for the tokenize() in src.lexFeature
"""
class TestTokenize(unittest.TestCase):
	def setUp(self):
		self.input0 = [u"abcde"]
		self.input1 = [u"", u"ab", u"cde", u""]
		self.input2 = "<p>AB<p>CDE</p>"
		self.input3 = "<u>AB\\nCDE</u>"
		self.input4 = "<u>AB\\\nCDE</u>"
		self.input5 = "(AB)CDE\""
		self.input6 = "ABCDE"

	#Test if the symbols are correctly removed
	def test_moved(self):
		self.assertEqual(tokenize(self.input2), self.input1)
		self.assertEqual(tokenize(self.input3), self.input1)
		self.assertEqual(tokenize(self.input4), self.input1)
		self.assertEqual(tokenize(self.input5), self.input1)
	#Test if these is no symbol in the string
	def test_no_symbol(self):
		self.assertEqual(tokenize(self.input6), self.input0)


if __name__ == "__main__":
	unittest.main()



