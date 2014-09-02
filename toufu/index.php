<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width"/>
<meta property="og:title" content="阿美語萌典"/>
<meta property="og:description" content="方敏英字典電子化 +1"/>
<meta property="og:image" content="https://raw.github.com/g0v/style-guide/master/logo/png/double-line/g0v-2line-white-s.png">
<meta property="og:url" content="http://ckhis.ck.tp.edu.tw/~ljm/amis-toufu">
<title>阿美語萌典</title>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.2.2/bootstrap.min.js"></script>
<script type="text/javascript">
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-54332820-1', 'auto');
  ga('send', 'pageview');
</script>
<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.2.2/css/bootstrap.css">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
    <h3>阿美語字典OCR</h3>
    <h3>請填入圖片中的字</h3>
    <div class="manual">手寫的字體不要打，謝謝。<a href="https://g0v.hackpad.com/ep/pad/static/rVh0lLhnVuF">說明書</a></div>
    <button id="submit" class="btn btn-primary submit" tabindex="2">　送出　</button>
    <button id="no-content" class="btn no-content" tabindex="3">這是空白</button>
    <input id="ans" class="form-control ans" type="text" name="ans" tabindex="1" />
    <input id="ans-shadow" class="form-control ans-shadow" type="text" readonly="true" tabindex="-1" style="display: none"/>
    <!-- <button id="next" tabindex="10">下一張</button> -->
    <div class="tip">Enter: 送出 / shift+Enter: 這是空白 / ctrl+Enter: 這答案沒錯</div>

    <div>
	<span class="cell-info"></span>
        <button id="confirm" class="btn btn-success confirm" tabindex="5566" style="display: none; margin-left: 43%">這答案沒錯</button>
    </div>
    <div class="cell-image"></div>
    <button id="unclear" class="btn btn-warning unclear" tabindex="-1" style="display: none;">圖片不清楚</button>
    <div class="progress">
    <div class="bar" style="width: 80%;"></div>
    <span id="progress_text"></span>
    </div>
    <div><b>以下是供參考的機器自動辨識結果，可以複製正確的部份到答案欄，可以少打一些字</b></div>
    <div class="ocr_block">
        <label for="">英文OCR</label>
        <textarea name="" id="ocrEng" cols="50" rows="4"></textarea>
    </div>
    <div class="ocr_block">
        <label for="">中文OCR</label>
        <textarea name="" id="ocrCht" cols="50" rows="4"></textarea>
    </div>
    <div style="clear: both;"></div>
</div>
<script src="cell.js"></script>
<link rel="stylesheet" href="cell.css">
</body>
</html>
