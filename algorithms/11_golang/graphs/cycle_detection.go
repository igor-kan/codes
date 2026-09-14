package main

import "fmt"

const (
	white = 0
	gray  = 1
	black = 2
)

func hasCycle(n int, edges [][2]int) bool {
	adj := make([][]int, n)
	for _, e := range edges {
		adj[e[0]] = append(adj[e[0]], e[1])
	}
	color := make([]int, n)
	var dfs func(u int) bool
	dfs = func(u int) bool {
		color[u] = gray
		for _, v := range adj[u] {
			if color[v] == gray {
				return true
			}
			if color[v] == white && dfs(v) {
				return true
			}
		}
		color[u] = black
		return false
	}
	for s := 0; s < n; s++ {
		if color[s] == white && dfs(s) {
			return true
		}
	}
	return false
}

func main() {
	if !hasCycle(3, [][2]int{{0, 1}, {1, 2}, {2, 0}}) {
		panic("cycle detection: cycle should be found")
	}
	if hasCycle(4, [][2]int{{0, 1}, {1, 2}, {0, 2}, {2, 3}}) {
		panic("cycle detection: DAG should have no cycle")
	}
	fmt.Println("[Go CycleDetection] Directed cycle detection verified.")
}
