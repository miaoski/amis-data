import sys
import sqlite3

conn = sqlite3.connect('/tmp/toufu.sq3')
c = conn.cursor()

f = open('glossary-list', 'r')
for lx in f:
    (glos, page) = lx.strip().split('\t')
    c.execute('SELECT line FROM toufu WHERE p=? AND ans LIKE ?',
            (int(page), glos+'%'))
    line = c.fetchone()
    if line:
        print '\t'.join([glos, page, str(line[0])])
    else:
        print '\t'.join([glos, page, '-1'])
