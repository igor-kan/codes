<?php
declare(strict_types=1);

namespace Algorithms\Strings;

function manacher(string $s): int {
    $t = "#" . implode("#", str_split($s)) . "#";
    $n = strlen($t);
    $p = array_fill(0, $n, 0);
    $c = 0;
    $r = 0;
    for ($i = 0; $i < $n; $i++) {
        if ($i < $r) $p[$i] = min($r - $i, $p[2 * $c - $i]);
        while ($i + $p[$i] + 1 < $n && $i - $p[$i] - 1 >= 0 &&
               $t[$i + $p[$i] + 1] === $t[$i - $p[$i] - 1]) {
            $p[$i]++;
        }
        if ($i + $p[$i] > $r) {
            $c = $i;
            $r = $i + $p[$i];
        }
    }
    return max($p);
}

if (php_sapi_name() === 'cli' && basename($_SERVER['SCRIPT_FILENAME'] ?? '') === basename(__FILE__)) {
    if (manacher("abba") !== 4 || manacher("racecar") !== 7) {
        throw new \RuntimeException("Manacher verification failed");
    }
    echo "[PHP Manacher] Longest palindromic substring verified\n";
}
