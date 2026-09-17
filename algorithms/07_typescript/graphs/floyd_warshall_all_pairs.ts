/**
 * Floyd-Warshall Algorithm (CLRS 3rd Ed. Chapter 25.2)
 * All-pairs shortest paths via dynamic programming in O(V^3).
 */

export function floydWarshall(matrix: number[][]): number[][] {
  const n = matrix.length;
  const dist = matrix.map((row) => [...row]);

  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (dist[i][k] + dist[k][j] < dist[i][j]) {
          dist[i][j] = dist[i][k] + dist[k][j];
        }
      }
    }
  }
  return dist;
}

const INF = 1e9;
const initialGraph = [
  [0, 3, 8, INF, -4],
  [INF, 0, INF, 1, 7],
  [INF, 4, 0, INF, INF],
  [2, INF, -5, 0, INF],
  [INF, INF, INF, 6, 0],
];
const resFW = floydWarshall(initialGraph);
if (resFW[0][2] !== -1) throw new Error("Floyd-Warshall failed");
console.log("CLRS Floyd-Warshall verified successfully.");
