/**
 * Dijkstra's Algorithm with Binary Min-Heap (CLRS 3rd Ed. Chapter 24.3)
 * Non-negative edge weight single-source shortest paths in O((V + E) log V).
 */

class MinHeap<T> {
  private data: { key: number; item: T }[] = [];

  push(key: number, item: T): void {
    this.data.push({ key, item });
    this.up(this.data.length - 1);
  }

  pop(): { key: number; item: T } | undefined {
    if (this.data.length === 0) return undefined;
    const top = this.data[0];
    const bottom = this.data.pop()!;
    if (this.data.length > 0) {
      this.data[0] = bottom;
      this.down(0);
    }
    return top;
  }

  get size(): number {
    return this.data.length;
  }

  private up(i: number): void {
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (this.data[i].key >= this.data[p].key) break;
      [this.data[i], this.data[p]] = [this.data[p], this.data[i]];
      i = p;
    }
  }

  private down(i: number): void {
    const len = this.data.length;
    while ((i << 1) + 1 < len) {
      let left = (i << 1) + 1;
      let right = left + 1;
      let best = left;
      if (right < len && this.data[right].key < this.data[left].key) best = right;
      if (this.data[i].key <= this.data[best].key) break;
      [this.data[i], this.data[best]] = [this.data[best], this.data[i]];
      i = best;
    }
  }
}

export function dijkstra(
  n: number,
  adj: { to: number; weight: number }[][],
  source: number
): number[] {
  const dist = new Array(n).fill(Infinity);
  dist[source] = 0;
  const heap = new MinHeap<number>();
  heap.push(0, source);

  while (heap.size > 0) {
    const { key: d, item: u } = heap.pop()!;
    if (d > dist[u]) continue;

    for (const edge of adj[u]) {
      if (dist[u] + edge.weight < dist[edge.to]) {
        dist[edge.to] = dist[u] + edge.weight;
        heap.push(dist[edge.to], edge.to);
      }
    }
  }
  return dist;
}

const g: { to: number; weight: number }[][] = [
  [{ to: 1, weight: 4 }, { to: 2, weight: 1 }],
  [{ to: 3, weight: 1 }],
  [{ to: 1, weight: 2 }, { to: 3, weight: 5 }],
  [],
];
const dists = dijkstra(4, g, 0);
if (dists[3] !== 4) throw new Error("Dijkstra verification failed");
console.log("CLRS Dijkstra with Min-Heap verified successfully.");
