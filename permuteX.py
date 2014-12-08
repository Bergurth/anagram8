from permute import Permute
import sys

if len(sys.argv) < 2: #check for whether input specified or not
    print "No jumbled word specified.Please enter a jumbled word."
    sys.exit(0)



jumble = unicode(sys.argv[1], 'utf8')

permuteArray = Permute(jumble)

for x in permuteArray:
    print x
