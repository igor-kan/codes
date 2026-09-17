/**
 * Edmonds-Karp Algorithm (CLRS 3rd Ed. Chapter 26.2)
 * Implementation of Ford-Fulkerson using BFS shortest augmenting paths in O(V E^2).
 */

export class EdmondsKarp {
  private n: number;
  private capacity: number[][];

  constructor(n: number) {
    this.n = n;
    this.capacity = Array.from({ length: n }, () => new Array(n).fill(0));
  }

  addEdge(u: number, v: number, cap: number): void {
    this.capacity[u][v] += cap;
  }

  maxFlow(source: number, sink: number): number {
    let flow = 0;
    const parent = new Array(this.n).fill(-1);

    while (this.bfs(source, sink, parent)) {
      let push = Infinity;
      for (let v = sink; v !== source; v = parent[v]) {
        const u = parent[v];
        push = Math.min(push, this.capacity[u][v]);
      }
      for (let v = sink; v !== source; v = parent[v]) {
        const u = parent[v];
        this.capacity[u][v] -= push;
        this.capacity[v][u] += push;
      }
      flow += push;
    }
    return flow;
  }

  private bfs(s: number, t: number, parent: number[]): boolean {
    parent.fill(-1);
    parent[s] = s;
    const queue = [s];

    while (queue.length > 0) {
      const u = queue.shift()!;
      for (let v = 0; v < this.n; v++) {
        if (parent[v] === -1 && this.capacity[u][v] > 0) {
          parent[v] = u;
          if (v === t) return true;
          queue.push(v);
        }
      }
    }
    return false;
  }
}

const ek = new EdmondsKarp(6);
ek.addEdge(0, 1, 16);
ek.addEdge(0, 2, 13);
ek.addEdge(1, 2, 10);
ek.addEdge(1, 3, 12);
ek.addEdge(2, 1, 4);
ek.addEdge(2, 4, 14);
ek.addEdge(3, 2, 9);
ek.addEdge(3, 5, 20);
ek.addEdge(4, 3, 7);
ek.addEdge(4, 5, 4);
if (ek.maxFlow(0, 5) !== 23) throw new Error("Edmonds-Karp max flow failed");
console.log("CLRS Edmonds-Karp Max Flow verified successfully.");
