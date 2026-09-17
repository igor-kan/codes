// Package graphs implements Hopcroft-Karp algorithm in Go.
package graphs

type HopcroftKarp struct {
	nu, nv       int
	adj          [][]int
	pairU, pairV []int
	dist         []int
}

func NewHopcroftKarp(nu, nv int) *HopcroftKarp {
	return &HopcroftKarp{
		nu:    nu,
		nv:    nv,
		adj:   make([][]int, nu+1),
		pairU: make([]int, nu+1),
		pairV: make([]int, nv+1),
		dist:  make([]int, nu+1),
	}
}

func (hk *HopcroftKarp) AddEdge(u, v int) {
	hk.adj[u] = append(hk.adj[u], v)
}

func (hk *HopcroftKarp) MaxMatching() int {
	matching := 0
	for hk.bfs() {
		for u := 1; u <= hk.nu; u++ {
			if hk.pairU[u] == 0 && hk.dfs(u) {
				matching++
			}
		}
	}
	return matching
}

func (hk *HopcroftKarp) bfs() bool {
	queue := []int{}
	for u := 1; u <= hk.nu; u++ {
		if hk.pairU[u] == 0 {
			hk.dist[u] = 0
			queue = append(queue, u)
		} else {
			hk.dist[u] = 1e9
		}
	}
	hk.dist[0] = 1e9

	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		if hk.dist[u] < hk.dist[0] {
			for _, v := range hk.adj[u] {
				if hk.dist[hk.pairV[v]] == 1e9 {
					hk.dist[hk.pairV[v]] = hk.dist[u] + 1
					queue = append(queue, hk.pairV[v])
				}
			}
		}
	}
	return hk.dist[0] != 1e9
}

func (hk *HopcroftKarp) dfs(u int) bool {
	if u != 0 {
		for _, v := range hk.adj[u] {
			if hk.dist[hk.pairV[v]] == hk.dist[u]+1 && hk.dfs(hk.pairV[v]) {
				hk.pairV[v] = u
				hk.pairU[u] = v
				return true
			}
		}
		hk.dist[u] = 1e9
		return false
	}
	return true
}
