<?php
declare(strict_types=1);

namespace Algorithms\DynamicProgramming;

function lis(array $arr): int {
    $n = count($arr);
    if ($n === 0) return 0;
    $dp = array_fill(0, $n, 1);
    for ($i = 1; $i < $n; $i++) {
        for ($j = 0; $j < $i; $j++) {
            if ($arr[$j] < $arr[$i]) {
                $dp[$i] = max($dp[$i], $dp[$j] + 1);
            }
        }
    }
    return max($dp);
}

if (php_sapi_name() === 'cli' && basename($_SERVER['SCRIPT_FILENAME'] ?? '') === basename(__FILE__)) {
    if (lis([10, 9, 2, 5, 3, 7, 101, 18]) !== 4 || lis([]) !== 0) {
        throw new \RuntimeException("LIS verification failed");
    }
    echo "[PHP LIS] Longest increasing subsequence verified\n";
}
