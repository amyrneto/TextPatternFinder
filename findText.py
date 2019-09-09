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
	temp=""
	kwList = []
	annotationBegin=False
	for w in wordList:
		w=w.strip(".,;:!? ")
		#print ("w:"+w)
		if (~("\\\\" in w)) & (annotationBegin == True):
			temp += " " + w

		if ("\\\\" in w[0:4]) & (annotationBegin == False):
			annotationBegin = True
			w = w.lstrip('\\')
			if ("\\\\" in w[-4:]):
				annotationBegin = False
				w = w.rstrip('\\')
				temp = w
				kwList.append(temp)
			else:
				temp = w


		if ("\\\\" in w[-4:]) & (annotationBegin == True):
			annotationBegin = False
			w = w.rstrip('\\')
			temp += " " + w
			kwList.append(temp)
	return kwList



dataLines = getDataLines("annotated.txt")
keyWords = []
for dl in dataLines:
	keyWords.append(getTargetKeyword(dl))

# Lista de strings com as anotações criadas.
for k in keyWords:
	print (k)

# @todo: fazer uma lista completa de palavras
# @todo: fazer uma lista com os indices de anotação (palavra inicial e palavra final de cada anotação)
# @todo: analisar a lista completa de palavras ao redor das anotações
# @todo: criar uma lista das palavras que ocorrem com maior frequencia antes e depois das anotações.
# @todo: criar modelos de linguagem (grafos) que iniciam nas palavras mais frequentes e vão até o início da anotação.

