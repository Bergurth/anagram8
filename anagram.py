import sys
import re
from substring import *

##########################################################################
# Function    : filterWordsBasedOnLength
# Parameters  : jumbledWord(String) and dictionary reference word(String)
# Returns     : String
# Description : This function matches the two given string for 
#               their length and returns the word if the lenghts are same.
##########################################################################

def filterWordsBasedOnLength(jumbledWord,word):
    if len(jumbledWord) == len(word):
        return word


##########################################################################
# Function    : computeValuForEachWord
# Parameters  : filteredWord(String) and jumbledWord(String)
# Returns     : boolean
# Description : This computes the unicode value of each sting to filter out
#               the words and then if the value matches it then checks
#  whether the characters match if they do it return true else
#false
##########################################################################
   
def computeValuForEachWord(filteredWord,jumbledWord):
    filteredWordValue = 0
    jumbledWordValue = 0
    for character in filteredWord:
        filteredWordValue += ord(character)

    for char in jumbledWord:
        jumbledWordValue += ord(char)
    filteredWord = list(filteredWord)
    if filteredWordValue == jumbledWordValue:
        for w in jumbledWord:
            if w not in filteredWord:
                return False
            else:
                del filteredWord[filteredWord.index(w)] #For filtering out cases where value becomes same due to multi occurence of same char
        return True
    else:
        return False


