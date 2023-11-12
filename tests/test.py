"""
Usage:
test.py <a>

Options:
 <a>
"""
import re
from docopt import docopt

def test1(a="yes"):
    print(test1.__defaults__)
    print(a)

a=None
test1(a=a)


#args = docopt(__doc__)
#a = float(args['<a>'])
#
#if str(a).split('.')[0] != '0':
#    print(str(a).split('.'))
#    print('a > 1')
#else :
#    print(re.match(r'0*'))





