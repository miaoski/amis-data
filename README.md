amis-data
=========

Data from Virginia Fey's Amis Dictionary


編輯說明
========

請參考各字母首字的檔案，a-z 以外的字首 (如 ' 或 ^) 請加在 0.txt ，如 'acam 請加在 0.txt 中。
單字與單字間請空一行。

第一個字元定義該行的屬性，請參考 [萌典原始碼] (https://github.com/audreyt/moedict-webkit/blob/master/main.ls#L507)
為了 parse 方便，加了 pa, pe, pm (phrase 短語) 和 ea, ee, em (example 例子) 六個 tag.

```
# 這個開頭的是註解
t=title (Word)
f=def (usually in Mandarin)
E=English (definition in English)
pa=phrase in Amis
pe=phrase in English
pm=phrase in Mandarin
ea=example in Amis
ee=example in English
em=example in Mandarin
R=root/stem
l=link
```

轉換
====

請用 `python moedict.py` 轉成萌典使用的 dict-amis.json 檔。

License
=======

謹感謝 [台灣聖經公會](http://www.biblesociety-tw.org/) 授權電子化。商業使用之授權，請洽台灣聖經公會。

This work is licensed under the Creative Commons 姓名標示-非商業性 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/deed.zh_TW.
