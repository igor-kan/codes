// Package graphs implements Hierholzer's Eulerian Path algorithm in Go.
package graphs

func Hierholzer(n int, adj [][]int) []int {
	graph := make([][]int, n)
	for i := range adj {
		graph[i] = append([]int{}, adj[i]...)
	}

	stack := []int{0}
	path := []int{}

	for len(stack) > 0 {
		u := stack[len(stack)-1]
		if len(graph[u]) > 0 {
			v := graph[u][len(graph[u])-1]
			graph[u] = graph[u][:len(graph[u])-1]
			stack = append(stack, v)
		} else {
			path = append(path, stack[len(stack)-1])
			stack = stack[:len(stack)-1]
		}
	}

	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
		path[i], path[j] = path[j], path[i]
	}
	return path
}
