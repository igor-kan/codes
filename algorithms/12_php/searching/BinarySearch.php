<?php
declare(strict_types=1);

namespace Algorithms\Searching;

function binarySearch(array $arr, int $target): int {
    $lo = 0;
    $hi = count($arr) - 1;
    while ($lo <= $hi) {
        $mid = intdiv($lo + $hi, 2);
        if ($arr[$mid] === $target) {
            return $mid;
        } elseif ($arr[$mid] < $target) {
            $lo = $mid + 1;
        } else {
            $hi = $mid - 1;
        }
    }
    return -1;
}

if (php_sapi_name() === 'cli' && basename($_SERVER['SCRIPT_FILENAME'] ?? '') === basename(__FILE__)) {
    $arr = [1, 3, 5, 7, 9, 11, 13];
    if (binarySearch($arr, 7) !== 3 || binarySearch($arr, 8) !== -1 || binarySearch($arr, 1) !== 0) {
        throw new \RuntimeException("BinarySearch verification failed");
    }
    echo "[PHP BinarySearch] Binary search verified\n";
}
