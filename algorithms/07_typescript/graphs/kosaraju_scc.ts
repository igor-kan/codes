/**
 * Kosaraju's SCC Algorithm (CLRS 3rd Ed. Chapter 22.5)
 * Two DFS passes on graph and transpose graph in O(V + E).
 */

export function kosarajuSCC(n: number, adj: number[][]): number[][] {
  const visited = new Array(n).fill(false);
  const order: number[] = [];

  function dfs1(v: number): void {
    visited[v] = true;
    for (const u of adj[v]) {
      if (!visited[u]) dfs1(u);
    }
    order.push(v);
  }

  for (let i = 0; i < n; i++) {
    if (!visited[i]) dfs1(i);
  }

  // Transpose graph
  const revAdj: number[][] = Array.from({ length: n }, () => []);
  for (let u = 0; u < n; u++) {
    for (const v of adj[u]) revAdj[v].push(u);
  }

  visited.fill(false);
  const sccs: number[][] = [];

  function dfs2(v: number, comp: number[]): void {
    visited[v] = true;
    comp.push(v);
    for (const u of revAdj[v]) {
      if (!visited[u]) dfs2(u, comp);
    }
  }

  while (order.length > 0) {
    const v = order.pop()!;
    if (!visited[v]) {
      const comp: number[] = [];
      dfs2(v, comp);
      sccs.push(comp);
    }
  }
  return sccs;
}

const kAdj: number[][] = [
  [1],
  [2],
  [0, 3],
  [4],
  [3],
];
const kRes = kosarajuSCC(5, kAdj);
if (kRes.length !== 2) throw new Error("Kosaraju SCC failed");
console.log("CLRS Kosaraju SCC verified successfully.");
