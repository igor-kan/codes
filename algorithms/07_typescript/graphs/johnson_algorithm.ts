/**
 * Johnson's Algorithm for Sparse Graphs (CLRS 3rd Ed. Chapter 25.3)
 * Reweight edges using Bellman-Ford, then run Dijkstra from all vertices in O(V^2 log V + VE).
 */

interface AdjEdge {
  to: number;
  weight: number;
}

export function johnsonAllPairs(n: number, edges: { u: number; v: number; weight: number }[]): number[][] | null {
  // Add extra vertex s = n with 0-weight edges to all vertices
  const bfEdges = [...edges];
  for (let i = 0; i < n; i++) bfEdges.push({ u: n, v: i, weight: 0 });

  const h = new Array(n + 1).fill(Infinity);
  h[n] = 0;
  for (let iter = 0; iter < n; iter++) {
    for (const { u, v, weight } of bfEdges) {
      if (h[u] !== Infinity && h[u] + weight < h[v]) {
        h[v] = h[u] + weight;
      }
    }
  }
  for (const { u, v, weight } of bfEdges) {
    if (h[u] !== Infinity && h[u] + weight < h[v]) return null; // Negative cycle
  }

  // Reweight graph
  const reweightedAdj: AdjEdge[][] = Array.from({ length: n }, () => []);
  for (const { u, v, weight } of edges) {
    reweightedAdj[u].push({ to: v, weight: weight + h[u] - h[v] });
  }

  const allDist: number[][] = [];
  for (let u = 0; u < n; u++) {
    const d = new Array(n).fill(Infinity);
    d[u] = 0;
    const visited = new Array(n).fill(false);
    for (let i = 0; i < n; i++) {
      let minNode = -1;
      for (let j = 0; j < n; j++) {
        if (!visited[j] && (minNode === -1 || d[j] < d[minNode])) minNode = j;
      }
      if (d[minNode] === Infinity) break;
      visited[minNode] = true;
      for (const { to, weight } of reweightedAdj[minNode]) {
        if (d[minNode] + weight < d[to]) d[to] = d[minNode] + weight;
      }
    }
    // Restore original distances
    for (let v = 0; v < n; v++) {
      if (d[v] !== Infinity) d[v] = d[v] - h[u] + h[v];
    }
    allDist.push(d);
  }
  return allDist;
}

const jEdges = [
  { u: 0, v: 1, weight: -2 },
  { u: 1, v: 2, weight: -1 },
  { u: 2, v: 0, weight: 4 },
];
const jDist = johnsonAllPairs(3, jEdges);
if (!jDist || jDist[0][2] !== -3) throw new Error("Johnson's algorithm failed");
console.log("CLRS Johnson's Algorithm verified successfully.");
