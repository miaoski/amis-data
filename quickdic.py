# -*- coding: utf8 -*-
# Convert amis dict to quickdic format (amis-cmn)
# vim: ts=4 et sw=4 sts=4

import sys
import json
import codecs

def quickdic():
    dictionary = json.load(open("dict-amis.json"))
    amis_cmn = codecs.open('amis-cmn.dicts.txt', 'w', 'utf8')
    cmn_amis = codecs.open('cmn-amis.dicts.txt', 'w', 'utf8')
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
                cmn_amis.write('\t'.join((title, zh)) + '\n')
    amis_cmn.close()
    cmn_amis.close()

if __name__ == '__main__':
    quickdic()
