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


# Now the idea is to form a list of word sets, all
# words within each set being anagramous with one another
