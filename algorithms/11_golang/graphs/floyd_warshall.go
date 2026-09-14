// All-pairs shortest paths (Floyd-Warshall).
package main

import "fmt"

const inf = 1 << 30

func floydWarshall(dist [][]int) [][]int {
	n := len(dist)
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if dist[i][k]+dist[k][j] < dist[i][j] {
					dist[i][j] = dist[i][k] + dist[k][j]
				}
			}
		}
	}
	return dist
}

func main() {
	graph := [][]int{
		{0, 3, inf, 7},
		{8, 0, 2, inf},
		{5, inf, 0, 1},
		{2, inf, inf, 0},
	}
	dist := floydWarshall(graph)
	if dist[0][2] != 5 || dist[0][3] != 6 {
		panic("wrong distance")
	}
	fmt.Println(dist[0])
}
