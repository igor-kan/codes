/**
 * Tarjan's Strongly Connected Components (CLRS 3rd Ed. Chapter 22 Problem)
 * Computes all maximal strongly connected components in single DFS pass in O(V + E).
 */

export function tarjanSCC(n: number, adj: number[][]): number[][] {
  const index = new Array(n).fill(-1);
  const lowlink = new Array(n).fill(-1);
  const onStack = new Array(n).fill(false);
  const stack: number[] = [];
  const sccs: number[][] = [];
  let curIndex = 0;

  function strongConnect(v: number): void {
    index[v] = curIndex;
    lowlink[v] = curIndex++;
    stack.push(v);
    onStack[v] = true;

    for (const w of adj[v]) {
      if (index[w] === -1) {
        strongConnect(w);
        lowlink[v] = Math.min(lowlink[v], lowlink[w]);
      } else if (onStack[w]) {
        lowlink[v] = Math.min(lowlink[v], index[w]);
      }
    }

    if (lowlink[v] === index[v]) {
      const scc: number[] = [];
      while (true) {
        const w = stack.pop()!;
        onStack[w] = false;
        scc.push(w);
        if (w === v) break;
      }
      sccs.push(scc);
    }
  }

  for (let i = 0; i < n; i++) {
    if (index[i] === -1) strongConnect(i);
  }
  return sccs;
}

const tAdj: number[][] = [
  [1],
  [2],
  [0, 3],
  [4],
  [5],
  [3],
];
const sccs = tarjanSCC(6, tAdj);
if (sccs.length !== 2) throw new Error("Tarjan SCC failed");
console.log("Tarjan SCC verified successfully.");
