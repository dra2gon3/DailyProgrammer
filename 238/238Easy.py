import sys
import random

consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']

fileName, newWord = sys.argv
def makingWord(newWord):
	s = ""
	for i in newWord:
		if i == 'c':
			s += str(random.choice(consonants))
		if i == 'v':
			s += str(random.choice(vowels))
		if i == 'C':
			s += str(random.choice(consonants)).upper()
		if i == 'V':
			s += str(random.choice(vowels)).upper()
	print (s)
	
def checkInput(newWord):
	length = 0
	fullLength = len(newWord)
	while(True):
		for i in newWord:
			if i == 'c' or i == 'v' or i == 'C' or i == 'V':
				length += 1
		if fullLength == length:
			makingWord(newWord)
			exit(0)
		else:
			newWord = input("Input: ")
			length = 0
			fullLength = len(newWord)
checkInput(newWord)