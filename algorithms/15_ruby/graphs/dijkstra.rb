def dijkstra(graph, src)
  dist = Hash.new(Float::INFINITY); dist[src] = 0
  pq = [[0, src]]
  until pq.empty?
    d, u = pq.min_by { |x| x[0] }; pq.delete([d, u])
    next if d > dist[u]
    (graph[u] || []).each do |v, w|
      nd = d + w; if nd < dist[v]; dist[v] = nd; pq << [nd, v]; end
    end
  end
  dist
end