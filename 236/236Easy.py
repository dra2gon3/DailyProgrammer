import random

letterList = ['O','I','S','Z','L','J','T']

def tetrominiPieces():
	tetrominiString = ""
	for x in range(0, 50):
		tetrominiString += random.choice(letterList)
	if len(tetrominiString) > 2 and tetrominiString[-1] == tetrominiString[-2] and tetrominiString[-1] == tetrominiString[-3]:
		tetrominiString.pop()
		x -= 1
	print (tetrominiString)
tetrominiPieces()
