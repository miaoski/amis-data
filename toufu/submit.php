<?php	// Submit answer to some toufu
header('Content-Type: application/json; charset=utf-8');
$pdo = new PDO("sqlite:toufu.sq3");

if(!isset($_POST['p']) ||
   !isset($_POST['line']) ||
   !isset($_POST['ans']) ||
   strlen(trim($_POST['ans'])) == 0) {
   get_progress($pdo);
   die();
}


$v = array(
	':p' => intval($_POST['p']),
	':line' => intval($_POST['line']),
	':ans' => $_POST['ans'],
);
$stmt = $pdo->prepare("UPDATE toufu SET ans=:ans,cnt=cnt+1 WHERE p=:p AND line=:line");
$stmt->execute($v);
$stmt = $pdo->prepare("INSERT INTO log VALUES (:p, :line, :ans)");
$stmt->execute($v);
get_progress($pdo);

function get_progress($pdo) {
  $st = $pdo->prepare("SELECT COUNT(1) FROM toufu WHERE ans IS NOT NULL");
  $st->execute();
  $row = $st->fetch();
  if($row) {
    echo json_encode(array('cnt' => intval($row[0])));
  }
}
