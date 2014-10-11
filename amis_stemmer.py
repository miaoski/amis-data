# -*- coding: utf8 -*-
# vim: et sws=4 ts=4 sts=4
# Reduce grammatical affixes from amis word to the longest match in index.json
# Ref.: Fey, Virginia (1986) pp.357--365

import json

with open('index.json', 'r') as f:
    INDEX = [x.replace('ng', 'g') for x in json.load(f)]

# I hate exceptions, but let's cut things short
EXCEPTIONS = {
    'mapararaw': ('mapa', 'raraw'),
}

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
    'mitolon':      '`mi~`tolon~',
    'pitolon':      '`pi~`tolon~',
    'Pitolon':      '`Pi~`tolon~',
    'Mararaw':      '`Ma~`raraw~',
    'matayal':      '`ma~`tayal~',
    "ma'araw":      "`ma~`'araw~",
    'katayal':      '`ka~`tayal~',
    'katayalan':    '`katayalan~',
    'pitolonan':    '`pi~`tolon~`an~',
    "namafana'":    "`nama~`fana'~",
    'nanisigkoay':  '`nani~`sigko~`ay~',
    'panokay':      '`pa~`nokay~',
    'papinokay':    '`papi~`nokay~',
    'papipanokayen':'`papipa~`nokay~`en~',
    'pakacowa':     '`pakacowa~',
    'pakatimol':    '`paka~`timol~',
    'pakalahci':    '`paka~`lahci~',
    'gagasawan':    '`ga~`gasaw~`an~',
    'papipakatayalen': '`papipaka~`tayal~`en~',
    'saasik':       '`saasik~',
    'sapitilid':    '`sapi~`tilid~',
    'sapatilid':    '`sapa~`tilid~',
    'sakatayal':    '`saka~`tayal~',
    'mitgilay':     '`mi~`tgil~`ay~',
    'matgilay':     '`ma~`tgil~`ay~',
    "mafana'ay":    "`ma~`fana'~`ay~",
    'panokayen':    '`pa~`nokay~`en~',
    'papinokayen':  '`papi~`nokay~`en~',
    'negnegaw':     '`negneg~`aw~',
    'sapinegnegaw': '`sapi~`negneg~`aw~',
    'sakatayra':    '`saka~`tayra~',
    'mipatala':     '`mi~`patala~',
    "mafana'":      "`ma~`fana'~",
    'nipinegneg':   '`nipi~`negneg~',
    'nitgilan':     '`ni~`tgil~`an~',
    'nitooran':     '`ni~`toor~`an~',
    'nipipatilid':  '`nipipa~`tilid~',
    "nipipakafana'": "`nipipaka~`fana'~",
    'sapitilidan':  '`sapi~`tilid~`an~',
    'sakatayraan':  '`saka~`tayra~`an~',
    "nipakafana'an":"`nipaka~`fana'~`an~",
    'pasowal':      '`pa~`sowal~',
    'sapatilidaw':  '`sapa~`tilid~`aw~',
    "sapakafana'aw":"`sapaka~`fana'~`aw~",
    "misaloma'":    "`misaloma'~",
    'misatfon':     '`misatfon~',
    'kasakyokay':   '`kasa~`kyokay~',
    'malawawa':     '`mala~`wawa~',
    'mapalawaco':   '`ma~`palawaco~',
    'mikihatiya':   '`mikihatiya~',
    'pikihatiya':   '`piki~`hatiya~',
    "pakitira'":    "`paki~`tira'~",
    'pakomagah':    '`pako~`magah~',
    'citilid':      '`ci~`tilid~',
    'ciina':        '`ci~`ina~',
    'ciwawa':       '`ci~`wawa~',
    'halitolon':    '`hali~`tolon~',
    "hali'pah":     "`hali~`'pah~",
    "mafana'to":    "`ma~`fana'~`to~",
    'tatayra':      '`ta~`tayra~',
    'mamatayal':    '`mamatayal~',
    'mapararaw':    '`mapa~`raraw~',
# 'cacitodog': '`todo]g~', # removed, not in our dictionary
    "lomaloma'":    "`loma~`loma'~",
    'romaroma':     '`roma~`roma~',
    'malalicalicay':'`mala~`lica~`licay~',
    'malalicay':    '`mala~`licay~',
    'kasakitakitakit': '`kasa~`kita~`kitakit~',
    'dadayadaya':   '`dadaya~`daya~',
    'tamtamdaw':    '`tam~`tamdaw~',}

def compose(*wx):
    return ''.join(['`'+x+'~' for x in wx if x is not None])

def gnostic(w):
    "Stemmer without referring to index.json"
    import re
    if len(w) < 1 or not re.search(r"[\w:']+", w): return w
    if w in INDEX: return compose(w)
    if w in EXCEPTIONS: return compose(*EXCEPTIONS[w])

    # prefix + suffix
    px = None
    sx = None
    for (pre, suf) in pre_suffix:
        if w.lower().startswith(pre) and w.endswith(suf):
            psw = w[len(pre):-len(suf)]
            if psw in INDEX: 
                (px, psw, sx) = (w[:len(pre)], psw, w[-len(suf):])
                return compose(px, psw, sx)
    # prefix
    psw = w
    for p in prefix:        # longest -> shortest
        if w.lower().startswith(p):
            psw = w[len(p):]
            if psw in INDEX: 
                (px, psw) = (w[:len(p)], psw)
                return compose(px, psw, sx)
            (px, psw) = (w[:len(p)], psw)
            break
    w = psw
    for p in suffix:
        if w.endswith(p):
            psw = w[:-len(p)]
            if psw in INDEX: 
                (psw, sx) = (psw, w[-len(p):])
                return compose(px, psw, sx)
    return deduplication(px, w, sx)


def deduplication(*pps):
    "Remove duplication by syllabic rules"
    (px, w, sx) = pps
    if len(w) >= 8 and w[0:4] == w[4:8]:    # (CVCV)CVCV.. => CVCV..
        return compose(px, w[:4], w[4:], sx)
    if len(w) >= 8 and w[0:3] == w[3:6]:    # (CVC)CVC.. => CVC..
        return compose(px, w[:3], w[3:], sx)
    if len(w) >= 10 and w[2:6] == w[6:10]:  # CVCVCV(CVCV).. => CVCVCV..
        return compose(px, w[0:6], w[6:], sx) # not sure if specially for dadayadaya
    if len(w) >= 6 and w[0:2] == w[2:4]:    # (CV)CV.. => CV..
        return compose(px, w[:2], w[2:], sx)
    return compose(w)

def runtest():
    failed = False
    for (k,v) in test_suits.iteritems():
        r = gnostic(k)
        if r != v:
            print "Failed: %s => %s, expected: %s" % (k, r, v)
            failed = True
    if not failed:
        print "Success"

if __name__ == '__main__':
    runtest()
