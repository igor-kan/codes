/**
 * Hierholzer's Algorithm
 * Finds an Eulerian path/circuit in a directed graph in linear O(V + E) time.
 */

export function hierholzerEulerianPath(n: number, adj: number[][]): number[] | null {
  const inDegree = new Array(n).fill(0);
  const outDegree = new Array(n).fill(0);
  const graph = adj.map((list) => [...list]);

  for (let u = 0; u < n; u++) {
    outDegree[u] = graph[u].length;
    for (const v of graph[u]) inDegree[v]++;
  }

  let startNode = 0;
  let startNodes = 0;
  let endNodes = 0;

  for (let i = 0; i < n; i++) {
    if (outDegree[i] - inDegree[i] === 1) {
      startNode = i;
      startNodes++;
    } else if (inDegree[i] - outDegree[i] === 1) {
      endNodes++;
    } else if (inDegree[i] !== outDegree[i]) {
      return null;
    }
  }

  if (!((startNodes === 0 && endNodes === 0) || (startNodes === 1 && endNodes === 1))) {
    return null;
  }

  const stack: number[] = [startNode];
  const path: number[] = [];

  while (stack.length > 0) {
    const u = stack[stack.length - 1];
    if (graph[u].length > 0) {
      const next = graph[u].pop()!;
      stack.push(next);
    } else {
      path.push(stack.pop()!);
    }
  }
  return path.reverse();
}

const eulerAdj: number[][] = [
  [1],
  [2],
  [0, 3],
  [0],
];
const ePath = hierholzerEulerianPath(4, eulerAdj);
if (!ePath || ePath.length !== 6) throw new Error("Hierholzer algorithm failed");
console.log("Hierholzer Eulerian Circuit verified successfully.");
