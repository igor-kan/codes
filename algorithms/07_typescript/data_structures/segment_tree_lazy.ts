/**
 * Segment Tree with Lazy Propagation
 * O(log n) range additions and range sum queries.
 */

export class SegmentTreeLazy {
  private n: number;
  private tree: number[];
  private lazy: number[];

  constructor(arr: number[]) {
    this.n = arr.length;
    this.tree = new Array(4 * this.n).fill(0);
    this.lazy = new Array(4 * this.n).fill(0);
    this.build(arr, 0, 0, this.n - 1);
  }

  private build(arr: number[], node: number, l: number, r: number): void {
    if (l === r) {
      this.tree[node] = arr[l];
      return;
    }
    const mid = (l + r) >> 1;
    this.build(arr, 2 * node + 1, l, mid);
    this.build(arr, 2 * node + 2, mid + 1, r);
    this.tree[node] = this.tree[2 * node + 1] + this.tree[2 * node + 2];
  }

  private push(node: number, l: number, r: number): void {
    if (this.lazy[node] !== 0) {
      const mid = (l + r) >> 1;
      const leftChild = 2 * node + 1;
      const rightChild = 2 * node + 2;
      const val = this.lazy[node];

      this.tree[leftChild] += val * (mid - l + 1);
      this.lazy[leftChild] += val;
      this.tree[rightChild] += val * (r - mid);
      this.lazy[rightChild] += val;
      this.lazy[node] = 0;
    }
  }

  updateRange(ql: number, qr: number, val: number, node = 0, l = 0, r = this.n - 1): void {
    if (ql <= l && r <= qr) {
      this.tree[node] += val * (r - l + 1);
      this.lazy[node] += val;
      return;
    }
    this.push(node, l, r);
    const mid = (l + r) >> 1;
    if (ql <= mid) this.updateRange(ql, qr, val, 2 * node + 1, l, mid);
    if (qr > mid) this.updateRange(ql, qr, val, 2 * node + 2, mid + 1, r);
    this.tree[node] = this.tree[2 * node + 1] + this.tree[2 * node + 2];
  }

  queryRange(ql: number, qr: number, node = 0, l = 0, r = this.n - 1): number {
    if (ql <= l && r <= qr) return this.tree[node];
    this.push(node, l, r);
    const mid = (l + r) >> 1;
    let sum = 0;
    if (ql <= mid) sum += this.queryRange(ql, qr, 2 * node + 1, l, mid);
    if (qr > mid) sum += this.queryRange(ql, qr, 2 * node + 2, mid + 1, r);
    return sum;
  }
}

const seg = new SegmentTreeLazy([1, 2, 3, 4, 5]);
seg.updateRange(1, 3, 10);
if (seg.queryRange(1, 3) !== 39) throw new Error("Segment tree lazy query failed");
console.log("Segment Tree with Lazy Propagation verified successfully.");
