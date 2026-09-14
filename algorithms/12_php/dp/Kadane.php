<?php
declare(strict_types=1);

namespace Algorithms\DynamicProgramming;

function kadane(array $arr): int {
    $best = $arr[0];
    $cur = $arr[0];
    for ($i = 1, $n = count($arr); $i < $n; $i++) {
        $cur = max($arr[$i], $cur + $arr[$i]);
        $best = max($best, $cur);
    }
    return $best;
}

if (php_sapi_name() === 'cli' && basename($_SERVER['SCRIPT_FILENAME'] ?? '') === basename(__FILE__)) {
    if (kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]) !== 6 || kadane([-5, -2, -3]) !== -2) {
        throw new \RuntimeException("Kadane verification failed");
    }
    echo "[PHP Kadane] Maximum subarray sum verified\n";
}
