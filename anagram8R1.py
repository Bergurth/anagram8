import sys
import re
from substring import *

from itertools import combinations
from collections import defaultdict

# library, 3 functions
# words is now a list with unicode objects from the dictionary

# the following functino checks if the input string contains all the letters of whe candidate
def hasAllLetters(candidateWord, inputString):
    for char in candidateWord:
        if char not in inputString:
            return False

    return True


#identifies repeat letters
def repeatLetters(word):
    repeats = {}
    for char in word:
        if ord(char) in repeats:
            repeats[ord(char)] += 1 
        else:
            repeats[ord(char)] = 1
        
    return repeats

def notToManyRepeats(candidateWord,inputString):
    input_repeats = repeatLetters(inputString)
    word_repeats = repeatLetters(candidateWord)
    for key in word_repeats:
        if word_repeats[key] > input_repeats[key]:
            return False
    return True








if len(sys.argv) < 2: #check for whether input specified or not
    print "No jumbled word specified.Please enter a jumbled word."
    sys.exit(0)

input_string = sys.argv[1]
uni_input = unicode(input_string,'utf8')
#output_file = sys.argv[2]


# dictionary part
try:
    inputFile = open("./islenska2-20081208.txt","r")
except Exception, e:
    print "Exception while reading the dictionary file . Following are the details of the exception :\n\r"+ str(e)
    sys.exit(0)
    #words = inputFile.read().strip().split("\r\n") #This would be faster but cannot use as it input file format could vary.
fileContents = words = inputFile.read().strip() #Striping whitespaces
    
wordsOrig = re.split("[\s\n\r]+",fileContents) #Splitting the file into word tokes based on either spaces/new line/carriage return

words1 = []
words = []
for word in wordsOrig:
    words1.append( word.decode('iso-8859-1').encode('utf-8'))
    
sentanceLength = len(uni_input)


for word in words1:
    uniWord = word.decode('utf8')
    words.append(uniWord)

possibleWords = []
wordLengths = {}
lengthWords = defaultdict(list)
i = 0
for word in words:
    if hasAllLetters(word, uni_input) and notToManyRepeats(word, uni_input):
        possibleWords.append(word)
        wordLengths[i]=len(word)
        lengthWords[len(word)].append(word)
        i += 1

# for each word length, maybe sort into anagram classes

# first try at recursive function
def recFunc1(wordlist, stringRemainder, stringSoFar):
    if len(stringSoFar) == sentanceLength:
        print stringSoFar
    elif len(stringSoFar) > sentanceLength:
        pass 
    else:
        wrd = wordlist.pop()
        if hasAllLetters(wrd, stringRemainder):
            if notToManyRepeats(wrd, stringRemainder):
                stringSoFar+=" " + wrd
                for char1 in wrd:
                    for char2 in stringRemainder:
                        if char1 == char2:
                            stringRemainder.replace(char2, "")
        for word in wordlist:
            
            recFunc1(wordlist, stringRemainder, stringSoFar)
        #return stringSoFar

#recFunc1(possibleWords, uni_input, "")
sentances = []
def recFunc2(wordlist, stringRemainder, sentance):
    print stringRemainder
    print type(sentance)
    sentanceString = ''.join(sentance)
    print type(sentance)
    print type(sentanceLength)
    print type(len(sentanceString))
    if len(sentanceString) == sentanceLength:
        sentances.append(' '.join(sentance))
        return
    if len(sentanceString) > sentanceLength:
        return
    wordlist2 = []
    for word in wordlist:
        if hasAllLetters(word, stringRemainder) and notToManyRepeats(word, stringRemainder):
            wordlist2.append(word)
    if len(wordlist2) <= 1:
        return
    for x in range(len(wordlist2)):
        wrd = wordlist2[x]
        recFunc2(listRemove(wordlist2,x),stringSubtract(wrd, stringRemainder),appendToList(sentance,wrd))
        
def appendToList(l, x):
    l.append(x)
    return l

def listRemove(l,x):
    l.pop(x)
    return l

def stringSubtract(string1, string2):
    for char1 in string1:
        for char2 in string2:
            if char1 == char2:
                string2.replace(char2, "")
    return string2
        
print sentanceLength

recFunc2(possibleWords, uni_input, [""])
for x in sentances:
    print x
