<?php
declare(strict_types=1);

namespace Algorithms\Graphs;

use SplQueue;

function bfs(array $graph, int $start): array {
    $visited = [];
    $queue = new SplQueue();
    $order = [];

    $visited[$start] = true;
    $queue->enqueue($start);

    while (!$queue->isEmpty()) {
        $node = $queue->dequeue();
        $order[] = $node;

        foreach ($graph[$node] ?? [] as $neighbor) {
            if (!isset($visited[$neighbor])) {
                $visited[$neighbor] = true;
                $queue->enqueue($neighbor);
            }
        }
    }

    return $order;
}
