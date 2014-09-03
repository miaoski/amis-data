<?php

if (!isset($argv[1])) {
    echo 'please supply image file name';
    exit(1);
}

$imgFn = $argv[1];
$tmpFileBase = '/tmp/amisOcrGuess';
$tmpFile = $tmpFileBase . ".txt";

function getOcr($lang)
{
    global $imgFn, $tmpFileBase, $tmpFile;

    $cmd = 'tesseract "' . $imgFn . '"  "' . $tmpFileBase . '" -l ' . $lang . ' 2>&1 > /dev/null';
    exec($cmd);
    $ocr = file_get_contents($tmpFile);
    $ocr = trim($ocr);

    return $ocr;
}

preg_match('/([0-9]{3})_([0-9]{3}).jpg/', $imgFn, $matches);
if (!$matches) {
    die('wrong format of the image file name ');
}
$p = $matches[1];
$line = $matches[2];

$ocrEng = getOcr('eng');
$ocrCht = getOcr('chi_tra');

$pdo = new PDO("sqlite:toufu.sq3");
$st = $pdo->prepare("UPDATE toufu SET ocr_eng=:eng, ocr_cht=:cht WHERE p=:p AND line=:line ");
$st->execute(array(
    'eng' => $ocrEng,
    'cht' => $ocrCht,
    'p' => $p,
    'line' => $line
));

echo "$p $line \n";
