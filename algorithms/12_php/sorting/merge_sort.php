<?php
declare(strict_types=1);

namespace Algorithms\Sorting;

function mergeSort(array $arr): array {
    if (count($arr) <= 1) return $arr;
    $mid = intdiv(count($arr), 2);
    $left = mergeSort(array_slice($arr, 0, $mid));
    $right = mergeSort(array_slice($arr, $mid));
    
    $res = [];
    $i = $j = 0;
    while ($i < count($left) && $j < count($right)) {
        if ($left[$i] <= $right[$j]) {
            $res[] = $left[$i++];
        } else {
            $res[] = $right[$j++];
        }
    }
    return array_merge($res, array_slice($left, $i), array_slice($right, $j));
}
