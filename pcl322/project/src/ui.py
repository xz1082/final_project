#Author: Po-Chih Lin

from utility import *
from exception import *

"""
Show welcome message
Input: none
Output: welcome message (written to stdout)
Return: none
"""
def welcome():
	print "\n>> WELCOME TO PROJECT NYC JOBS ANALYSIS"


"""
Show goodbye message
Input: none
Output: goodbye message (written to stdout)
Return: none
"""
def goodbye():
	print "\n>> THANK YOU"


"""
Let user to choose which function to use
Input: function flag (specified by user from stdin)
Return: function flag chosen by user
"""
def choosingFunctions():

	while True:
		try:
			#Get the function flag from user
			flag = raw_input("\n>> ENTER 1 FOR SALARY PREDICTION,\n>>       2 FOR KEYTERM LEXICON GENERATION\n>>       3 FOR GRAPHICAL ANALYSIS\n>>       OTHER ELSE TO QUIT\n")
			break
		#If KeyboardInterrupt, terminate the program
		except KeyboardInterrupt:
			terminate()

	return flag


"""
Ask the user if he/she wants to restart the function again
Input: restart flag (specified by user from stdin)
Return: true or false
"""
def restart():
	
	while True:
		try:
			#Get the restart flag from the user
			flag = raw_input("\n>> Start again? (enter 1 if yes, 0 if no)\n")
			#Check the flag is binary or not
			valid_binary(flag)
			break
		#If it's not binary, exception will be raised
		except BinaryErr as err:
			print err
	
		#If KeyboardInterrupt, terminate the program
		except KeyboardInterrupt:
			terminate()
	
	#Return true when flag == 1, otherwise false
	if flag == "1":
		return True
	else:
		return False

"""
Get the setting of lexicon from user
Input: the number of topics and lexicon file path (specified by user from stdin)
Return: the number of topics and lexicon file path
"""
def getLexiconSetting():
	while True:
		try:
			#Get the number of topic from user
			n_topic = raw_input("\n>> Please specify the number of topics\n")
			#Check the input is an integer
			valid_integer(n_topic)
			break
		#Not an integer
		except IntegerErr as err:
			print err

		#If KeyboardInterrupt, terminate the program
                except KeyboardInterrupt:
                        terminate()

	while True:
		try:
			#Get the lexicon file path
			output_file = raw_input("\n>> Please specify the output file path\n")
			#Check the input is a string
			valid_string(output_file)
			#Check the file path is correct
			fp = open(output_file, "w")
			fp.close()
			break
		#IO Error
        	except IOError as err:
                	print err.errno
                	print err.strerror

		#Not a string
		except StringErr as err:
			print err

		#If KeyboardInterrupt, terminate the program
                except KeyboardInterrupt:
                        terminate()

	return int(n_topic), output_file



"""
Get the lexicon file from user
If user skips to specify one, use the default lex file
Input: the default lexicon file path and the lexicon file path specified by user from stdin
Return: lexicon file path
"""		
def getLexicon(lex_file_default):
	while True:
		try:
			#Get the keyterm file path from user
			lex_file = raw_input("\nPlease specify the path of the keyterm lexicon (press enter to skip if using the default file)\n")
			#Check if the file path entered or not
			valid_string(lex_file)
			#Check if the file can be opened
			fp = open(lex_file, "r")
			fp.close()
			break
		#User skipped entering the file path, use the default file
		except StringErr:
			return lex_file_default
		#IO Error
		except IOError as err:
			print err.errno
			print err.strerror

		#If KeyboardInterrupt, terminate the program
		except KeyboardInterrupt:
			terminate()
	
	return lex_file


"""
Get the information about the data to be shown on plot
Input: feature of jobs, target value, and the number of top items (specified by user from stdin)
Return: valid feature, target, and number of items
"""
def getAnalyTarget():
	targets = ("Salary", "# Of Positions")
	features = ("Agency", "Business Title", "Civil Service Title")

	while True:
		try:
			#Get the feature of jobs
			flag = raw_input("\n>> Please specify the data you are interested in\n\
>> Enter 1 for \"%s\"\n\
>>       2 for \"%s\"\n\
>>       3 for \"%s\"\n"%features)

			#Check if it is a valid code
			valid_code(flag, ["1", "2", "3"])
			#Convert the code to feature name
			feature = features[int(flag)-1]
			break
		#Invalid code entered
		except CodeErr as err:
			print err

                #If KeyboardInterrupt, terminate the program
                except KeyboardInterrupt:
                        terminate()

	while True:
		try:
			#Get the target value of the feature
			flag = raw_input("\n>> Please specify the target value\n\
>> Enter 1 for \"Averaged %s\"\n\
>>       2 for \"Total %s\"\n"%targets)

			#Check if it is a valid code
			valid_code(flag, ["1", "2"])
			#Convert the code to target name
			target = targets[int(flag)-1]
			break
		#Invalid code entered
		except CodeErr as err:
			print err

		#If KeyboardInterrupt, terminate the program
		except KeyboardInterrupt:
			terminate()

	while True:
		#Set the max number of items 
		max_len = 30
		try:
			#Get the number of top items
			flag = raw_input("\nPlease specify the number of \
top items to be shown (up to %d)\n"%(max_len))
			#Check if it is valid
			valid_integer(flag)
			#Check the value of the number
			k = int(flag)
			if k > max_len:
				k = max_len
			break
		#Not a valid integer
		except IntegerErr as err:
			print err

		#If KeyboardInterrupt, terminate the program
		except KeyboardInterrupt:
			terminate()

	return feature, target, k
	

"""
Get the resume of user
Input: the resume (described by user in stdin)
Output: the resume in a long string

"""
def getResume():

	while True:
		try:
			#Get the user's resume from stdin
			resume = raw_input("\n>> Please enter your resume (which includes the keyterms of your skills)\n")			
			resume = resume.decode("ascii")
			valid_string(resume)
			break
		#Input format Error
		except StringErr as err:
			print err

		#The input is in undefined coding
		except UnicodeDecodeError as err:
			print err

		#If KeyboardInterrupt, terminate the program
		except KeyboardInterrupt:
			terminate()

	return resume


"""
Show the retrieval results
Input: retrieved jobs, sklls, and the predicted salary interval
Output: the information of the results (shown on stdin)
Return: none
"""
def showJobMatchingResults(jobs, skills, salary_interval):

	print "\n==================== Results ===================="
	print "\nThe top %d matched jobs are: "%(len(jobs)),
	print "".join(str("\n- "+s+"") for s in jobs)
	print "\nThe top %d keyterms in the jobs are" % (len(skills)),
	print "".join(str("\n- "+s) for s in skills)
	print "\nYour predicted salary interval is"
	print salary_interval


