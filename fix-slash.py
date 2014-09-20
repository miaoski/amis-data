# -*- coding: utf8 -*-
# Fix:
# word1 / word2. [some description]

import sys
import re

for line in sys.stdin:
    ln = line.rstrip()
    if ln.find('/') == -1:
        print ln
        continue
    x = re.match(r"^[A-Za-z':]+( ?/ ?[A-Za-z':]+)+[. ]+", ln)
    if x is None:
        print ln
    else:
        try:
            (word, dsc) = ln.split('.', 1)
        except:
            print "Error:", ln
            raise
        wx = [w.strip() for w in word.split('/')]
        print wx[0]
        print "=>", ', '.join(wx[1:])
        if dsc != '':
            print dsc.strip()
