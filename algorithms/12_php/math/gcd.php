<?php
declare(strict_types=1);

namespace Algorithms\Math;

function gcd(int $a, int $b): int {
    while ($b !== 0) {
        $temp = $b;
        $b = $a % $b;
        $a = $temp;
    }
    return $a;
}

function lcm(int $a, int $b): int {
    return (int) (($a / gcd($a, $b)) * $b);
}
