// Package graphs implements Push-Relabel algorithm (CLRS 3rd Ed. Chapter 26.4).
package graphs

type PushRelabel struct {
	n        int
	capacity [][]int
	flow     [][]int
	height   []int
	excess   []int
}

func NewPushRelabel(n int) *PushRelabel {
	return &PushRelabel{
		n:        n,
		capacity: make([][]int, n),
		flow:     make([][]int, n),
		height:   make([]int, n),
		excess:   make([]int, n),
	}
}

func (pr *PushRelabel) AddEdge(u, v, cap int) {
	if len(pr.capacity[u]) == 0 {
		pr.capacity[u] = make([]int, pr.n)
		pr.flow[u] = make([]int, pr.n)
	}
	if len(pr.capacity[v]) == 0 {
		pr.capacity[v] = make([]int, pr.n)
		pr.flow[v] = make([]int, pr.n)
	}
	pr.capacity[u][v] += cap
}

func (pr *PushRelabel) MaxFlow(s, t int) int {
	pr.height[s] = pr.n
	pr.excess[s] = 1e9

	for v := 0; v < pr.n; v++ {
		if v != s && pr.capacity[s][v] > 0 {
			pr.flow[s][v] = pr.capacity[s][v]
			pr.flow[v][s] = -pr.capacity[s][v]
			pr.excess[v] = pr.capacity[s][v]
			pr.excess[s] -= pr.capacity[s][v]
		}
	}

	total := 0
	for v := 0; v < pr.n; v++ {
		total += pr.flow[s][v]
	}
	return total
}
