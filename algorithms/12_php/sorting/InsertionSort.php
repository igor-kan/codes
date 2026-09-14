<?php
declare(strict_types=1);

namespace Algorithms\Sorting;

function insertionSort(array $arr): array {
    $a = $arr;
    $n = count($a);
    for ($i = 1; $i < $n; $i++) {
        $key = $a[$i];
        $j = $i - 1;
        while ($j >= 0 && $a[$j] > $key) {
            $a[$j + 1] = $a[$j];
            $j--;
        }
        $a[$j + 1] = $key;
    }
    return $a;
}

if (php_sapi_name() === 'cli' && basename($_SERVER['SCRIPT_FILENAME'] ?? '') === basename(__FILE__)) {
    $data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19];
    $sorted = insertionSort($data);
    $expected = $data;
    sort($expected);
    if ($sorted !== $expected) {
        throw new \RuntimeException("InsertionSort verification failed");
    }
    echo "[PHP InsertionSort] Insertion sort verified: " . json_encode($sorted) . "\n";
}
