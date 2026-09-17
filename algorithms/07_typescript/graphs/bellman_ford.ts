/**
 * Bellman-Ford Algorithm (CLRS 3rd Ed. Chapter 24.1)
 * Computes single-source shortest paths on graphs with negative edge weights and detects negative-weight cycles.
 */

export interface Edge {
  u: number;
  v: number;
  weight: number;
}

export function bellmanFord(
  numVertices: number,
  edges: Edge[],
  source: number
): { distances: number[]; predecessors: (number | null)[]; hasNegativeCycle: boolean } {
  const distances = new Array(numVertices).fill(Infinity);
  const predecessors = new Array<number | null>(numVertices).fill(null);
  distances[source] = 0;

  for (let i = 1; i < numVertices; i++) {
    for (const { u, v, weight } of edges) {
      if (distances[u] !== Infinity && distances[u] + weight < distances[v]) {
        distances[v] = distances[u] + weight;
        predecessors[v] = u;
      }
    }
  }

  for (const { u, v, weight } of edges) {
    if (distances[u] !== Infinity && distances[u] + weight < distances[v]) {
      return { distances, predecessors, hasNegativeCycle: true };
    }
  }

  return { distances, predecessors, hasNegativeCycle: false };
}

const edges: Edge[] = [
  { u: 0, v: 1, weight: -1 },
  { u: 0, v: 2, weight: 4 },
  { u: 1, v: 2, weight: 3 },
  { u: 1, v: 3, weight: 2 },
  { u: 1, v: 4, weight: 2 },
  { u: 3, v: 2, weight: 5 },
  { u: 3, v: 1, weight: 1 },
  { u: 4, v: 3, weight: -3 },
];
const res = bellmanFord(5, edges, 0);
if (res.hasNegativeCycle || res.distances[3] !== -2) {
  throw new Error("Bellman-Ford verification failed");
}
console.log("CLRS Bellman-Ford verified successfully.");
