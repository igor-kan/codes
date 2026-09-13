func bfs(graph:[Int:[Int]], start:Int)->[Int]{
    var visited=Set<Int>(), queue=[start], order=[Int]()
    while !queue.isEmpty { let node=queue.removeFirst()
        guard visited.insert(node).inserted else { continue }
        order.append(node); queue+=graph[node,default:[]] }
    return order
}