SQ3 = dict-amis.sq3

all:
	@echo "Usage: make sqlite"
	@echo "       make quickdic"

sqlite:	dict-amis.sql
	rm -f $(SQ3)
	sqlite3 $(SQ3) < $<
	python moedict.py
	python sqlite_dict.py

quickdic:
	python quickdic.py
