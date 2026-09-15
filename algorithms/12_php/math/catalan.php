<?php

// Catalan numbers by the recurrence.
$catalan = array_fill(0, 11, 0);
$catalan[0] = 1;
for ($i = 1; $i <= 10; $i++) {
    $sum = 0;
    for ($j = 0; $j < $i; $j++) {
        $sum += $catalan[$j] * $catalan[$i - 1 - $j];
    }
    $catalan[$i] = $sum;
}
if ($catalan[5] !== 42 || $catalan[10] !== 16796) {
    throw new Exception("wrong Catalan numbers");
}
echo "catalan(10)={$catalan[10]}\n";
