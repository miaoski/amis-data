切豆腐的細節
============

1. 切成一行一行的

    for i in `seq -f%03g 047 356`; do
      ../StripPhotoIntoRows/cut_line ~/amis-data/pic/$i.jpg
      for n in cut_strip_*.jpg; do
        mv $n `echo $n | sed "s/cut_strip/$i/"`
      done
    done

2. 壓小一點點

    mkdir s
    for n in ???_???.jpg; do
      bn=`basename $n .jpg`
      convert -resize 1024x $n s/$bn.jpg
    done

3. 用 SQLite3 裝資料

    sqlite> .dump
    PRAGMA foreign_keys=OFF;
    BEGIN TRANSACTION;
    CREATE TABLE toufu ( p int, line int, words text );
    CREATE INDEX p on toufu (p);
    CREATE INDEX line on toufu (line);
    COMMIT;

    for n in *.jpg; do
      echo "insert into toufu values ("`echo $n | cut -c1-3`", "`echo $n | cut -c5-7`", NULL);"
    done


    使用tesseract 做中英文的初步OCR，可以讓大家少打一點字
    
    需要先在系統上安裝好tesseract, 並裝好中文語言檔(chi_tra)，另外db裡toufu這個表要有ocr_eng, ocr_cht這兩欄

	    for n in *.jpg; do
	      php ocr_guess.php "$n";
	    done


4. 寫前端，從 https://github.com/ctiml/campaign-finance.g0v.ctiml.tw 抄一些設計過來
