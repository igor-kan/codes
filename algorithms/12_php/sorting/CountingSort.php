<?php
declare(strict_types=1);

namespace Algorithms\Sorting;

function countingSort(array $arr): array {
    if (count($arr) === 0) return [];
    $maxVal = max($arr);
    $count = array_fill(0, $maxVal + 1, 0);
    foreach ($arr as $x) $count[$x]++;
    for ($i = 1; $i <= $maxVal; $i++) $count[$i] += $count[$i - 1];
    $out = array_fill(0, count($arr), 0);
    foreach (array_reverse($arr) as $x) {
        $count[$x]--;
        $out[$count[$x]] = $x;
    }
    return $out;
}

if (php_sapi_name() === 'cli' && basename($_SERVER['SCRIPT_FILENAME'] ?? '') === basename(__FILE__)) {
    $data = [4, 2, 2, 8, 3, 3, 1];
    $sorted = countingSort($data);
    $expected = $data;
    sort($expected);
    if ($sorted !== $expected) {
        throw new \RuntimeException("CountingSort verification failed");
    }
    echo "[PHP CountingSort] Counting sort verified: " . json_encode($sorted) . "\n";
}
