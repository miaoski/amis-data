# -*- coding: utf8 -*-
# 印出 p-046.txt 鄉民OCR格式中每個單字在哪一頁

import sys
import re

def extractFromFile(curpage, lx):
    re1 = re.compile(r"(^[a-z':]+) *-")
    re2 = re.compile(r"(^[a-z':]+) */")
    for l in lx:
        grp = re1.search(l) or re2.search(l)
        if grp:
            print "%s\t%d" % (grp.group(1), curpage)


if __name__ == '__main__':
    curpage = int(re.search('p-([0-9]+).txt', sys.argv[1]).group(1))
    with open(sys.argv[1], 'r') as f:
        extractFromFile(curpage, f.readlines())
