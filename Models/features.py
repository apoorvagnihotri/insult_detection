def giveNumBadWords(sentence, badWordList):
	counter = 0
	for word in sentence:
		if word in badWordList:
			counter += 1
	return counter

# assumption, badwords delimited by `\n`
def readBadWordFile(fileName):
	f = open(fileName, 'r')
	words = f.read().splitlines()
	return words

def hasYourMom(sentence):
    return i.lower().count("your mom")

def wordCount(sentence):
    return len(sentence.split())

def countUpper(sentence):
    return float(sum(1 for k in i if k.isupper()))/len(sentence)

def countExclaim(sentence):
    return float(sentence.count('!')/float(len(sentence)))

def countAtTheRate(sentence):
    return float(sentence.count('@')/float(len(sentence)))

def countPercent(sentence):
    return float(sentence.count('%')/float(len(sentence)))

def countLeftBracket(sentence):
    return float(sentence.count('(')/float(len(sentence)))

def countQuotes(sentence):
    return float(sentence.count('"')/float(len(sentence)))

def countStar(sentence):
    return float(sentence.count('*')/float(len(sentence)))

def countBackSlashes(sentence):
    return float(sentence.count('\\')/float(len(sentence)))

def countFrontSlash(sentence):
    return float(sentence.count('/')/float(len(sentence)))

def countYour(sentence):
    lst = ['your','Your','YOUR']
    for word in lst:
        s += sentence.count(word)
    return float(s)/len(sentence)

def countYou(sentence):
    lst = ['you','You','YOU']
    for word in lst:
        s += sentence.count(word)
    return float(s)/len(sentence)
