def bfs(graph, start)
  visited = {}; queue = [start]; order = []
  while !queue.empty?
    node = queue.shift
    next if visited[node]
    visited[node] = true; order << node
    queue += (graph[node] || [])
  end
  order
end