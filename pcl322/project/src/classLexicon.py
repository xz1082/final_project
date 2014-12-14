#Author: Po-Chih Lin

"""
The class of lexicon
self.data	:all the keyterms in list
self.mapping	:the dicionary for mapping keyterm to id
self.invMapping	:the dictionary for mapping id to keyterm
self.size	:the total number of keyterm in the lexicon
"""
class lexicon:

	"""
	Initialize with the lexicon file path
	Input: the file path
	"""
	def __init__(self, filename):
		#Read the lexicon file
		fp = open(filename, "r")

		i = 0
		self.mapping = {}
		self.invMapping = {}
		self.data = []
		while True:
			line = fp.readline().rstrip("\n")
			if not line:
				break
			#Initialize all the data in lexicon object
			if line not in self.data:
				self.mapping[line] = i
				self.invMapping[i] = line

				i = i + 1
			self.data.append(line)
		fp.close()
		self.size = i

		#Save the attributes of the lexicon
                self.numWordsInTopics = 10
                self.numTopics = int(float(len(self.data))/self.numWordsInTopics)

	"""
	Print all the keyterms discovered on stdin
	Input: none
	Output: the keyterm in all topics (shown on stdout)
	"""
	def show_keyterms(self):
		for i in range(self.numTopics):
			print "Topic %d:"%(i),

			for j in range(self.numWordsInTopics):
				comma = ","
				if j == self.numWordsInTopics-1:
					comma = ""
				print self.data[i*self.numWordsInTopics+j] + comma,
			print ""


