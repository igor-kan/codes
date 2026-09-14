function isBipartite(n, edges) {
  const adj = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) { adj[u].push(v); adj[v].push(u); }
  const color = new Array(n).fill(-1);
  for (let s = 0; s < n; s++) {
    if (color[s] !== -1) continue;
    color[s] = 0;
    const q = [s];
    while (q.length) {
      const u = q.shift();
      for (const v of adj[u]) {
        if (color[v] === -1) { color[v] = color[u] ^ 1; q.push(v); }
        else if (color[v] === color[u]) return false;
      }
    }
  }
  return true;
}

module.exports = { isBipartite };

if (require.main === module) {
  if (!isBipartite(4, [[0, 1], [0, 3], [1, 2], [2, 3]])) throw new Error("bipartite check failed");
  if (isBipartite(3, [[0, 1], [1, 2], [2, 0]])) throw new Error("odd cycle should not be bipartite");
  console.log("[JavaScript Bipartite Check] BFS 2-coloring verified");
}
