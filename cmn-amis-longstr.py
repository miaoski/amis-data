# -*- coding: utf8 -*-
# vim: ts=4 et sw=4 sts=4
# 產生阿美語-漢語的超長字串

import sys
import json
import codecs

def load_amis():
    longstr = ''
    dictionary = json.load(open("dict-amis.json"))
    for word in dictionary:
        title = word['title']
        for het in word['heteronyms']:
            for defs in het['definitions']:
                if 'def' not in defs:
                    print "!!!!!", title
                dx = defs['def']
                ex = defs.get('example', [])
                p2 = dx.find(u'\ufffb')
                zh = dx[p2+1:]
                longstr += u'\ufffa' + title + u'\ufffb' + zh
                for x in ex:
                    p2 = x.find(u'\ufffb')
                    zh = x[p2+1:]
                    longstr += zh
                longstr += '\n'
    codecs.open("revdict-amis.txt", "w", "utf8").write(longstr)

if __name__ == '__main__':
    load_amis()
