# -*- coding: utf8 -*-
# Convert ?.txt to dict-amis.json for moedict

import sys

JSON = {}
INDEX = []

def ng(s):
	return s.replace('g', 'ng')

def ngtilde(s):
	import re
	return re.sub(r'([\w\']+)', r'`\1~', ng(s))

def addsplt(s):
	return u'\ufff9'+s[0].decode('utf8')+u'\ufffa'+s[1].decode('utf8')+u'\ufffb'+s[2].decode('utf8')

def addtilde(s):
	return '`'+s+'~'

def mkword(title, definitions):
	global JSON, INDEX
	word = {'title': title,
		'heteronyms': [{'definitions': definitions}]}
	JSON[title] = word
	INDEX.append(title)

def mkdef(defi, examples, link):
	defdic = {}
	if len(examples) > 0:
		defdic['example'] = examples
		examples = []
	if defi[2] != '':
		defdic['def'] = addsplt(defi)
	if link:
		defdic['link'] = map(addtilde, link.split(','))
	if link and 'def' not in defdic:
		try:
			defdic['def'] = JSON[link]['heteronyms'][0]['definitions'][0]['def']
		except:
			print "Cannot find the reference: ", link
	return defdic

def readdict(fn):
	fp = open(fn, 'ru')
	title = None
	for line in fp:
		if line.strip() == '' and title:
			defdic = mkdef(defi, examples, link)
			if len(defdic) > 0:
				definitions.append(defdic)
			mkword(title, definitions)
			title = None
			continue
		if line.strip() == '':	# 空白行
			continue
		if line[0] == '#':
			continue
		(tag,st) = line.strip().split('=', 1)
		if tag == 't':
			title = ng(st)
			definitions = []
			examples = []
			link = None
			defi = ['', '', '']
			continue
		if tag == 'E':
			defdic = mkdef(defi, examples, link)
			if len(defdic) > 0:
				definitions.append(defdic)
			defi = ['', st, '']
			continue
		if tag == 'f':
			defi[2] = st
			continue
		if tag == 'pa':
			ex = [ngtilde(st), '', '']
			continue
		if tag == 'pe':
			ex[1] = st
			continue
		if tag == 'pm':
			ex[2] = st
			examples.append(addsplt(ex))
			continue
		if tag == 'ea':
			ex = [ngtilde(st), '', '']
			continue
		if tag == 'ee':
			ex[1] = st
			continue
		if tag == 'em':
			ex[2] = st
			examples.append(addsplt(ex))
			continue
		if tag == 'l':
			link = ng(st)
	if title:
		defdic = mkdef(defi, examples, link)
		if len(defdic) > 0:
			definitions.append(defdic)
		mkword(title, definitions)

if __name__ == '__main__':
	import os
	import json
	import re
	import codecs
	for fn in os.listdir('.'):
		if re.match(r'^[0a-z]\.txt$', fn):
			readdict(fn)
	f = codecs.open('dict-amis.json', mode='w', encoding='utf8')
	f.write(json.dumps(JSON.values(), indent=2, separators=(',', ':'), ensure_ascii = False))
	f.close()
	f = codecs.open('index.json', mode='w', encoding='utf8')
	f.write(json.dumps(INDEX, indent=2, separators=(',', ':'), ensure_ascii = False))
	f.close()
