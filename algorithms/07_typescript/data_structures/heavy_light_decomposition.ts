/**
 * Heavy-Light Decomposition (HLD)
 * Decomposes a tree into disjoint heavy chains for O(log^2 n) path queries.
 */

export class HeavyLightDecomposition {
  private n: number;
  private adj: number[][];
  private parent: number[];
  private depth: number[];
  private heavy: number[];
  private head: number[];
  private pos: number[];
  private curPos = 0;

  constructor(n: number, edges: [number, number][]) {
    this.n = n;
    this.adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
      this.adj[u].push(v);
      this.adj[v].push(u);
    }
    this.parent = new Array(n).fill(-1);
    this.depth = new Array(n).fill(0);
    this.heavy = new Array(n).fill(-1);
    this.head = new Array(n).fill(0);
    this.pos = new Array(n).fill(0);

    this.dfs(0, -1);
    this.decompose(0, 0);
  }

  private dfs(v: number, p: number): number {
    let size = 1;
    let maxChildSize = 0;
    this.parent[v] = p;
    this.depth[v] = p === -1 ? 0 : this.depth[p] + 1;

    for (const c of this.adj[v]) {
      if (c === p) continue;
      const childSize = this.dfs(c, v);
      size += childSize;
      if (childSize > maxChildSize) {
        maxChildSize = childSize;
        this.heavy[v] = c;
      }
    }
    return size;
  }

  private decompose(v: number, h: number): void {
    this.head[v] = h;
    this.pos[v] = this.curPos++;
    if (this.heavy[v] !== -1) this.decompose(this.heavy[v], h);
    for (const c of this.adj[v]) {
      if (c !== this.parent[v] && c !== this.heavy[v]) {
        this.decompose(c, c);
      }
    }
  }

  lowestCommonAncestor(u: number, v: number): number {
    while (this.head[u] !== this.head[v]) {
      if (this.depth[this.head[u]] > this.depth[this.head[v]]) {
        u = this.parent[this.head[u]];
      } else {
        v = this.parent[this.head[v]];
      }
    }
    return this.depth[u] < this.depth[v] ? u : v;
  }
}

const hld = new HeavyLightDecomposition(5, [[0, 1], [0, 2], [1, 3], [1, 4]]);
if (hld.lowestCommonAncestor(3, 4) !== 1 || hld.lowestCommonAncestor(3, 2) !== 0) {
  throw new Error("HLD LCA failed");
}
console.log("Heavy-Light Decomposition verified successfully.");
