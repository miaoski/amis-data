# -*- coding: utf8 -*-
# vim: ts=4 et sw=4 sts=4

import sys
import json
import sqlite3

conn = sqlite3.connect('dict-amis.sq3')
c = conn.cursor()

def load_amis():
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
                en = dx[2:p2]
                zh = dx[p2+1:]
                conn.execute('INSERT INTO amis VALUES (?, NULL, ?, ?)', (title, en, zh))
                for x in ex:
                    p1 = x.find(u'\ufffa')
                    p2 = x.find(u'\ufffb')
                    am = x[1:p1].replace('`', '').replace('~', '')
                    en = x[p1+1:p2]
                    zh = x[p2+1:]
                    conn.execute('INSERT INTO amis VALUES (?, ?, ?, ?)', (title, am, en, zh))
                conn.commit()

if __name__ == '__main__':
    load_amis()
