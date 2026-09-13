package graphs
func DFS(graph map[int][]int, start int) []int {
	visited:=map[int]bool{}; stack:=[]int{start}; order:=[]int{}
	for len(stack)>0 { n:=len(stack)-1; node:=stack[n]; stack=stack[:n]
		if !visited[node] { visited[node]=true; order=append(order,node)
			stack=append(stack,graph[node]...) } }
	return order
}