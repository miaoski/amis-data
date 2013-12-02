# -*- coding: utf8 -*-
# Compare two JSON files in moedict format
import json
import sys

J1 = {}
J2 = {}

f1 = open(sys.argv[1], 'ru')
f2 = open(sys.argv[2], 'ru')
j1 = json.load(f1)
j2 = json.load(f2)
for x in j1:
	J1[x['title']] = x
for x in j2:
	J2[x['title']] = x
if J1 == J2:
	print "Identical"
else:
	for k in set(J1.keys() + J2.keys()):
		if k in J1 and k in J2:
			if J1[k] != J2[k]:
				print k, ' differs.'
		else:
			if k in J1:
				print k, ' only in ', sys.argv[1]
			if k in J2:
				print k, ' only in ', sys.argv[2]
f1.close()
f2.close()
