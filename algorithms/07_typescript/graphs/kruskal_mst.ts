/**
 * Kruskal's Minimum Spanning Tree (CLRS 3rd Ed. Chapter 23.2)
 * Greedy algorithm utilizing Disjoint Set Forest (Union-Find) in O(E log E).
 */

class DSU {
  parent: number[];
  rank: number[];

  constructor(n: number) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = new Array(n).fill(0);
  }

  find(x: number): number {
    if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);
    return this.parent[x];
  }

  union(x: number, y: number): boolean {
    const rx = this.find(x);
    const ry = this.find(y);
    if (rx === ry) return false;
    if (this.rank[rx] < this.rank[ry]) this.parent[rx] = ry;
    else if (this.rank[rx] > this.rank[ry]) this.parent[ry] = rx;
    else {
      this.parent[ry] = rx;
      this.rank[rx]++;
    }
    return true;
  }
}

export interface WeightedEdge {
  u: number;
  v: number;
  weight: number;
}

export function kruskalMST(n: number, edges: WeightedEdge[]): { mst: WeightedEdge[]; totalWeight: number } {
  const sorted = [...edges].sort((a, b) => a.weight - b.weight);
  const dsu = new DSU(n);
  const mst: WeightedEdge[] = [];
  let totalWeight = 0;

  for (const edge of sorted) {
    if (dsu.union(edge.u, edge.v)) {
      mst.push(edge);
      totalWeight += edge.weight;
      if (mst.length === n - 1) break;
    }
  }
  return { mst, totalWeight };
}

const kEdges: WeightedEdge[] = [
  { u: 0, v: 1, weight: 4 },
  { u: 0, v: 2, weight: 4 },
  { u: 1, v: 2, weight: 2 },
  { u: 2, v: 3, weight: 3 },
  { u: 2, v: 4, weight: 2 },
  { u: 2, v: 5, weight: 4 },
  { u: 3, v: 4, weight: 3 },
  { u: 4, v: 5, weight: 3 },
];
const mstRes = kruskalMST(6, kEdges);
if (mstRes.totalWeight !== 14) throw new Error("Kruskal MST failed");
console.log("CLRS Kruskal MST verified successfully.");
