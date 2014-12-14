#Author: Yitong Wang

#Invalid integer
class IntegerErr(Exception):
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return self.message

#Invalid string format
class StringErr(Exception):
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return self.message

#No job that matches the given resume
class NoJobMatchedErr(Exception):	
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return self.message

#Invalid binary code
class BinaryErr(Exception):	
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return self.message

#The requsted file does not exist
class FileNotExistedErr(Exception):	
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return self.message

#Invalid code entered by user
class CodeErr(Exception):	
	def __init__(self, message):
		self.message = message
	def __str__(self):
		return self.message
