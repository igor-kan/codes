function buildLCA(n, edges, root) {
  const LOG = Math.ceil(Math.log2(n)) + 1;
  const adj = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) { adj[u].push(v); adj[v].push(u); }
  const up = Array.from({ length: n }, () => new Array(LOG).fill(-1));
  const depth = new Array(n).fill(0);
  const parent = new Array(n).fill(-1);
  const seen = new Array(n).fill(false);
  const stack = [root];
  seen[root] = true;
  parent[root] = root;
  while (stack.length) {
    const u = stack.pop();
    for (const v of adj[u]) {
      if (!seen[v]) {
        seen[v] = true;
        parent[v] = u;
        depth[v] = depth[u] + 1;
        stack.push(v);
      }
    }
  }
  for (let i = 0; i < n; i++) up[i][0] = parent[i];
  for (let j = 1; j < LOG; j++)
    for (let i = 0; i < n; i++)
      up[i][j] = up[up[i][j - 1]][j - 1];

  function lca(a, b) {
    if (depth[a] < depth[b]) [a, b] = [b, a];
    let diff = depth[a] - depth[b];
    for (let j = 0; j < LOG; j++) if (diff & (1 << j)) a = up[a][j];
    if (a === b) return a;
    for (let j = LOG - 1; j >= 0; j--) {
      if (up[a][j] !== up[b][j]) { a = up[a][j]; b = up[b][j]; }
    }
    return up[a][0];
  }

  return { lca, depth, up };
}

module.exports = { buildLCA };

if (require.main === module) {
  const edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]];
  const { lca } = buildLCA(6, edges, 0);
  if (lca(3, 4) !== 1) throw new Error("LCA failed");
  if (lca(3, 5) !== 0) throw new Error("LCA failed");
  if (lca(3, 1) !== 1) throw new Error("LCA failed");
  console.log("[JavaScript LCA] Binary lifting LCA verified");
}
