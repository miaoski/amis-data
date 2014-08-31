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

4. 寫前端，從 https://github.com/ctiml/campaign-finance.g0v.ctiml.tw 抄一些設計過來
