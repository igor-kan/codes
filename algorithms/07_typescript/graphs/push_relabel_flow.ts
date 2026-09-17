/**
 * Push-Relabel Algorithm (CLRS 3rd Ed. Chapter 26.4)
 * Preflow-push maximum flow algorithm in O(V^2 E).
 */

export class PushRelabel {
  private n: number;
  private capacity: number[][];
  private flow: number[][];
  private height: number[];
  private excess: number[];

  constructor(n: number) {
    this.n = n;
    this.capacity = Array.from({ length: n }, () => new Array(n).fill(0));
    this.flow = Array.from({ length: n }, () => new Array(n).fill(0));
    this.height = new Array(n).fill(0);
    this.excess = new Array(n).fill(0);
  }

  addEdge(u: number, v: number, cap: number): void {
    this.capacity[u][v] += cap;
  }

  maxFlow(source: number, sink: number): number {
    this.height[source] = this.n;
    this.excess[source] = Infinity;

    for (let i = 0; i < this.n; i++) {
      if (i !== source) this.push(source, i);
    }

    while (true) {
      let u = -1;
      for (let i = 0; i < this.n; i++) {
        if (i !== source && i !== sink && this.excess[i] > 0) {
          u = i;
          break;
        }
      }
      if (u === -1) break;

      let pushed = false;
      for (let v = 0; v < this.n; v++) {
        if (this.capacity[u][v] - this.flow[u][v] > 0 && this.height[u] === this.height[v] + 1) {
          this.push(u, v);
          pushed = true;
          break;
        }
      }
      if (!pushed) this.relabel(u);
    }

    let total = 0;
    for (let i = 0; i < this.n; i++) total += this.flow[source][i];
    return total;
  }

  private push(u: number, v: number): void {
    const send = Math.min(this.excess[u], this.capacity[u][v] - this.flow[u][v]);
    this.flow[u][v] += send;
    this.flow[v][u] -= send;
    this.excess[u] -= send;
    this.excess[v] += send;
  }

  private relabel(u: number): void {
    let minH = Infinity;
    for (let v = 0; v < this.n; v++) {
      if (this.capacity[u][v] - this.flow[u][v] > 0) {
        minH = Math.min(minH, this.height[v]);
      }
    }
    if (minH < Infinity) this.height[u] = minH + 1;
  }
}

const pr = new PushRelabel(4);
pr.addEdge(0, 1, 10);
pr.addEdge(0, 2, 10);
pr.addEdge(1, 2, 2);
pr.addEdge(1, 3, 10);
pr.addEdge(2, 3, 10);
if (pr.maxFlow(0, 3) !== 20) throw new Error("Push-Relabel failed");
console.log("CLRS Push-Relabel verified successfully.");
