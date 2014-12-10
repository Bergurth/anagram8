import sys
import re
from substring import *



if len(sys.argv) < 2: #check for whether input specified or not
    print "No jumbled word specified.Please enter a jumbled word."
    sys.exit(0)

input_string = sys.argv[1]
uni_input = unicode(input_string,'utf8')

# dictionary part
try:
    inputFile = open("islenska2-20081208.txt","r")
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
    word_repeats = repeatLetters(word)
    for key in word_repeats:
        if word_repeats[key] > input_repeats[key]:
            return False
    return True
    




# main function
letterWords = []
for word in words:
    if hasAllLetters(word,uni_input):
        letterWords.append(word)


for word in letterWords:
    if notToManyRepeats(word, uni_input):
        print word

    
