# -*- coding: utf8 -*-
# Convert amis dict to quickdic format (amis-cmn)
# Cf. https://code.google.com/p/quickdic-dictionary/wiki/BuildDictionary
# vim: ts=4 et sw=4 sts=4

import sys
import json
import codecs

def quickdic():
    dictionary = json.load(open("dict-amis.json"))
    amis_cmn = codecs.open('amis-cmn.dicts.txt', 'w', 'utf8')
    amis_en = codecs.open('amis-en.dicts.txt', 'w', 'utf8')
    for word in dictionary:
        title = word['title']
        for het in word['heteronyms']:
            for defs in het['definitions']:
                if 'def' not in defs:
                    print "!!!!!", title
                dx = defs['def']
                ex = defs.get('example', [])
                p2 = dx.find(u'\ufffb')
                en = dx[2:p2]
                zh = dx[p2+1:]
                amis_cmn.write('\t'.join((title, zh)) + '\n')
                amis_en.write('\t'.join((title, en)) + '\n')
    amis_cmn.close()
    amis_en.close()

if __name__ == '__main__':
    quickdic()
