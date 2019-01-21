# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21, 2019

File: Text Analysis

In 1949, Dr. RUdolf Flesch published The Art of Readable Writing, in which he proposed a measure of text readability known as the FLesh Index. This index is based on the average number of syllables per word and the average number of words per sentence in a piece of text. Index scores usually range from 0 to 100, and they indicate readable prose for the folling grade levels:
	
Flesch Index  	 	 	 	Grade Level of readability 
0–30 	 	 	 	 	 	College 
50–60  	 	 	 	 	 	High School 
90–100  	 	 	 	 	Fourth Grade

In this case study, we develop a program that computes the Flesh Index for a text file.

@author: Byen23
"""

# Request 
"""Write a program that computes the Flesch Index and grade level for text stored in a text file."""

# Analysis 
"""The input to thsi program is the name of a text file. The outputs are teh number of sentences, words, and syllables in the file, as well as the files's Flesh Index and Grade evel Equivalent.

During Analysis, we consult experts in domain to learn any information that might be relevant in solving the problem. For our problem, this information includes the definition of a sentence, word, and syllable. For the purpose of this program, these terms are defined at Table 4-7."""

"""
Word 	 	 	Any sequence of non-whitespace characters.

Sentence 	 	Any sequence of words ending in a period, question  	 	 	 	 	mark, exclamation point, colon, or semicolon.

Syllable 	 	Any word of three characters or less; or any vowl(a,  	 	 	  	e, i, o, u) or pair of consecutive vowels, except for  	 	  	 	a final -es, -ed, or -e that is not -le.

Note that the definition of word and sentence are approximations. SOme words, such as doubles or kettles, end in -es but will be counted as having one syllable, and an ellipsis(...) will be counted as three syllables.

Flesch's formula to calculate the index F is the following:
	
	F = 206.835 - 1.015 x (words / sentences) - 84.6 x (syllables  	 	  	 	 	  	  	 	 	  	 	 	 	 	 words)
	
The Flesh-Kincaid Grade Level Formula is used to compute the Equivalent Grade Level G:
	
	G = 0.39 x (words/sentences)+ 11.8 x (syllables/words) - 15.59
"""

# Design 
"""This program will perform the following tasks:
	
	1. Recieve the filename from the user, open the file for input,  	 	   the text.
	2. Count the sentences in the text.
	3. Count the words in the text.
	4. Count the syllables in the text.
	5. Compute the Flesch Index.
	6. Compute the Grade Level Equivalent.
	7. Print these two values with the appropriate labels, as well as   	   the counts from tast 2-4.
	
	The first and last task require no desig. Let's assume that the text is input as a single string from teh file and is then processed in tasks 2-4. These three tasks can be designed as coe segments that use the input string and produce an integer value. Task 5, computing the FLesch Index, uses the three integer results of tasks 2-4 to compute the FLesch Index. Lastly, task 6 is code segment that uses the same integers and computes the Grade Level Equivalent. The five tasks are listed in Tables 4-8, where text is a variable that refers the string read from the file.
	
	All the real work is done in the tasks that count the items:
		
		 Add the number of characters in text that end the sentences. 	 	 These characters were specified in analysis, and the string  	 	 method count is used to count them in the algorithm.
	
		 Split text into a list of words and determine the text  	 	  	 	 length.
		 
		 Count the syllables in each word in text."""
		 
		 
"""
--------------------------------------------------------------------
|           Task 	 	 	|             What it does             |
--------------------------------------------------------------------
--------------------------------------------------------------------
Count the sentences         | Counts the number of sentences in text.	
---------------------------------------------------------------------
Count the words 	 	 	| Counts the number of words in text.
---------------------------------------------------------------------   
Count the syllables 	 	| Counts the number of syllables in text.
---------------------------------------------------------------------
Compute the Flesch Index 	| Computes the Flesch Index for the given  	 	 	 	  	 	 	| numbers of sentences, words, and                         	 	 	 	 	 	 	| syllables.
---------------------------------------------------------------------
Compute the grade level     | Computes the Grade Level Equivalent for  	 	 	 	 	 	 	| the given numbers of sentences, words,  	 	  	 	 	 	 	| and syllables.
---------------------------------------------------------------------
"""


# Table 4-8 - The tasks defined in the text analysis program.

"""The last task is the most complex. For each word in the text, we must count the syllables in that word. From analysis, we know that each distinct vowel counts as a syllable, unless it is in the ending -ed, -es, or -e (but not -le). For now, we ignore the possibility of consecutive vowels."""

# Implementation (Coding)

"""The main tasks are marked off in the program code with a blank line and a comment."""

"""
Computes and displays the FLesch Index and the Grade Level Equivalent for the readability of a text file.
"""
# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

# Count the sentences 
sentences = text.count('.') + text.count('?') + \
		    text.count(':') + text.count(';') + \
			text.count('!')
			
# Count the words
words = len(text.split())

# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"

for word in text.spit():
	for vowel in vowels:
		syllables += word.count(vowel)
	for ending in ['es', 'ed', 'e']:
		if word.endswith(ending):
			syllables -= 1
		if word.endswith('le'):
			syllables += 1
			
# Compute the FLesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
	    84.6 * (syllables / words)

level = round(0.38 * (words / sentences) + 11.8 * \
			  (syllables / words) - 15.59)

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")







