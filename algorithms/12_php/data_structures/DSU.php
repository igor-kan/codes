<?php
declare(strict_types=1);

namespace Algorithms\DataStructures;

class DSU {
    private array $parent;
    private array $rank;

    public function __construct(int $n) {
        $this->parent = range(0, $n - 1);
        $this->rank = array_fill(0, $n, 0);
    }

    public function find(int $x): int {
        if ($this->parent[$x] !== $x) {
            $this->parent[$x] = $this->find($this->parent[$x]);
        }
        return $this->parent[$x];
    }

    public function union(int $x, int $y): void {
        $rx = $this->find($x);
        $ry = $this->find($y);
        if ($rx === $ry) return;
        if ($this->rank[$rx] < $this->rank[$ry]) {
            $this->parent[$rx] = $ry;
        } elseif ($this->rank[$rx] > $this->rank[$ry]) {
            $this->parent[$ry] = $rx;
        } else {
            $this->parent[$ry] = $rx;
            $this->rank[$rx]++;
        }
    }

    public function connected(int $x, int $y): bool {
        return $this->find($x) === $this->find($y);
    }
}

if (php_sapi_name() === 'cli' && basename($_SERVER['SCRIPT_FILENAME'] ?? '') === basename(__FILE__)) {
    $dsu = new DSU(5);
    $dsu->union(0, 1);
    $dsu->union(1, 2);
    $dsu->union(3, 4);
    if (!$dsu->connected(0, 2) || $dsu->connected(0, 3)) {
        throw new \RuntimeException("DSU verification failed");
    }
    echo "[PHP DSU] Disjoint set union verified\n";
}
