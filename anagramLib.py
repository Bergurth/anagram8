import sys
import re
from substring import *

from itertools import combinations
from collections import defaultdict


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
