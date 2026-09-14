<?php
declare(strict_types=1);

namespace Algorithms\Math;

function sieve(int $limit): array {
    if ($limit < 2) return [];
    $isPrime = array_fill(0, $limit + 1, true);
    $isPrime[0] = $isPrime[1] = false;

    for ($p = 2; $p * $p <= $limit; $p++) {
        if ($isPrime[$p]) {
            for ($i = $p * $p; $i <= $limit; $i += $p) {
                $isPrime[$i] = false;
            }
        }
    }

    $primes = [];
    for ($i = 2; $i <= $limit; $i++) {
        if ($isPrime[$i]) $primes[] = $i;
    }
    return $primes;
}
