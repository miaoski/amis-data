<?php	// Submit answer to some toufu
header('Content-Type: application/json; charset=utf-8');
$pdo = new PDO("sqlite:../toufu.sq3");

error_log(serialize($_POST));
if(!isset($_POST['p']) ||
   !isset($_POST['cont']) ||
   strlen(trim($_POST['cont'])) == 0) {
   die();
}

$v = array(
	':p' => intval($_POST['p']),
	':cont' => $_POST['cont'],
);
$stmt = $pdo->prepare("INSERT INTO log VALUES (:p, 999, :cont)");
$stmt->execute($v);
$stmt = $pdo->prepare("UPDATE pages SET cont=:cont,lock=datetime('now', '+30 days') WHERE p=:p");
$stmt->execute($v);
echo json_encode(array('p' => intval($_POST['p'])));
