/**
 * Hopcroft-Karp Algorithm
 * Maximum cardinality matching in bipartite graphs in O(E sqrt(V)).
 */

export class HopcroftKarp {
  private nU: number;
  private nV: number;
  private adj: number[][];
  private pairU: number[];
  private pairV: number[];
  private dist: number[];

  constructor(nU: number, nV: number) {
    this.nU = nU;
    this.nV = nV;
    this.adj = Array.from({ length: nU + 1 }, () => []);
    this.pairU = new Array(nU + 1).fill(0);
    this.pairV = new Array(nV + 1).fill(0);
    this.dist = new Array(nU + 1).fill(0);
  }

  addEdge(u: number, v: number): void {
    this.adj[u].push(v);
  }

  private bfs(): boolean {
    const queue: number[] = [];
    for (let u = 1; u <= this.nU; u++) {
      if (this.pairU[u] === 0) {
        this.dist[u] = 0;
        queue.push(u);
      } else {
        this.dist[u] = Infinity;
      }
    }
    this.dist[0] = Infinity;

    while (queue.length > 0) {
      const u = queue.shift()!;
      if (this.dist[u] < this.dist[0]) {
        for (const v of this.adj[u]) {
          if (this.dist[this.pairV[v]] === Infinity) {
            this.dist[this.pairV[v]] = this.dist[u] + 1;
            queue.push(this.pairV[v]);
          }
        }
      }
    }
    return this.dist[0] !== Infinity;
  }

  private dfs(u: number): boolean {
    if (u !== 0) {
      for (const v of this.adj[u]) {
        if (this.dist[this.pairV[v]] === this.dist[u] + 1) {
          if (this.dfs(this.pairV[v])) {
            this.pairV[v] = u;
            this.pairU[u] = v;
            return true;
          }
        }
      }
      this.dist[u] = Infinity;
      return false;
    }
    return true;
  }

  maxMatching(): number {
    let matching = 0;
    while (this.bfs()) {
      for (let u = 1; u <= this.nU; u++) {
        if (this.pairU[u] === 0 && this.dfs(u)) {
          matching++;
        }
      }
    }
    return matching;
  }
}

const hk = new HopcroftKarp(4, 4);
hk.addEdge(1, 2);
hk.addEdge(1, 3);
hk.addEdge(2, 1);
hk.addEdge(3, 2);
hk.addEdge(4, 2);
hk.addEdge(4, 4);
if (hk.maxMatching() !== 4) throw new Error("Hopcroft-Karp failed");
console.log("Hopcroft-Karp verified successfully.");
