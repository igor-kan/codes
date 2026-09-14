package main

import "fmt"

func kahnTopoSort(n int, edges [][2]int) ([]int, bool) {
	adj := make([][]int, n)
	indeg := make([]int, n)
	for _, e := range edges {
		adj[e[0]] = append(adj[e[0]], e[1])
		indeg[e[1]]++
	}
	q := []int{}
	for i := 0; i < n; i++ {
		if indeg[i] == 0 {
			q = append(q, i)
		}
	}
	order := []int{}
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		order = append(order, u)
		for _, v := range adj[u] {
			indeg[v]--
			if indeg[v] == 0 {
				q = append(q, v)
			}
		}
	}
	if len(order) != n {
		return nil, false
	}
	return order, true
}

func main() {
	edges := [][2]int{{5, 2}, {5, 0}, {4, 0}, {4, 1}, {2, 3}, {3, 1}}
	order, ok := kahnTopoSort(6, edges)
	if !ok {
		panic("Kahn: expected a DAG order")
	}
	pos := make([]int, 6)
	for i, u := range order {
		pos[u] = i
	}
	for _, e := range edges {
		if pos[e[0]] >= pos[e[1]] {
			panic("Kahn: invalid topological order")
		}
	}
	// Cyclic graph must be rejected.
	if _, ok := kahnTopoSort(3, [][2]int{{0, 1}, {1, 2}, {2, 0}}); ok {
		panic("Kahn: should have detected cycle")
	}
	fmt.Println("[Go Kahn] Topological sort verified:", order)
}
