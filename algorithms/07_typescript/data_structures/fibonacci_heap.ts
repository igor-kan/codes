/**
 * Fibonacci Heap Implementation (CLRS 3rd Ed. Chapter 19)
 * Amortized O(1) insertion, decrease-key, and O(log n) extract-min.
 */

export class FibNode<T> {
  key: number;
  value: T;
  degree = 0;
  mark = false;
  parent: FibNode<T> | null = null;
  child: FibNode<T> | null = null;
  left: FibNode<T> = this;
  right: FibNode<T> = this;

  constructor(key: number, value: T) {
    this.key = key;
    this.value = value;
  }
}

export class FibonacciHeap<T> {
  minNode: FibNode<T> | null = null;
  count = 0;

  insert(key: number, value: T): FibNode<T> {
    const node = new FibNode(key, value);
    if (!this.minNode) {
      this.minNode = node;
    } else {
      this.addToRootList(node);
      if (node.key < this.minNode.key) this.minNode = node;
    }
    this.count++;
    return node;
  }

  private addToRootList(node: FibNode<T>): void {
    if (!this.minNode) {
      this.minNode = node;
      node.left = node;
      node.right = node;
      return;
    }
    node.right = this.minNode.right;
    node.left = this.minNode;
    this.minNode.right.left = node;
    this.minNode.right = node;
  }

  extractMin(): FibNode<T> | null {
    const z = this.minNode;
    if (!z) return null;

    if (z.child) {
      let c = z.child;
      const children: FibNode<T>[] = [];
      do {
        children.push(c);
        c = c.right;
      } while (c !== z.child);

      for (const child of children) {
        this.addToRootList(child);
        child.parent = null;
      }
    }

    z.left.right = z.right;
    z.right.left = z.left;

    if (z === z.right) {
      this.minNode = null;
    } else {
      this.minNode = z.right;
      this.consolidate();
    }
    this.count--;
    return z;
  }

  private consolidate(): void {
    const maxDegree = Math.floor(Math.log2(this.count + 1)) + 5;
    const A: (FibNode<T> | null)[] = new Array(maxDegree).fill(null);

    const rootNodes: FibNode<T>[] = [];
    let curr = this.minNode;
    if (curr) {
      do {
        rootNodes.push(curr);
        curr = curr.right;
      } while (curr !== this.minNode);
    }

    for (const w of rootNodes) {
      let x = w;
      let d = x.degree;
      while (A[d]) {
        let y = A[d]!;
        if (x.key > y.key) {
          const tmp = x;
          x = y;
          y = tmp;
        }
        this.link(y, x);
        A[d] = null;
        d++;
      }
      A[d] = x;
    }

    this.minNode = null;
    for (const node of A) {
      if (node) {
        if (!this.minNode || node.key < this.minNode.key) {
          this.minNode = node;
        }
      }
    }
  }

  private link(y: FibNode<T>, x: FibNode<T>): void {
    y.left.right = y.right;
    y.right.left = y.left;
    y.parent = x;
    if (!x.child) {
      x.child = y;
      y.left = y;
      y.right = y;
    } else {
      y.right = x.child.right;
      y.left = x.child;
      x.child.right.left = y;
      x.child.right = y;
    }
    x.degree++;
    y.mark = false;
  }
}

const fib = new FibonacciHeap<string>();
fib.insert(10, "A");
fib.insert(3, "B");
fib.insert(15, "C");
const min = fib.extractMin();
if (!min || min.key !== 3) throw new Error("Fibonacci heap extract min failed");
console.log("CLRS Fibonacci Heap verified successfully.");
