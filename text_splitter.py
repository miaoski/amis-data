#!/usr/bin/env python
# -*- coding: utf8 -*-

import re

import fileinput
import unicodedata as ud


def unbreak_line(iterator):
    buf = []
    for l in iterator:
        l = l.decode("utf8")
        new_entrie_match = re.match("^[\w':]+ (/ [\w':]+ ?)+\.?", l)
        if "-" in l or new_entrie_match:
            if "-" not in l:
                begin, end = new_entrie_match.span()
                l = l[:end] + " - " + l[end:]
            if len(buf) != 0:
                yield " ".join(buf)
                buf = []
        buf.append(l.strip())
    if len(buf) != 0:
        yield " ".join(buf)


def split_on_first_CJK(line):
    for i in range(len(line)):
        try:
            if 'CJK' in ud.name(line[i]):
                return (line[:i], line[i:])
        except:
            pass
    return (line, "")

def amis_synonym(glos):
    glos = glos.strip()
    syn = re.search(r"^/ ?([a-z':]+)[.]? ", glos)
    if syn:
        amis = "=> %s" % syn.group(1)
        eng = glos.split(' ', 1)[1]
        return amis+"\n"+eng
    else:
        return glos

if __name__ == "__main__":
    for l in unbreak_line(fileinput.input()):
        if "-" not in l:
            print "problem with", l.encode("utf8")
            continue
        amis, remaining = l.split("-", 1)
        heteronyms = []
        for nym in re.split("\d\.", remaining):
            english, mandarin = split_on_first_CJK(nym)
            if english.strip() == "" and mandarin.strip() == "":
                continue
            heteronyms.append((english, mandarin))
        if len(heteronyms) > 0:
            english, mandarin = zip(*heteronyms)
            heteronyms = "\n".join([amis_synonym(x) for i, x in enumerate(english)] + [x.strip() for i, x in enumerate(mandarin)])
        else:
            heteronyms = ""
            print "problem with (het)", l.encode("utf8")
        print "\n".join([amis, heteronyms, "\n"]).encode("utf8")
