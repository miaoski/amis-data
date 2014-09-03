<?php	// 把全形改半形，把破折號規範化
header('Content-Type: application/json; charset=utf-8');
$pdo = new PDO("sqlite:toufu.sq3");

for($i = 46; $i <= 356; $i++) {
	$p = sprintf('%03d', $i);
	$st = $pdo->prepare("SELECT ans FROM toufu WHERE p=:p ORDER BY line");
	$st->execute(array(':p' => $i));
	$line = "";
	while($row = $st->fetch(PDO::FETCH_ASSOC)) {
		$n = trim($row['ans']);
		if($n == '[這是空白]' || $n == '[圖片不清楚]')
			$n = '';
		$n = str_replace('（', '(', $n);
		$n = str_replace('）', ')', $n);
		$n = preg_replace('/-+/', '-', $n);
		$n = str_replace('ー', ' - ', $n);
		$n = str_replace('—', ' - ', $n);
		$n = str_replace('─', ' - ', $n);
		$n = str_replace('—', ' - ', $n);
		$n = str_replace('—', ' - ', $n);
		$n = str_replace('–', ' - ', $n);
		$n = str_replace(' ─ ', ' - ', $n);
		$n = str_replace('-', ' - ', $n);
		$n = str_replace('(', ' (', $n);
		$n = str_replace(')', ') ', $n);
		$n = preg_replace('/ +/', ' ', $n);
		$n = str_replace(' /', '/', $n);
		$n = str_replace('/ ', '/', $n);
		$n = preg_replace('/(\w)\/(\w)/', '$1 / $2', $n);
		$n = trim($n);
		$line .= "$n\n";
	}
	$pdo->beginTransaction();
	$st = $pdo->prepare("INSERT INTO pages VALUES (:p, :cont)");
        print "$i\n";
	$st->execute(array(
		':p'    => $i,
		':cont' => $line));
	$pdo->commit();
}
