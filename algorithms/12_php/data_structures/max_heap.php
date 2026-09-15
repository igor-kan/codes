<?php

// Binary max-heap.
function push_heap(array &$a, int $v): void
{
    $a[] = $v;
    $i = count($a) - 1;
    while ($i > 0) {
        $p = intdiv($i - 1, 2);
        if ($a[$p] >= $a[$i]) {
            break;
        }
        [$a[$p], $a[$i]] = [$a[$i], $a[$p]];
        $i = $p;
    }
}

function pop_heap(array &$a): int
{
    $top = $a[0];
    $last = array_pop($a);
    if (count($a) > 0) {
        $a[0] = $last;
        $i = 0;
        while (true) {
            $l = 2 * $i + 1;
            $r = 2 * $i + 2;
            $b = $i;
            if ($l < count($a) && $a[$l] > $a[$b]) {
                $b = $l;
            }
            if ($r < count($a) && $a[$r] > $a[$b]) {
                $b = $r;
            }
            if ($b === $i) {
                break;
            }
            [$a[$i], $a[$b]] = [$a[$b], $a[$i]];
            $i = $b;
        }
    }
    return $top;
}

$a = [];
foreach ([5, 3, 8, 1, 4] as $v) {
    push_heap($a, $v);
}
$prev = PHP_INT_MAX;
while (count($a) > 0) {
    $x = pop_heap($a);
    if ($x > $prev) {
        throw new Exception("not a max-heap order");
    }
    $prev = $x;
}
echo "max heap ok\n";
