<?php
declare(strict_types=1);

namespace Algorithms\Sorting;

function selectionSort(array $arr): array {
    $a = $arr;
    $n = count($a);
    for ($i = 0; $i < $n - 1; $i++) {
        $minIdx = $i;
        for ($j = $i + 1; $j < $n; $j++) {
            if ($a[$j] < $a[$minIdx]) $minIdx = $j;
        }
        [$a[$i], $a[$minIdx]] = [$a[$minIdx], $a[$i]];
    }
    return $a;
}

if (php_sapi_name() === 'cli' && basename($_SERVER['SCRIPT_FILENAME'] ?? '') === basename(__FILE__)) {
    $data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19];
    $sorted = selectionSort($data);
    $expected = $data;
    sort($expected);
    if ($sorted !== $expected) {
        throw new \RuntimeException("SelectionSort verification failed");
    }
    echo "[PHP SelectionSort] Selection sort verified: " . json_encode($sorted) . "\n";
}
