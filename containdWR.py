import sys
import re
from substring import *

from itertools import combinations
from collections import defaultdict


if len(sys.argv) < 2: #check for whether input specified or not
    print "No jumbled word specified.Please enter a jumbled word."
    sys.exit(0)

input_string = sys.argv[1]
uni_input = unicode(input_string,'utf8')
#output_file = sys.argv[2]
#word_depth = int(sys.argv[3])
"""
use:
anagram8 thisisstringtoanagram outputfile depth
"""

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
    


for word in words1:
    uniWord = word.decode('utf8')
    words.append(uniWord)
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


def getPossibleWords(uni_input, words):
    sentanceLength = len(uni_input)
    
    # possible sentances part
    # main function
    letterWords = []
    for word in words:
        if hasAllLetters(word,uni_input):
            letterWords.append(word)
    possibleWords = []
    for word in letterWords:
        if notToManyRepeats(word, uni_input):
            possibleWords.append(word)

    return possibleWords


possibleWords = getPossibleWords(uni_input, words)

"""
the loop
"""
count = 0
input_string = unicode(uni_input)
sentance = ""

while True:


    for x in range(len(possibleWords)):
        print str(x) + " " + possibleWords[x]

    
    print "#####################"
    print sentance
    print "#####################"
    numb = int(raw_input("choose a word: \n"))

    

    chooseWord = possibleWords[numb]
    # next is to aquire a new possible words, and possibly
    # a new uni input ...
    sentance = sentance + " " + chooseWord


    for char in chooseWord:
        input_string = input_string[0:input_string.index(char)] + input_string[input_string.index(char)+1: len(input_string)]
    #st[0:st.index('f')] + st[st.index('f')+1:len(st)]

    print "#############################################################################"
    print input_string
    print "#############################################################################"
    
    possibleWords = getPossibleWords(input_string, words)




"""

possibleWords2 = getPossibleWords(input_string, possibleWords)

for x in range(len(possibleWords2)):
    print str(x) + " " + possibleWords2[x]
"""
"""
# baisic functionality is ready

now it just needs to be looped and cleaned
and the sentance being made needs to be kept track of,

-----<)

in the future the option of finding the anagram setances
of the remainder to a word depth x
should also be offered

in that case we need a functional version of the
word depth loops fom anagram8-3 ..


"""
