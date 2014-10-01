# -*- coding: utf8 -*-
# vim: et sws=4 ts=4 sts=4
# Reduce grammatical affixes from amis word to the longest match in index.json
# Ref.: Fey, Virginia (1986) pp.357--365

import json

with open('index.json', 'r') as f:
    INDEX = [x.replace('ng', 'g') for x in json.load(f)]

# ordering is important
prefix = [ 'papipaka', 'nipipaka', 'pasasi', 'papipa', 'nipipa', 'mipaka',
'saso', 'sasi', 'sapi', 'sapa', 'saka', 'piki', 'pasa', 'papi', 'pala',
'pako', 'paki', 'paka', 'nipi', 'nika', 'nani', 'nama', 'misa', 'miki',
'mala', 'kasa', 'hali', 'nai', 'sa', 'na', 'ni', 'ma', 'mi', 'ka', 'ci',
'pa', 'pi', ]

pre_suffix = [
    ('ka', 'an'),
    ('pi', 'an'),
    ('sapi', 'an'),
    ('saka', 'an'),
    ('nipaka', 'an'),
    ('sapi', 'aw'),
    ('sapa', 'aw'),
    ('sapaka', 'aw'),
    ('sa', 'en'), ]

# ordering is important
suffix = [ 'ananay', 'en', 'ay', 'an', 'aw', 'to', 'ho', ]

# stem duplication: lomaloma', romaroma, tamtamdaw, kasakitakitakit, dadayadaya
test_suits = {
    'mitolon': 'tolon',
    'pitolon': 'tolon',
    'matayal': 'tayal',
    "ma'araw": "'araw",
    'katayal': 'tayal',
    'katayalan': 'katayalan',
    'pitolonan': 'tolon',
    "namafana'": "fana'",
    'nanisigkoay': 'sigko',
    'panokay': 'nokay',
    'papinokay': 'nokay',
    'papipanokayen': 'nokay',
    'pakacowa': 'pakacowa',
    'pakatimol': 'timol',
    'pakalahci': 'lahci',
    'papipakatayalen': 'tayal',
    'saasik': 'saasik',
    'sapitilid': 'tilid',
    'sapatilid': 'tilid',
    'sakatayal': 'tayal',
    'mitgilay': 'tgil',
    'matgilay': 'tgil',
    "mafana'ay": "fana'",
    'panokayen': 'nokay',
    'papinokayen': 'nokay',
    'negnegaw': 'negneg',
    'sapinegnegaw': 'negneg',
    'sakatayra': 'tayra',
    'mipatala': 'patala',
    "mafana'": "fana'",
    'nipinegneg': 'negneg',
    'nitgilan': 'tgil',
    'nitooran': 'toor',
    'nipipatilid': 'tilid',
    "nipipakafana'": "fana'",
    'sapitilidan': 'tilid',
    'sakatayraan': 'tayra',
    "nipakafana'an": "fana'",
    'pasowal': 'sowal',
    'sapatilidaw': 'tilid',
    "sapakafana'aw": "fana'",
    "misaloma'": "misaloma'",
    'misatfon': 'misatfon',
    'kasakyokay': 'kyokay',
    'malawawa': 'wawa',
    'mapalawaco': 'palawaco',
    'mikihatiya': 'mikihatiya',
    'pikihatiya': 'hatiya',
    "pakitira'": "tira'",
    'pakomagah': 'magah',
    'citilid': 'tilid',
    'ciina': 'ina',
    'ciwawa': 'wawa',
    'halitolon': 'tolon',
    "hali'pah": "'pah",
    "mafana'to": "fana'",
    'tatayra': 'tayra',
    'mamatayal': 'mamatayal',
    'mapararaw': 'raraw',
# 'cacitodog': 'todo]g', # removed, not in our dictionary
    "lomaloma'": "loma'",
    'romaroma': 'roma',
    'malalicalicay': 'licay',
    'malalicay': 'licay',
    'kasakitakitakit': 'kitakit',
    'dadayadaya': 'dadaya',
    'dadayadaya': 'dadaya',
    'tamtamdaw': 'tamdaw',}

def gnostic(w):
    "Stemmer without referring to index.json"
    if w in INDEX: return w
    # prefix + suffix
    for (pre, suf) in pre_suffix:
        if w.startswith(pre) and w.endswith(suf):
            psw = w[len(pre):-len(suf)]
            if psw in INDEX: return psw
    # prefix
    psw = w
    for p in prefix:        # longest -> shortest
        if w.startswith(p):
            psw = w[len(p):]
            if psw in INDEX: return psw
            break
    w = psw
    for p in suffix:
        if w.endswith(p):
            psw = w[:-len(p)]
            if psw in INDEX: return psw
    return deduplication(w)


def deduplication(w):
    "Remove duplication by syllabic rules"
    if len(w) >= 8 and w[0:4] == w[4:8]:    # (CVCV)CVCV.. => CVCV..
        return w[4:]
    if len(w) >= 8 and w[0:3] == w[3:6]:    # (CVC)CVC.. => CVC..
        return w[3:]
    if len(w) >= 10 and w[2:6] == w[6:10]:  # CVCVCV(CVCV).. => CVCVCV..
        return w[0:6]                       # not sure if specially for dadayadaya
    if len(w) >= 6 and w[0:2] == w[2:4]:    # (CV)CV.. => CV..
        return w[2:]
    return w

def runtest():
    for (k,v) in test_suits.iteritems():
        r = gnostic(k)
        if r != v:
            print "Failed: %s => %s, expected: %s" % (k, r, v)
    else:
        print "Success"

if __name__ == '__main__':
    runtest()
