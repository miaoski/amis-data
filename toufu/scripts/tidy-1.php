<?php	// 把全形改半形，把破折號規範化
header('Content-Type: application/json; charset=utf-8');
$pdo = new PDO("sqlite:toufu.sq3");


$pdo->beginTransaction();
$st = $pdo->prepare("SELECT * FROM toufu WHERE ans LIKE '%-%' OR ans LIKE '%ー%' OR ans LIKE '%（%'");
$st->execute();
while($row = $st->fetch(PDO::FETCH_ASSOC)) {
	$n = str_replace('（', '(', $row['ans']);
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
	if($n != $row['ans']) {
		echo "Update $row[p] : $row[line]\n";
		$repl = $pdo->prepare('UPDATE toufu SET ans=:ans WHERE p=:p AND line=:line');
		$repl->execute(array(':ans' => $n, ':p' => $row['p'], ':line' => $row['line']));
	}
}
$pdo->commit();
