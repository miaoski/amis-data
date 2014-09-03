<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width"/>
<meta property="og:title" content="阿美語萌典 [整頁模式]"/>
<meta property="og:description" content="方敏英字典電子化 +1"/>
<meta property="og:image" content="https://raw.github.com/g0v/style-guide/master/logo/png/double-line/g0v-2line-white-s.png">
<meta property="og:url" content="http://ckhis.ck.tp.edu.tw/~ljm/amis-toufu">
<title>阿美語萌典 [整頁模式]</title>
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
    <div class="row">
      <div class="span6"></div>
      <div class="span6"><h3>阿美語字典OCR：二校</h3></div>
    </div>
    <div class="span6"></div>
    <div class="manual span3">
      請校對整頁，並忽略每一行前後的空白。
    </div>
    <div class="span2">
      <button id="submit" class="btn btn-primary submit" tabindex="2">　送出　</button>
    </div>
</div>


<div style="display:none;">
  <span class="cell-info"></span>
</div>
<div id="img"></div>
<textarea id="txt" rows="50"></textarea>


<script src="cell.js"></script>
<link rel="stylesheet" href="cell.css">
</body>
</html>
