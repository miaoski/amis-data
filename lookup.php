<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<title>阿美語萌典 - 查詢</title>
<meta name="viewport" content="width=device-width; initial-scale=1.0" />
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
</head>
<body>
<div class="container">
  <div class="panel panel-default" style="margin:0 auto;width:500px">
    <div class="panel-heading">
      <h2 class="panel-title">Lookup moedict no Pangcah</h2>
    </div>
    <div class="panel-body">
      <form name="form" method="get" action="#" class="form-horizontal" role="form">
      <div class="form-group">
        <label for="query" class="col-lg-2 control-label">Search:</label>
        <div class="col-lg-10">
          <input type="text" class="form-control" id="query" name="query" placeholder="請輸入阿美語、英文或漢文">
        </div>
      </div>
      </form>
    </div>
  </div>
</div>
<?php
$path = explode('/', $_SERVER['PHP_SELF']);
array_pop($path);
$path = implode('/', $path);
if(isset($_GET['query']) && !empty($_GET['query'])) {
  $query = $_GET['query'];
  $pdo = new PDO("sqlite:dict-amis.sq3");

  $rets = array();
  $st = $pdo->prepare("SELECT * FROM amis WHERE example LIKE :q OR en LIKE :q OR cmn LIKE :q LIMIT 100");
  $st->execute(array(':q' => "%$query%"));
?>
<div class="container">
  <table class="table">
    <thead>
      <tr><th>單詞</th><th>例句</th><th>英文解釋</th><th>漢文解釋</th></tr>
    </thead>
    <tbody>
<?php
  $result = $st->setFetchMode(PDO::FETCH_NUM);
  while($row = $st->fetch()) {
    $amis = "<a href=\"$path#;$row[0]\">$row[0]</a>";
    print "<tr><td>$amis</td><td>$row[1]</td><td>$row[2]</td><td>$row[3]</td></tr>\n";
  }
?>
    </tbody>
  </table>
</div>
<?php
}
?>
</body>
</html>
