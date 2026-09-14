function kahnTopologicalSort(n, edges) {
  const indeg = new Array(n).fill(0);
  const adj = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) { adj[u].push(v); indeg[v]++; }
  const q = [];
  for (let i = 0; i < n; i++) if (indeg[i] === 0) q.push(i);
  const order = [];
  while (q.length) {
    const u = q.shift();
    order.push(u);
    for (const v of adj[u]) if (--indeg[v] === 0) q.push(v);
  }
  return order.length === n ? order : [];
}

module.exports = { kahnTopologicalSort };

if (require.main === module) {
  const edges = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]];
  const order = kahnTopologicalSort(6, edges);
  if (order.length !== 6) throw new Error("topological sort failed");
  const pos = new Array(6);
  order.forEach((u, i) => (pos[u] = i));
  for (const [u, v] of edges) if (pos[u] >= pos[v]) throw new Error("invalid topological order");
  console.log("[JavaScript Kahn Topological Sort] Kahn's algorithm verified");
}
