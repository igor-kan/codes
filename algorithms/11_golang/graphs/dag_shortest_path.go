package main

import "fmt"

type edge struct{ to, weight int }

func main() {
	adj := make([][]edge, 6)
	add := func(u, v, w int) { adj[u] = append(adj[u], edge{v, w}) }
	add(0, 1, 5)
	add(0, 2, 3)
	add(1, 2, 2)
	add(1, 3, 6)
	add(2, 3, 7)
	add(2, 4, 4)
	add(2, 5, 2)
	add(3, 4, -1)
	add(3, 5, 1)
	add(4, 5, -2)

	indegree := make([]int, 6)
	for u := range adj {
		for _, e := range adj[u] {
			indegree[e.to]++
		}
	}
	queue := []int{}
	for i, d := range indegree {
		if d == 0 {
			queue = append(queue, i)
		}
	}
	var order []int
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		order = append(order, u)
		for _, e := range adj[u] {
			indegree[e.to]--
			if indegree[e.to] == 0 {
				queue = append(queue, e.to)
			}
		}
	}
	const inf = 1 << 30
	dist := make([]int, 6)
	for i := range dist {
		dist[i] = inf
	}
	dist[0] = 0
	for _, u := range order {
		if dist[u] == inf {
			continue
		}
		for _, e := range adj[u] {
			if dist[u]+e.weight < dist[e.to] {
				dist[e.to] = dist[u] + e.weight
			}
		}
	}
	if dist[3] != 10 || dist[4] != 7 || dist[5] != 5 {
		panic("dag shortest path mismatch")
	}
	fmt.Println("dag shortest path ok")
}
