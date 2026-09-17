/**
 * Treap (Tree + Heap) Implementation
 * Randomized balanced binary search tree maintaining BST on keys and Max-Heap on priorities.
 */

export class TreapNode<T> {
  key: T;
  priority: number;
  left: TreapNode<T> | null = null;
  right: TreapNode<T> | null = null;

  constructor(key: T) {
    this.key = key;
    this.priority = Math.random();
  }
}

export class Treap<T> {
  root: TreapNode<T> | null = null;

  private rotateRight(y: TreapNode<T>): TreapNode<T> {
    const x = y.left!;
    y.left = x.right;
    x.right = y;
    return x;
  }

  private rotateLeft(x: TreapNode<T>): TreapNode<T> {
    const y = x.right!;
    x.right = y.left;
    y.left = x;
    return y;
  }

  insert(key: T): void {
    this.root = this.insertNode(this.root, key);
  }

  private insertNode(node: TreapNode<T> | null, key: T): TreapNode<T> {
    if (!node) return new TreapNode(key);
    if (key < node.key) {
      node.left = this.insertNode(node.left, key);
      if (node.left.priority > node.priority) node = this.rotateRight(node);
    } else if (key > node.key) {
      node.right = this.insertNode(node.right, key);
      if (node.right.priority > node.priority) node = this.rotateLeft(node);
    }
    return node;
  }

  search(key: T): boolean {
    let curr = this.root;
    while (curr) {
      if (key === curr.key) return true;
      curr = key < curr.key ? curr.left : curr.right;
    }
    return false;
  }
}

const treap = new Treap<number>();
[50, 30, 20, 40, 70, 60, 80].forEach((v) => treap.insert(v));
if (!treap.search(40)) throw new Error("Treap search failed");
console.log("Treap verified successfully.");
