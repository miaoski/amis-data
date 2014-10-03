amis-data
=========

Data from Virginia Fey's Amis Dictionary


編輯說明
========

請參考各字母首字的檔案，a-z 以外的字首 (如 ' 或 ^) 請加在 0.txt ，如 'acam 請加在 0.txt 中。
單字與單字間請空一行。

```
# 這個開頭的是註解
title (單詞)
English (英文定義)
def (漢語定義)
    阿美語片語
    英文解釋
    漢語解釋
    阿美語例句
    英文解釋
    漢語解釋
=> 相關詞, 逗號隔開, 字根請放這裡
```

字典標有其它讀音的部份，請拆開來，如: `'a'am / holo` 請拆成如下例:

```
'a'am
soft watery rice
稀飯、粥、米乳、米湯
=> miki'a'am

holo = 'a'am
```

字典中的例子，請拆開來，並在原本的詞條加上 link，如 `'aca` 下面的相關詞，請拆成:

```
'aca
...
=> pi'acaan, kalali'acaan, pa'aca, mi'aca

pi'acaan
market
商店、店鋪
```

拼寫
----

請保留原有的拼法，如 negneg 請不要寫成 nengneng, 轉換格式的時候，我們會用程式轉成現在比較通用的形式。


轉換
====

萌典
----
請用 `python moedict.py` 轉成萌典使用的 dict-amis.json 檔。


QuickDic
--------
Android 上的好用字典軟體 QuickDic. 請在 [quickdic-dictionary] (https://code.google.com/p/quickdic-dictionary/wiki/BuildDictionary) 下載 DictionaryBuilder.jar 後， `make quickdic` 即可。

預先轉換好的詞典檔，檔名叫 AMIS-CMN.quickdic 及 AMIS-EN.quickdic 也可以直接下載後，上傳到手機的 `/SDCard/quickdic` 目錄使用。


切豆腐
======

村長提示應該切個豆腐讓鄉民參與，計劃詳見 [Hackpad] (https://g0v.hackpad.com/moedict-no-pangcah--R2LBqjAdMwM).

把字典切成一行一行的程式，使用的是 [StripPhotoIntoRows] (https://github.com/CindyLinz/StripPhotoIntoRows).


License
=======

謹感謝 [台灣聖經公會](http://www.biblesociety-tw.org/) 授權電子化。商業使用之授權，請洽[台灣聖經公會]。

This work is licensed under the Creative Commons 姓名標示-非商業性 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/3.0/deed.zh_TW.
