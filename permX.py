# -*- coding: utf-8 -*-
from permute import Permute
import sys

if len(sys.argv) < 2: #check for whether input specified or not
    print "No jumbled word specified.Please enter a jumbled word."
    sys.exit(0)


strn = sys.argv[1]
fileName = sys.argv[2]
#jumble = unicode(strn,'utf-8')
jumble = unicode(strn,'utf-8')

permuteArray = Permute(jumble)

f = open(fileName, 'w')

for x in permuteArray:
    f.write(x.encode('utf8'))
    f.write('\n')


f.close()
