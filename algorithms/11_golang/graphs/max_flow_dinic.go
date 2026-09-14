package main

import "fmt"

type Dinic struct {
	adj  [][]int
	to   []int
	cap  []int
	dist []int
	ptr  []int
}

func NewDinic(n int) *Dinic {
	return &Dinic{
		adj:  make([][]int, n),
		dist: make([]int, n),
		ptr:  make([]int, n),
	}
}

func (d *Dinic) AddEdge(u, v, c int) {
	d.adj[u] = append(d.adj[u], len(d.to))
	d.to = append(d.to, v)
	d.cap = append(d.cap, c)
	d.adj[v] = append(d.adj[v], len(d.to))
	d.to = append(d.to, u)
	d.cap = append(d.cap, 0)
}

func (d *Dinic) bfs(s, t int) bool {
	for i := range d.dist {
		d.dist[i] = -1
	}
	d.dist[s] = 0
	q := []int{s}
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		for _, eid := range d.adj[u] {
			v := d.to[eid]
			if d.dist[v] == -1 && d.cap[eid] > 0 {
				d.dist[v] = d.dist[u] + 1
				q = append(q, v)
			}
		}
	}
	return d.dist[t] != -1
}

func (d *Dinic) dfs(u, t, f int) int {
	if u == t || f == 0 {
		return f
	}
	for ; d.ptr[u] < len(d.adj[u]); d.ptr[u]++ {
		eid := d.adj[u][d.ptr[u]]
		v := d.to[eid]
		if d.dist[v] != d.dist[u]+1 || d.cap[eid] == 0 {
			continue
		}
		pushed := d.dfs(v, t, min(f, d.cap[eid]))
		if pushed > 0 {
			d.cap[eid] -= pushed
			d.cap[eid^1] += pushed
			return pushed
		}
	}
	return 0
}

func (d *Dinic) MaxFlow(s, t int) int {
	flow := 0
	for d.bfs(s, t) {
		for i := range d.ptr {
			d.ptr[i] = 0
		}
		for {
			f := d.dfs(s, t, 1<<60)
			if f == 0 {
				break
			}
			flow += f
		}
	}
	return flow
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	d := NewDinic(6)
	d.AddEdge(0, 1, 16)
	d.AddEdge(0, 2, 13)
	d.AddEdge(1, 2, 10)
	d.AddEdge(1, 3, 12)
	d.AddEdge(2, 1, 4)
	d.AddEdge(2, 4, 14)
	d.AddEdge(3, 2, 9)
	d.AddEdge(3, 5, 20)
	d.AddEdge(4, 3, 7)
	d.AddEdge(4, 5, 4)
	if d.MaxFlow(0, 5) != 23 {
		panic("Dinic: max flow should be 23")
	}
	fmt.Println("[Go Dinic] Max flow verified: 23")
}
