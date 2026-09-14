<?php
declare(strict_types=1);

namespace Algorithms\Strings;

function zAlgorithm(string $s): array {
    $n = strlen($s);
    $z = array_fill(0, $n, 0);
    if ($n > 0) $z[0] = $n;
    $l = 0;
    $r = 0;
    for ($i = 1; $i < $n; $i++) {
        if ($i <= $r) $z[$i] = min($r - $i + 1, $z[$i - $l]);
        while ($i + $z[$i] < $n && $s[$z[$i]] === $s[$i + $z[$i]]) $z[$i]++;
        if ($i + $z[$i] - 1 > $r) {
            $l = $i;
            $r = $i + $z[$i] - 1;
        }
    }
    return $z;
}

if (php_sapi_name() === 'cli' && basename($_SERVER['SCRIPT_FILENAME'] ?? '') === basename(__FILE__)) {
    if (zAlgorithm("abacaba") !== [7, 0, 1, 0, 3, 0, 1]) {
        throw new \RuntimeException("ZAlgorithm verification failed");
    }
    echo "[PHP ZAlgorithm] Z-algorithm verified\n";
}
