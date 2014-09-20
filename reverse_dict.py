# -*- coding: utf8 -*-

import codecs

import re
import json

def load_amis():
    d = json.load(open("dict-amis.json"))
    defs = [ {'w':word['title'], 'd':definitions['def']} for word in d for het in word['heteronyms'] for definitions in het['definitions'] if 'def' in definitions]
    enzh = [(x['d'].split(u"\ufffb")[0][2:],x['d'].split(u"\ufffb")[1]) for x in defs]
    amis = [ x['w'] for x in defs]
    zhsplitted = [re.split(ur"[，、。．，]",x[1]) for x in enzh]
    english = [x[0] for x in enzh]
    return (amis, english, zhsplitted)

def load_cedict():
    d = {}
    with codecs.open("cedict.txt", "r", "utf8") as f:
        for l in f:
            if l[0] == '#':
                continue
            x, en = l.split("/",1)
            ens = en.split("/")
            zh = x.split(" ",1)[0]
            d[zh] = ens
    return d

def main():
    (amis, english, zh) = load_amis()
    cedict = load_cedict()
    result = {}
    for i in range(len(zh)):
        candidates = [w for w in zh[i] if len(w) <4]
        # TODO: check is candidates are consistent with english[i] translations
        if len(candidates) > 0:
            print ("%s %s %s" % (amis[i],english[i], " / ".join(candidates))).encode("utf8")
            for w in candidates:
                if w not in result:
                    result[w] = []
                result[w].append(amis[i])
        else:
            # TODO: design some heuristic rules to deal with longer definitions (or maybe go through English)
            pass
    json.dump(result, codecs.open("revdict-amis.json", "w", "utf8"), ensure_ascii=False, indent=2, separators=(',',':'))


if __name__ == "__main__":
    main()
