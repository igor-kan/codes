package main

import (
	"container/heap"
	"fmt"
	"math"
)

type Edge struct {
	To     int
	Weight float64
}

type Item struct {
	node     int
	priority float64
	index    int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int           { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].priority < pq[j].priority }
func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}
func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}
func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil
	item.index = -1
	*pq = old[0 : n-1]
	return item
}

func Dijkstra(n int, adj [][]Edge, source int) []float64 {
	dist := make([]float64, n)
	for i := range dist {
		dist[i] = math.Inf(1)
	}
	dist[source] = 0.0

	pq := make(PriorityQueue, 0)
	heap.Init(&pq)
	heap.Push(&pq, &Item{node: source, priority: 0.0})

	for pq.Len() > 0 {
		top := heap.Pop(&pq).(*Item)
		u := top.node
		d := top.priority

		if d > dist[u] {
			continue
		}

		for _, edge := range adj[u] {
			if dist[u]+edge.Weight < dist[edge.To] {
				dist[edge.To] = dist[u] + edge.Weight
				heap.Push(&pq, &Item{node: edge.To, priority: dist[edge.To]})
			}
		}
	}
	return dist
}

func main() {
	adj := make([][]Edge, 4)
	adj[0] = []Edge{{To: 1, Weight: 4.0}, {To: 2, Weight: 1.0}}
	adj[2] = []Edge{{To: 1, Weight: 2.0}, {To: 3, Weight: 5.0}}
	adj[1] = []Edge{{To: 3, Weight: 1.0}}

	dist := Dijkstra(4, adj, 0)
	if dist[3] != 4.0 {
		panic("Dijkstra failed")
	}
	fmt.Println("[Go Dijkstra] Shortest path 0 -> 3: 4.0 verified.")
}
