// Bellman-Ford shortest paths with negative edge support.
package main

import "fmt"

const inf = 1 << 60

type edge struct {
	from, to, weight int
}

func bellmanFord(n int, edges []edge, source int) ([]int, bool) {
	dist := make([]int, n)
	for i := range dist {
		dist[i] = inf
	}
	dist[source] = 0
	for iter := 0; iter < n-1; iter++ {
		for _, e := range edges {
			if dist[e.from] != inf && dist[e.from]+e.weight < dist[e.to] {
				dist[e.to] = dist[e.from] + e.weight
			}
		}
	}
	for _, e := range edges {
		if dist[e.from] != inf && dist[e.from]+e.weight < dist[e.to] {
			return nil, false
		}
	}
	return dist, true
}

func main() {
	edges := []edge{{0, 1, 4}, {0, 2, 5}, {1, 2, -3}, {2, 3, 2}}
	dist, ok := bellmanFord(4, edges, 0)
	if !ok {
		panic("unexpected negative cycle")
	}
	fmt.Println(dist)
}
