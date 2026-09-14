class DSU {
  constructor(n) {
    this.parent = new Array(n);
    this.size = new Array(n).fill(1);
    for (let i = 0; i < n; i++) this.parent[i] = i;
  }
  find(x) {
    if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);
    return this.parent[x];
  }
  union(a, b) {
    let ra = this.find(a), rb = this.find(b);
    if (ra === rb) return false;
    if (this.size[ra] < this.size[rb]) [ra, rb] = [rb, ra];
    this.parent[rb] = ra;
    this.size[ra] += this.size[rb];
    return true;
  }
  connected(a, b) {
    return this.find(a) === this.find(b);
  }
}

module.exports = { DSU };

if (require.main === module) {
  const dsu = new DSU(5);
  dsu.union(0, 1);
  dsu.union(1, 2);
  dsu.union(3, 4);
  if (!dsu.connected(0, 2) || dsu.connected(0, 3) || dsu.connected(0, 4)) {
    throw new Error("DSU connectivity failed");
  }
  console.log("[JavaScript DSU] Union-find with path compression verified");
}
