/**
 * Fenwick Tree / Binary Indexed Tree (Peter Fenwick)
 * O(log n) point update and prefix sum query data structure.
 */

export class FenwickTree {
  private tree: number[];

  constructor(size: number) {
    this.tree = new Array(size + 1).fill(0);
  }

  update(index: number, delta: number): void {
    for (let i = index + 1; i < this.tree.length; i += i & -i) {
      this.tree[i] += delta;
    }
  }

  prefixSum(index: number): number {
    let sum = 0;
    for (let i = index + 1; i > 0; i -= i & -i) {
      sum += this.tree[i];
    }
    return sum;
  }

  rangeSum(left: number, right: number): number {
    return this.prefixSum(right) - (left > 0 ? this.prefixSum(left - 1) : 0);
  }
}

const bit = new FenwickTree(10);
[1, 3, 5, 7, 9, 11].forEach((v, i) => bit.update(i, v));
if (bit.rangeSum(1, 3) !== 15) throw new Error("Fenwick tree range sum error");
console.log("Fenwick Tree verified successfully.");
