package graphs
func BFS(graph map[int][]int, start int) []int {
	visited:=map[int]bool{}; queue:=[]int{start}; order:=[]int{}
	for len(queue)>0 { node:=queue[0]; queue=queue[1:]
		if !visited[node] { visited[node]=true; order=append(order,node)
			queue=append(queue,graph[node]...) } }
	return order
}