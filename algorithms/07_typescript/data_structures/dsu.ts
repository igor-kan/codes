export class DSU {
  private parent: number[];
  private size: number[];

  constructor(n: number) {
    this.parent = new Array(n);
    this.size = new Array(n).fill(1);
    for (let i = 0; i < n; i++) this.parent[i] = i;
  }

  find(x: number): number {
    if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]);
    return this.parent[x];
  }

  union(a: number, b: number): boolean {
    let ra = this.find(a), rb = this.find(b);
    if (ra === rb) return false;
    if (this.size[ra] < this.size[rb]) [ra, rb] = [rb, ra];
    this.parent[rb] = ra;
    this.size[ra] += this.size[rb];
    return true;
  }

  connected(a: number, b: number): boolean {
    return this.find(a) === this.find(b);
  }
}

const dsu = new DSU(5);
dsu.union(0, 1);
dsu.union(1, 2);
if (!dsu.connected(0, 2) || dsu.connected(0, 3)) throw new Error("DSU failed");
console.log("[TypeScript DSU] Union-find with path compression verified");
