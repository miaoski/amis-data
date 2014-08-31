<?php	// Randomly select a toufu and return JSON
header('Content-Type: application/json; charset=utf-8');
$pdo = new PDO("sqlite:toufu.sq3");

$rows = array();
$st = $pdo->prepare("SELECT * FROM toufu LIMIT :offset,1");

for($i = 0; $i < 10; $i++) {
	$offset = rand(1, 14660);
	$st->execute(array(':offset' => $offset));
	$row = $st->fetch(PDO::FETCH_ASSOC);
	if($row) {
		$row['img'] = "$row[p]_$row[line].jpg";
		$rows[] = $row;
	}
}

echo json_encode($rows);
