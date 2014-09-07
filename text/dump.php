<?php
$pdo = new PDO("sqlite://tmp/toufu.sq3");

for($i = 320; $i <= 356; $i++) {
  echo "Page $i\n";
  $st = $pdo->prepare("SELECT cont FROM pages WHERE p=:p");
  $st->execute(array(':p' => $i));
  $row = $st->fetch(PDO::FETCH_NUM);
  $rows = explode("\n", $row[0]);
  $rows = array_map('trim', $rows);
  $row = implode("\n", $rows);
  $fp = fopen(sprintf("p-%03d.txt", $i), 'w');
  fwrite($fp, $row);
  fclose($fp);
}
