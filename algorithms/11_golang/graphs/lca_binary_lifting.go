package main

import "fmt"

type LCA struct {
	up    [][]int
	depth []int
	log   int
}

func NewLCA(adj [][]int, root int) *LCA {
	n := len(adj)
	log := 0
	for 1<<log <= n {
		log++
	}
	up := make([][]int, n)
	for i := range up {
		up[i] = make([]int, log)
	}
	depth := make([]int, n)
	var dfs func(u, p int)
	dfs = func(u, p int) {
		up[u][0] = p
		for k := 1; k < log; k++ {
			up[u][k] = up[up[u][k-1]][k-1]
		}
		for _, v := range adj[u] {
			if v != p {
				depth[v] = depth[u] + 1
				dfs(v, u)
			}
		}
	}
	dfs(root, root)
	return &LCA{up: up, depth: depth, log: log}
}

func (l *LCA) Query(a, b int) int {
	if l.depth[a] < l.depth[b] {
		a, b = b, a
	}
	diff := l.depth[a] - l.depth[b]
	for k := 0; k < l.log; k++ {
		if diff&(1<<k) != 0 {
			a = l.up[a][k]
		}
	}
	if a == b {
		return a
	}
	for k := l.log - 1; k >= 0; k-- {
		if l.up[a][k] != l.up[b][k] {
			a = l.up[a][k]
			b = l.up[b][k]
		}
	}
	return l.up[a][0]
}

func main() {
	adj := [][]int{
		{1, 2},
		{0, 3, 4},
		{0, 5, 6},
		{1}, {1}, {2}, {2},
	}
	l := NewLCA(adj, 0)
	if l.Query(3, 4) != 1 || l.Query(3, 6) != 0 || l.Query(5, 6) != 2 {
		panic("LCA: query mismatch")
	}
	fmt.Println("[Go LCA] Binary lifting verified.")
}
