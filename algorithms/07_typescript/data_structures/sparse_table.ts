/**
 * Sparse Table for Range Minimum Query (RMQ)
 * O(n log n) preprocessing, O(1) query time for idempotent operations.
 */

export class SparseTable {
  private st: number[][];
  private logTable: number[];

  constructor(arr: number[]) {
    const n = arr.length;
    const k = Math.floor(Math.log2(n)) + 1;
    this.st = Array.from({ length: n }, () => new Array(k).fill(0));
    this.logTable = new Array(n + 1).fill(0);

    for (let i = 2; i <= n; i++) {
      this.logTable[i] = this.logTable[Math.floor(i / 2)] + 1;
    }

    for (let i = 0; i < n; i++) this.st[i][0] = arr[i];

    for (let j = 1; j < k; j++) {
      for (let i = 0; i + (1 << j) <= n; i++) {
        this.st[i][j] = Math.min(this.st[i][j - 1], this.st[i + (1 << (j - 1))][j - 1]);
      }
    }
  }

  queryMin(l: number, r: number): number {
    const len = r - l + 1;
    const k = this.logTable[len];
    return Math.min(this.st[l][k], this.st[r - (1 << k) + 1][k]);
  }
}

const rmq = new SparseTable([7, 2, 3, 0, 5, 10, 3, 12, 18]);
if (rmq.queryMin(1, 4) !== 0 || rmq.queryMin(4, 7) !== 3) {
  throw new Error("Sparse table query failed");
}
console.log("Sparse Table RMQ verified successfully.");
