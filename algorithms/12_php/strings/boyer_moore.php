<?php

// Boyer-Moore-Horspool substring search.
function boyer_moore(string $text, string $pattern): int
{
    $n = strlen($text);
    $m = strlen($pattern);
    $skip = array_fill(0, 256, $m);
    for ($i = 0; $i < $m - 1; $i++) {
        $skip[ord($pattern[$i])] = $m - 1 - $i;
    }
    $i = 0;
    while ($i + $m <= $n) {
        $j = $m - 1;
        while ($j >= 0 && $text[$i + $j] === $pattern[$j]) {
            $j--;
        }
        if ($j < 0) {
            return $i;
        }
        $i += $skip[ord($text[$i + $m - 1])];
    }
    return -1;
}

if (boyer_moore("here is a simple example", "example") !== 17) {
    throw new Exception("search failed");
}
if (boyer_moore("abc", "xyz") !== -1) {
    throw new Exception("search failed");
}
echo "boyer-moore ok\n";
