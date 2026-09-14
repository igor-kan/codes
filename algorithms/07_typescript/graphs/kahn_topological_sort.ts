export function kahnTopologicalSort(n: number, edges: number[][]): number[] {
  const indeg: number[] = new Array(n).fill(0);
  const adj: number[][] = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) { adj[u].push(v); indeg[v]++; }
  const q: number[] = [];
  for (let i = 0; i < n; i++) if (indeg[i] === 0) q.push(i);
  const order: number[] = [];
  while (q.length) {
    const u = q.shift() as number;
    order.push(u);
    for (const v of adj[u]) if (--indeg[v] === 0) q.push(v);
  }
  return order.length === n ? order : [];
}

const edges = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]];
const order = kahnTopologicalSort(6, edges);
if (order.length !== 6) throw new Error("Topological sort failed");
console.log("[TypeScript Kahn Topological Sort] Kahn's algorithm verified");
