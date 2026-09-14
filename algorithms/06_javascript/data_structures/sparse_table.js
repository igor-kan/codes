class SparseTable {
  constructor(arr) {
    this.n = arr.length;
    this.log = new Array(this.n + 1).fill(0);
    for (let i = 2; i <= this.n; i++) this.log[i] = this.log[i >> 1] + 1;
    const k = this.log[this.n] + 1;
    this.st = Array.from({ length: this.n }, () => new Array(k).fill(0));
    for (let i = 0; i < this.n; i++) this.st[i][0] = arr[i];
    for (let j = 1; j < k; j++)
      for (let i = 0; i + (1 << j) <= this.n; i++)
        this.st[i][j] = Math.min(this.st[i][j - 1], this.st[i + (1 << (j - 1))][j - 1]);
  }
  query(l, r) {
    const j = this.log[r - l + 1];
    return Math.min(this.st[l][j], this.st[r - (1 << j) + 1][j]);
  }
}

module.exports = { SparseTable };

if (require.main === module) {
  const st = new SparseTable([4, 2, 6, 1, 9, 3]);
  if (st.query(1, 4) !== 1) throw new Error("RMQ query failed");
  if (st.query(0, 2) !== 2) throw new Error("RMQ query failed");
  console.log("[JavaScript Sparse Table] Range minimum query verified");
}
