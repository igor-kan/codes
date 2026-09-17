/**
 * Bridges and Articulation Points (Hopcroft-Tarjan Algorithm)
 * Discovers cut edges and cut vertices of undirected graphs in O(V + E).
 */

export function findBridgesAndArticulationPoints(
  n: number,
  adj: number[][]
): { bridges: [number, number][]; articulationPoints: number[] } {
  const visited = new Array(n).fill(false);
  const tin = new Array(n).fill(-1);
  const low = new Array(n).fill(-1);
  let timer = 0;
  const bridges: [number, number][] = [];
  const isAP = new Array(n).fill(false);

  function dfs(v: number, p = -1): void {
    visited[v] = true;
    tin[v] = low[v] = timer++;
    let children = 0;

    for (const to of adj[v]) {
      if (to === p) continue;
      if (visited[to]) {
        low[v] = Math.min(low[v], tin[to]);
      } else {
        dfs(to, v);
        low[v] = Math.min(low[v], low[to]);
        if (low[to] > tin[v]) bridges.push([v, to]);
        if (low[to] >= tin[v] && p !== -1) isAP[v] = true;
        children++;
      }
    }
    if (p === -1 && children > 1) isAP[v] = true;
  }

  for (let i = 0; i < n; i++) {
    if (!visited[i]) dfs(i);
  }

  const articulationPoints: number[] = [];
  for (let i = 0; i < n; i++) {
    if (isAP[i]) articulationPoints.push(i);
  }
  return { bridges, articulationPoints };
}

const bAdj: number[][] = [
  [1, 2],
  [0, 2, 3],
  [0, 1],
  [1, 4],
  [3],
];
const bRes = findBridgesAndArticulationPoints(5, bAdj);
if (bRes.bridges.length !== 2 || !bRes.articulationPoints.includes(1)) {
  throw new Error("Bridges and Articulation Points failed");
}
console.log("Bridges and Articulation Points verified successfully.");
