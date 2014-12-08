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
output_file = sys.argv[2]


# dictionary part
try:
    inputFile = open("/home/bergur/Desktop/pythonStuff/islenska2-20081208.txt","r")
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

sentanceLength = len(uni_input)
    
# possible sentances part







# main function
letterWords = []
for word in words:
    if hasAllLetters(word,uni_input):
        letterWords.append(word)

possibleWords = []
wordLengths = {}
lengthWords = defaultdict(list)
i = 0
for word in letterWords:
    if notToManyRepeats(word, uni_input):
        possibleWords.append(word)
        wordLengths[i]=len(word)
        lengthWords[len(word)].append(word)
        i += 1
        #print word

# wordlengths is a dictionary with index the same place the word is and the length of thw word as value
# lengthWords is a dictionary of lists with the key being the length of words and the value a list of
#  words of that length
"""
for key in wordLengths:
    print wordLengths[key]
"""


combos2 = []
#pair for pair in itertools.combinations(li,2) if sum(pair) == 10
for var in combinations(wordLengths, 2):
    if var[0] + var[1] == sentanceLength:
        combos2.append(var)

combos3 = []
#pair for pair in itertools.combinations(li,2) if sum(pair) == 10
for var in combinations(wordLengths, 3):
    if var[0] + var[1] + var[2] == sentanceLength:
        combos3.append(var)

combos4 = []
#pair for pair in itertools.combinations(li,2) if sum(pair) == 10
for var in combinations(wordLengths, 4):
    if var[0] + var[1] + var[2] + var[3] == sentanceLength:
        combos4.append(var)

combos5 = []
#pair for pair in itertools.combinations(li,2) if sum(pair) == 10
for var in combinations(wordLengths, 5):
    if var[0] + var[1] + var[2] + var[3] + var[4] == sentanceLength:
        combos5.append(var)




#print lengthWords

#print sentanceLength
print combos2

print "###################################################################"
print uni_input

twoWordCombos = []
for combo in combos2:
    #print combo[0]
    #print combo[1]
    for word1 in lengthWords[combo[0]]:
        for word2 in lengthWords[combo[1]]:
            longWord = word1 + word2
            #print longWord
            if notToManyRepeats(longWord, uni_input):
                twoWordCombos.append(longWord)


threeWordCombos = []
for combo in combos3:
    for word1 in lengthWords[combo[0]]:
        for word2 in lengthWords[combo[1]]:
            for word3 in lengthWords[combo[2]]:
                longWord = word1 + word2 + word3
                #print longWord
                if notToManyRepeats(longWord, uni_input):
                    threeWordCombos.append(longWord)


fourWordCombos = []
for combo in combos4:
    for word1 in lengthWords[combo[0]]:
        for word2 in lengthWords[combo[1]]:
            for word3 in lengthWords[combo[2]]:
                for word4 in lengthWords[combo[3]]:
                    longWord = word1 + word2 + word3 + word4
                    if notToManyRepeats(longWord, uni_input):
                        fourWordCombos.append(longWord)

fiveWordCombos = []
for combo in combos5:
    for word1 in lengthWords[combo[0]]:
        for word2 in lengthWords[combo[1]]:
            for word3 in lengthWords[combo[2]]:
                for word4 in lengthWords[combo[3]]:
                    for word5 in lengthWords[combo[4]]:
                        longWord = word1 + word2 + word3 + word4
                        if notToManyRepeats(longWord, uni_input):
                            fourWordCombos.append(longWord)



f = open(output_file, 'w')


f.write("two word combos -----------------------------------------------------2\n")
print "two word combos -----------------------------------------------------2"
for x in twoWordCombos:
    f.write(x.encode('utf8'))
    f.write('\n')
    print x

f.write("three word combos -----------------------------------------------------3\n")
print "three word combos ---------------------------------------------------3"
for x in threeWordCombos:
    f.write(x.encode('utf8'))
    f.write('\n')
    print x

f.write("four word combos -----------------------------------------------------4\n")
print "four word combos ----------------------------------------------------4"
for x in fourWordCombos:
    f.write(x.encode('utf8'))
    f.write('\n')
    print x


f.write("five word combos -----------------------------------------------------5\n")
print "five word combos ----------------------------------------------------5"
for x in fiveWordCombos:
    f.write(x.encode('utf8'))
    f.write('\n')
    print x

"""
print combos2
print combos3
print combos4
print combos5
"""
