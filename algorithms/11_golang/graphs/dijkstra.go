package graphs
import "container/heap"
type Item struct{node,dist int}
type PQ []Item
func(p PQ)Len()int{return len(p)}; func(p PQ)Less(i,j int)bool{return p[i].dist<p[j].dist}
func(p PQ)Swap(i,j int){p[i],p[j]=p[j],p[i]}
func(p*PQ)Push(x interface{}){*p=append(*p,x.(Item))}
func(p*PQ)Pop()interface{}{old:=*p;n:=len(old);x:=old[n-1];*p=old[:n-1];return x}
func Dijkstra(graph map[int][]Item, src int) map[int]int {
	dist:=map[int]int{src:0}; pq:=&PQ{{src,0}}; heap.Init(pq)
	for pq.Len()>0 { cur:=heap.Pop(pq).(Item)
		for _,nb:=range graph[cur.node] { nd:=cur.dist+nb.dist
			if d,ok:=dist[nb.node];!ok||nd<d { dist[nb.node]=nd; heap.Push(pq,Item{nb.node,nd}) } } }
	return dist
}