# -*- coding: utf8 -*-
# vim: ts=4 et sw=4 sts=4

import sys
import json
import codecs

csv = codecs.open('amis-fey.csv', 'w', 'utf-8')

def add_apostrophe(*args):
    def addit(x):
        return "'"+x if x.startswith("'") else x
    return tuple(map(addit, args))

def load_amis():
    dictionary = json.load(open("dict-amis.json"))

    # Sort according to lexicon
    DICT = {}
    for word in dictionary:
        DICT[word['title']] = word
    words = DICT.keys()
    words.sort()

    for title in words:
        word = DICT[title]
        for het in word['heteronyms']:
            for defs in het['definitions']:
                if 'def' not in defs:
                    print "!!!!!", title
                if 'synonyms' in defs:
                    syn = ', '.join(defs['synonyms']).replace('`','').replace('~','')
                else:
                    syn = ''
                dx = defs['def']
                ex = defs.get('example', [])
                p2 = dx.find(u'\ufffb')
                en = dx[2:p2]
                zh = dx[p2+1:]
                if len(ex) == 0:        # 第一個例句和解釋放在一起
                    csv.write('%s\t%s\t%s\t\t\t\t%s\n' % add_apostrophe(title, en, zh, syn))
                else:
                    x = ex.pop(0)
                    p1 = x.find(u'\ufffa')
                    p2 = x.find(u'\ufffb')
                    am = x[1:p1].replace('`', '').replace('~', '')
                    am_en = x[p1+1:p2]
                    am_zh = x[p2+1:]
                    csv.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % add_apostrophe(title, en, zh, am, am_en, am_zh, syn))
                for x in ex:
                    title = ''
                    p1 = x.find(u'\ufffa')
                    p2 = x.find(u'\ufffb')
                    am = x[1:p1].replace('`', '').replace('~', '')
                    en = x[p1+1:p2]
                    zh = x[p2+1:]
                    csv.write('%s\t\t\t%s\t%s\t%s\n' % add_apostrophe(title, am, en, zh))
                title = ''

if __name__ == '__main__':
    load_amis()
