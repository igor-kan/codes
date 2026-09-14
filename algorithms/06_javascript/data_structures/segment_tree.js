class SegmentTree {
  constructor(arr) {
    this.n = arr.length;
    this.tree = new Array(4 * this.n).fill(0);
    this._build(arr, 1, 0, this.n - 1);
  }
  _build(arr, node, l, r) {
    if (l === r) { this.tree[node] = arr[l]; return; }
    const mid = (l + r) >> 1;
    this._build(arr, node * 2, l, mid);
    this._build(arr, node * 2 + 1, mid + 1, r);
    this.tree[node] = this.tree[node * 2] + this.tree[node * 2 + 1];
  }
  update(pos, val, node = 1, l = 0, r = this.n - 1) {
    if (l === r) { this.tree[node] = val; return; }
    const mid = (l + r) >> 1;
    if (pos <= mid) this.update(pos, val, node * 2, l, mid);
    else this.update(pos, val, node * 2 + 1, mid + 1, r);
    this.tree[node] = this.tree[node * 2] + this.tree[node * 2 + 1];
  }
  query(qL, qR, node = 1, l = 0, r = this.n - 1) {
    if (qL > r || qR < l) return 0;
    if (qL <= l && r <= qR) return this.tree[node];
    const mid = (l + r) >> 1;
    return this.query(qL, qR, node * 2, l, mid) + this.query(qL, qR, node * 2 + 1, mid + 1, r);
  }
}

module.exports = { SegmentTree };

if (require.main === module) {
  const st = new SegmentTree([1, 3, 5, 7, 9, 11]);
  if (st.query(1, 3) !== 15) throw new Error("range sum query failed");
  st.update(2, 10);
  if (st.query(1, 3) !== 20) throw new Error("point update failed");
  console.log("[JavaScript Segment Tree] Range sum with point update verified");
}
