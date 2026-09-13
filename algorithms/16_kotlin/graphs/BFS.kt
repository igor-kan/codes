import java.util.LinkedList
fun bfs(graph: Map<Int,List<Int>>, start: Int): List<Int> {
    val visited = mutableSetOf<Int>(); val queue = LinkedList(listOf(start)); val order = mutableListOf<Int>()
    while (queue.isNotEmpty()) { val u=queue.poll(); if(visited.add(u)){order+=u; queue+=graph[u]?:emptyList()} }
    return order
}