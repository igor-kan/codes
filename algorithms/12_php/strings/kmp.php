<?php
declare(strict_types=1);

namespace Algorithms\Strings;

function computeLPS(string $pattern): array {
    $m = strlen($pattern);
    $lps = array_fill(0, $m, 0);
    $len = 0;
    $i = 1;

    while ($i < $m) {
        if ($pattern[$i] === $pattern[$len]) {
            $len++;
            $lps[$i] = $len;
            $i++;
        } elseif ($len > 0) {
            $len = $lps[$len - 1];
        } else {
            $lps[$i] = 0;
            $i++;
        }
    }

    return $lps;
}

function kmpSearch(string $text, string $pattern): array {
    $n = strlen($text);
    $m = strlen($pattern);
    if ($m === 0) return [0];

    $lps = computeLPS($pattern);
    $result = [];
    $i = 0;
    $j = 0;

    while ($i < $n) {
        if ($pattern[$j] === $text[$i]) {
            $i++;
            $j++;
        }

        if ($j === $m) {
            $result[] = $i - $j;
            $j = $lps[$j - 1];
        } elseif ($i < $n && $pattern[$j] !== $text[$i]) {
            if ($j > 0) {
                $j = $lps[$j - 1];
            } else {
                $i++;
            }
        }
    }

    return $result;
}

if (php_sapi_name() === 'cli' && basename($_SERVER['SCRIPT_FILENAME'] ?? '') === basename(__FILE__)) {
    echo "[PHP KMP] Testing KMP string matching\n";
    echo "Pattern at: " . json_encode(kmpSearch("ABABDABACDABABCABAB", "ABABCABAB")) . " (expected [10])\n";
    echo "Pattern at: " . json_encode(kmpSearch("AAAA", "AA")) . " (expected [0,1,2])\n";
    echo "Pattern at: " . json_encode(kmpSearch("HELLO WORLD", "WORLD")) . " (expected [6])\n";
    echo "[PHP KMP] Test completed.\n";
}