<?php
declare(strict_types=1);

namespace Algorithms\Graphs;

use SplPriorityQueue;

function dijkstra(array $graph, int $source): array {
    $distances = [$source => 0];
    $pq = new SplPriorityQueue();
    $pq->insert($source, 0);

    while (!$pq->isEmpty()) {
        $u = $pq->extract();
        $d = $distances[$u];

        foreach ($graph[$u] ?? [] as [$v, $weight]) {
            $newDist = $d + $weight;
            if (!isset($distances[$v]) || $newDist < $distances[$v]) {
                $distances[$v] = $newDist;
                $pq->insert($v, -$newDist);
            }
        }
    }

    return $distances;
}
