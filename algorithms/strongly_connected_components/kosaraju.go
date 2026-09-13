package main

import "fmt"

type Kosaraju struct {
	n      int
	adj    [][]int
	revAdj [][]int
}

func NewKosaraju(n int) *Kosaraju {
	return &Kosaraju{
		n:      n,
		adj:    make([][]int, n),
		revAdj: make([][]int, n),
	}
}

func (k *Kosaraju) AddEdge(u, v int) {
	k.adj[u] = append(k.adj[u], v)
	k.revAdj[v] = append(k.revAdj[v], u)
}

func (k *Kosaraju) FindSCCs() [][]int {
	visited := make([]bool, k.n)
	var order []int

	var dfs1 func(u int)
	dfs1 = func(u int) {
		visited[u] = true
		for _, v := range k.adj[u] {
			if !visited[v] {
				dfs1(v)
			}
		}
		order = append(order, u)
	}

	for i := 0; i < k.n; i++ {
		if !visited[i] {
			dfs1(i)
		}
	}

	visited = make([]bool, k.n)
	var sccs [][]int

	var dfs2 func(u int, comp *[]int)
	dfs2 = func(u int, comp *[]int) {
		visited[u] = true
		*comp = append(*comp, u)
		for _, v := range k.revAdj[u] {
			if !visited[v] {
				dfs2(v, comp)
			}
		}
	}

	for i := len(order) - 1; i >= 0; i-- {
		u := order[i]
		if !visited[u] {
			var comp []int
			dfs2(u, &comp)
			sccs = append(sccs, comp)
		}
	}
	return sccs
}

func main() {
	g := NewKosaraju(5)
	g.AddEdge(1, 0)
	g.AddEdge(0, 2)
	g.AddEdge(2, 1)
	g.AddEdge(0, 3)
	g.AddEdge(3, 4)

	sccs := g.FindSCCs()
	if len(sccs) != 3 {
		panic("SCC count mismatch")
	}
	fmt.Println("[Go SCC] Kosaraju found components:", len(sccs))
}
