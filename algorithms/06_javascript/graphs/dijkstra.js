function dijkstra(graph, src) {
  const dist = {[src]:0}, visited = new Set();
  const pq = [[0, src]];
  while (pq.length) {
    pq.sort((a,b)=>a[0]-b[0]);
    const [d, u] = pq.shift();
    if (visited.has(u)) continue; visited.add(u);
    for (const [v,w] of (graph[u]||[])) {
      const nd = d+w; if (nd < (dist[v]??Infinity)) { dist[v]=nd; pq.push([nd,v]); }
    }
  }
  return dist;
}
module.exports = { dijkstra };