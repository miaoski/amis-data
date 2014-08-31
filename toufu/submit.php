<?php	// Submit answer to some toufu
if(!isset($_POST['p']) ||
   !isset($_POST['line']) ||
   !isset($_POST['ans']) ||
   strlen(trim($_POST['ans'])) == 0) {
   print_r($_POST);
   die("Invalid params");
}

$pdo = new PDO("sqlite:toufu.sq3");

$v = array(
	':p' => intval($_POST['p']),
	':line' => intval($_POST['line']),
	':ans' => $_POST['ans'],
);
$stmt = $pdo->prepare("UPDATE toufu SET ans=:ans,cnt=cnt+1 WHERE p=:p AND line=:line");
$stmt->execute($v);
$stmt = $pdo->prepare("INSERT INTO log VALUES (:p, :line, :ans)");
$stmt->execute($v);
