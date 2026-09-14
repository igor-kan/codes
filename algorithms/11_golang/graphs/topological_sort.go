package main

import (
	"fmt"
)

type Edge struct {
	U, V int
}

func KahnsTopologicalSort(n int, edges []Edge) []int {
	adj := make([][]int, n)
	inDegree := make([]int, n)

	for _, e := range edges {
		adj[e.U] = append(adj[e.U], e.V)
		inDegree[e.V]++
	}

	queue := make([]int, 0)
	for i := 0; i < n; i++ {
		if inDegree[i] == 0 {
			queue = append(queue, i)
		}
	}

	order := make([]int, 0, n)
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		order = append(order, u)

		for _, v := range adj[u] {
			inDegree[v]--
			if inDegree[v] == 0 {
				queue = append(queue, v)
			}
		}
	}

	if len(order) != n {
		return nil // Cycle
	}
	return order
}

func main() {
	edges := []Edge{
		{5, 2}, {5, 0}, {4, 0}, {4, 1}, {2, 3}, {3, 1},
	}
	n := 6
	order := KahnsTopologicalSort(n, edges)
	if len(order) != n {
		panic("Invalid topological sort result")
	}

	pos := make(map[int]int)
	for i, node := range order {
		pos[node] = i
	}
	for _, e := range edges {
		if pos[e.U] >= pos[e.V] {
			panic(fmt.Sprintf("Topological order violation: %d before %d", e.U, e.V))
		}
	}

	fmt.Printf("[Go TopoSort] Valid ordering verified: %v\n", order)
}
