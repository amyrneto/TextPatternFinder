def getDataLines(filename):
	dataLines = []
	with open(filename, "r") as f:
	    datafile = f.readlines()
	lineNr = 0
	for lines in datafile:
		if "\\\\" in lines:
			dataLines.append(lines)
	return dataLines

def getTargetKeyword(dataLine):
	wordList = dataLine.split(" ")
	for w in wordList:
		if "\\\\" in w:
			print(w)

dataLines = getDataLines("annotated.txt")
for dl in dataLines:
	getTargetKeyword(dl)