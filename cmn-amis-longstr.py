# -*- coding: utf8 -*-
# vim: ts=4 et sw=4 sts=4
# 產生阿美語-漢語的超長字串

import sys
import json
import codecs

def load_amis():
    longTitle = {}
    longEx = {}
    dictionary = json.load(open("dict-amis.json"))
    for word in dictionary:
        title = word['title']
        longTitle[title] = ''
        longEx[title] = ''
        for het in word['heteronyms']:
            for defs in het['definitions']:
                if 'def' not in defs:
                    print "!!!!!", title
                dx = defs['def']
                ex = defs.get('example', [])
                p2 = dx.find(u'\ufffb')
                zh = dx[p2+1:]
                longTitle[title] += zh
                for x in ex:
                    p2 = x.find(u'\ufffb')
                    zh = x[p2+1:]
                    longEx[title] += zh

    longstr = ''
    for (k, v) in longTitle.iteritems():
        if len(v) == 0: continue
        longstr += u'\ufffa' + k + u'\ufffb' + v + '\n'
        codecs.open("revdict-amis-def.txt", "w", "utf8").write(longstr)
    longstr = ''
    for (k, v) in longEx.iteritems():
        if len(v) == 0: continue
        longstr += u'\ufffa' + k + u'\ufffb' + v + '\n'
        codecs.open("revdict-amis-ex.txt", "w", "utf8").write(longstr)

if __name__ == '__main__':
    load_amis()
