export class SegmentTree {
  private n: number;
  private tree: number[];

  constructor(arr: number[]) {
    this.n = arr.length;
    this.tree = new Array(4 * this.n).fill(0);
    this.build(arr, 1, 0, this.n - 1);
  }

  private build(arr: number[], node: number, l: number, r: number): void {
    if (l === r) { this.tree[node] = arr[l]; return; }
    const mid = (l + r) >> 1;
    this.build(arr, node * 2, l, mid);
    this.build(arr, node * 2 + 1, mid + 1, r);
    this.tree[node] = this.tree[node * 2] + this.tree[node * 2 + 1];
  }

  update(pos: number, val: number, node: number = 1, l: number = 0, r: number = this.n - 1): void {
    if (l === r) { this.tree[node] = val; return; }
    const mid = (l + r) >> 1;
    if (pos <= mid) this.update(pos, val, node * 2, l, mid);
    else this.update(pos, val, node * 2 + 1, mid + 1, r);
    this.tree[node] = this.tree[node * 2] + this.tree[node * 2 + 1];
  }

  query(qL: number, qR: number, node: number = 1, l: number = 0, r: number = this.n - 1): number {
    if (qL > r || qR < l) return 0;
    if (qL <= l && r <= qR) return this.tree[node];
    const mid = (l + r) >> 1;
    return this.query(qL, qR, node * 2, l, mid) + this.query(qL, qR, node * 2 + 1, mid + 1, r);
  }
}

const st = new SegmentTree([1, 3, 5, 7, 9, 11]);
if (st.query(1, 3) !== 15) throw new Error("Segment Tree failed");
st.update(2, 10);
if (st.query(1, 3) !== 20) throw new Error("Segment Tree update failed");
console.log("[TypeScript Segment Tree] Range sum with point update verified");
