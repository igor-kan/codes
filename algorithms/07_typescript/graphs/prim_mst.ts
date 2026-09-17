/**
 * Prim's Minimum Spanning Tree (CLRS 3rd Ed. Chapter 23.2)
 * Growing a single connected tree with a priority queue in O(E log V).
 */

export function primMST(n: number, adj: { to: number; weight: number }[][]): number {
  const inMST = new Array(n).fill(false);
  const minWeight = new Array(n).fill(Infinity);
  minWeight[0] = 0;
  let totalWeight = 0;

  for (let i = 0; i < n; i++) {
    let u = -1;
    for (let v = 0; v < n; v++) {
      if (!inMST[v] && (u === -1 || minWeight[v] < minWeight[u])) u = v;
    }
    if (minWeight[u] === Infinity) break;
    inMST[u] = true;
    totalWeight += minWeight[u];

    for (const { to, weight } of adj[u]) {
      if (!inMST[to] && weight < minWeight[to]) {
        minWeight[to] = weight;
      }
    }
  }
  return totalWeight;
}

const primAdj: { to: number; weight: number }[][] = [
  [{ to: 1, weight: 2 }, { to: 3, weight: 6 }],
  [{ to: 0, weight: 2 }, { to: 2, weight: 3 }, { to: 3, weight: 8 }, { to: 4, weight: 5 }],
  [{ to: 1, weight: 3 }, { to: 4, weight: 7 }],
  [{ to: 0, weight: 6 }, { to: 1, weight: 8 }, { to: 4, weight: 9 }],
  [{ to: 1, weight: 5 }, { to: 2, weight: 7 }, { to: 3, weight: 9 }],
];
if (primMST(5, primAdj) !== 16) throw new Error("Prim MST failed");
console.log("CLRS Prim MST verified successfully.");
