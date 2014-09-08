#!/usr/bin/env python
# -*- coding: utf8 -*-

import fileinput
import unicodedata as ud


def unbreak_line(iterator):
    buf = []
    for l in iterator:
        l = l.decode("utf8")
        if "-" in l:
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


if __name__ == "__main__":
    for l in unbreak_line(fileinput.input()):
        if "-" not in l:
            print "problem with", l.encode("utf8")
            continue
        amis, remaining = l.split("-", 1)
        english, mandarin = split_on_first_CJK(remaining)
        print "\n".join([amis, english, mandarin, "\n"]).encode("utf8")
