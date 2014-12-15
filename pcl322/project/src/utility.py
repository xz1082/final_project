#Author: Yitong Wang

from exception import *
import sys
import re
import numpy as np

"""
Terminate the program
Input: none
Return: none
"""
def terminate():
	print "\nProgram terminated"
	sys.exit(0)

"""
Check the code is valid
Input: a string and the set of codes
Output: True if valid, otherwise raising exception
"""
def valid_code(input, codes):
	if input not in codes:
		raise CodeErr("Invalid Code")
	return True


"""
Check the string is valid (can't be an empty string)
Input: a string
Output: True if valid, otherwise raising exception
"""
def valid_string(input):
	if re.match(r"^.+$", input) == None:
		raise StringErr("Invalid String")
	return True


"""
Check the code is binary
Input: a code of string
Output: True if valid, otherwise raising exception
"""
def valid_binary(input):
	if re.match(r"^[01]$", input) == None:
		raise BinaryErr("Invalid Code")
	return True


"""
Check the input is in the valid integer format
Input: a string
Output: True if valid, otherwise raising exception
"""
def valid_integer(input):
	if re.match(r"^\d+$", input) == None:
		raise IntegerErr("Invalid Integer")
	if int(input) <= 0:
		raise IntegerErr("Number must be greater than zero")
	return True



