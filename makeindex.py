# -*- coding: utf8 -*-
# Make index.json

import glob
import codecs
import json

INDEX = []

title = None
state = None
for fn in glob.iglob('?.txt'):
    fp = open(fn)
    for line in fp:
        l = line.strip()
        if l == '' and title:           # 寫入詞條
            INDEX.append(title)
            title = None
            state = None
            continue
        if l == '':
            continue
        if l[0] == '#':
            continue
        xs = l.split()              # 處理 word'a = word'b
        if state is None and len(xs) == 3 and xs[1] == '=':
            title = xs[0].strip().replace('g', 'ng')
            INDEX.append(title)
            title = None
            continue
        if state is None:           # 詞
            title = l.strip()
            state = 't'
INDEX.append(title)

f = codecs.open('index.json', mode='w', encoding='utf8')
x = json.dumps(INDEX, indent=2, separators=(',', ':'), ensure_ascii = False)
# print x[55260:55280]
f.write(x)
f.close()
