// Binary max-heap.
class MaxHeap {
  private items: number[] = [];

  get size(): number {
    return this.items.length;
  }

  push(value: number): void {
    const a = this.items;
    a.push(value);
    let i = a.length - 1;
    while (i > 0) {
      const parent = (i - 1) >> 1;
      if (a[parent] >= a[i]) break;
      [a[parent], a[i]] = [a[i], a[parent]];
      i = parent;
    }
  }

  pop(): number {
    const a = this.items;
    const top = a[0];
    const last = a.pop() as number;
    if (a.length > 0) {
      a[0] = last;
      let i = 0;
      for (;;) {
        const l = 2 * i + 1;
        const r = 2 * i + 2;
        let best = i;
        if (l < a.length && a[l] > a[best]) best = l;
        if (r < a.length && a[r] > a[best]) best = r;
        if (best === i) break;
        [a[i], a[best]] = [a[best], a[i]];
        i = best;
      }
    }
    return top;
  }
}

const heap = new MaxHeap();
for (const v of [5, 3, 8, 1, 4]) heap.push(v);
let prev = Infinity;
while (heap.size > 0) {
  const x = heap.pop();
  if (x > prev) throw new Error("not a max-heap order");
  prev = x;
}
console.log("max heap ok");
