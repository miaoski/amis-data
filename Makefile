SQ3 = dict-amis.sq3

all:
	@echo "Usage: make sqlite"
	@echo "       make quickdic"
	@echo "       make moedict"

moedict:
	python makeindex.py
	python moedict.py

sqlite:	moedict dict-amis.sql
	rm -f $(SQ3)
	sqlite3 $(SQ3) < $<
	python moedict.py
	python sqlite_dict.py

quickdic:
	python quickdic.py
	java -Xmx512m -jar DictionaryBuilder.jar \
		--dictOut=AMI-CMN.quickdic   \
		--lang1=AMI   \
		--lang2=CMN   \
		--lang2Stoplist=CMN_stoplist.txt \
		--dictInfo="moedict no pangcah"   \
		--input1=amis-cmn.dicts.txt   \
		--input1Name="amis-cmn.dicts.txt"   \
		--input1Charset=UTF8   \
		--input1Format=tab_separated   \
		--input1FlipColumns=false
	java -Xmx512m -jar DictionaryBuilder.jar \
		--dictOut=AMI-EN.quickdic   \
		--lang1=AMI   \
		--lang2=EN   \
		--lang2Stoplist=EN_stoplist.txt \
		--dictInfo="moedict no pangcah"   \
		--input1=amis-en.dicts.txt   \
		--input1Name="amis-en.dicts.txt"   \
		--input1Charset=UTF8   \
		--input1Format=tab_separated   \
		--input1FlipColumns=false
	@echo "請上傳 *.quickdic 至手機的 /SDCard/quickdic 目錄中"
