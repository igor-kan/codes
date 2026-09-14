function hasCycle(n, edges) {
  const adj = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) adj[u].push(v);
  const WHITE = 0, GRAY = 1, BLACK = 2;
  const color = new Array(n).fill(WHITE);
  function dfs(u) {
    color[u] = GRAY;
    for (const v of adj[u]) {
      if (color[v] === GRAY) return true;
      if (color[v] === WHITE && dfs(v)) return true;
    }
    color[u] = BLACK;
    return false;
  }
  for (let i = 0; i < n; i++) if (color[i] === WHITE && dfs(i)) return true;
  return false;
}

module.exports = { hasCycle };

if (require.main === module) {
  if (!hasCycle(3, [[0, 1], [1, 2], [2, 0]])) throw new Error("cycle not detected");
  if (hasCycle(4, [[0, 1], [1, 2], [2, 3]])) throw new Error("DAG flagged as cyclic");
  console.log("[JavaScript Cycle Detection] Directed graph cycle detection verified");
}
