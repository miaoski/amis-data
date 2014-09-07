# -*- coding: utf8 -*-
# 印出 0.txt 格式中每個單字在哪一頁

import sys

def extractFromFile(lx):
    import re
    repage = re.compile(r'^# +p[.]([0-9]+)')
    curpage = 0
    GLOS = True
    NOT_GLOS = False
    sts = NOT_GLOS
    for l in lx:
        ls = l.strip()
        rp = repage.search(ls)
        if rp:
            curpage = int(rp.group(1))
            sts = GLOS
        elif sts == GLOS and len(ls) > 0 and \
                ls.find('=') == -1:    # 不要印 holo = 'am'am
            print "%s\t%d" % (ls, curpage)
            sts = NOT_GLOS
        elif len(ls) == 0:
            sts = GLOS


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        extractFromFile(f.readlines())
