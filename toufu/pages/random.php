<?php	// Randomly select a toufu and return JSON
header('Content-Type: application/json; charset=utf-8');
$pdo = new PDO("sqlite:../toufu.sq3");


$rets = array();
$st = $pdo->prepare("SELECT p FROM pages WHERE lock IS NULL OR lock < datetime('now', '-20 minutes')");
$st->execute();
$px = $st->fetchAll(PDO::FETCH_NUM);
shuffle($px);
$p = intval($px[0][0]);
$st = $pdo->prepare("SELECT cont FROM pages WHERE p=:p");
$st->execute(array(':p' => $p));
$row = $st->fetch(PDO::FETCH_ASSOC);
$row['p'] = sprintf("%03d", $p);
$st = $pdo->prepare("UPDATE pages SET lock=datetime('now') WHERE p=:p");
$st->execute(array(':p' => $p));

echo json_encode($row);
