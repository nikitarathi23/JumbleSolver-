from __future__ import division 


class WordJumbleSolver():
	def __init__(self):
		self.dictionary = {}

   #Builds a dictionary from the existing dictionary with the sorted word as the key and a list of words as the value.

	def builddictionary(self, infile):
		for line in infile:
			if line:
				line.strip()
				for word in line.split():
					word = word.lower()
					sorted_word = ''.join(sorted(word))
					self.dictionary.setdefault(sorted_word,[]).append(word)

    
    #Returns all substrings of a string.
   
	def substr(self, s, minlen):
   		if len(s) < minlen:
 			return []
		return [s[i:i+minlen] for i in range(len(s) - minlen + 1)] + self.substr(s, minlen + 1)
					


if __name__ == "__main__":
	var = WordJumbleSolver()
	infile = open('dictionary.txt','r')
	var.builddictionary(infile)
	jumble= raw_input("Enter a jumble to be solved ")   
	list_strings = var.substr(jumble.lower(),1)
	output_strings = []

	#Sorts every substring that can be created by the given string alphabetically, searches the dictionary for any existing word.
	
	for word in list_strings:
		word = ''.join(sorted(word))
		if word in var.dictionary:
			for item in var.dictionary[word]:
				output_strings.append(item)

	output_strings = list(set(output_strings))
	output_strings.sort(key = len)

	if output_strings:
		print "Words found are:\n" + ", ".join(output_strings)
	else:
		print "No word found"
			

	
	
	



		