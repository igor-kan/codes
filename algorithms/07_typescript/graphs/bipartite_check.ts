export function isBipartite(n: number, edges: number[][]): boolean {
  const adj: number[][] = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) { adj[u].push(v); adj[v].push(u); }
  const color: number[] = new Array(n).fill(-1);
  for (let s = 0; s < n; s++) {
    if (color[s] !== -1) continue;
    color[s] = 0;
    const q: number[] = [s];
    while (q.length) {
      const u = q.shift() as number;
      for (const v of adj[u]) {
        if (color[v] === -1) { color[v] = color[u] ^ 1; q.push(v); }
        else if (color[v] === color[u]) return false;
      }
    }
  }
  return true;
}

if (!isBipartite(4, [[0, 1], [0, 3], [1, 2], [2, 3]])) throw new Error("Bipartite check failed");
if (isBipartite(3, [[0, 1], [1, 2], [2, 0]])) throw new Error("Odd cycle should not be bipartite");
console.log("[TypeScript Bipartite Check] BFS 2-coloring verified");
