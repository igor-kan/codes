/**
 * Splay Tree Implementation (Sleator & Tarjan)
 * Self-adjusting binary search tree where recently accessed elements are moved to root.
 */

export class SplayNode<T> {
  key: T;
  left: SplayNode<T> | null = null;
  right: SplayNode<T> | null = null;
  parent: SplayNode<T> | null = null;

  constructor(key: T) {
    this.key = key;
  }
}

export class SplayTree<T> {
  root: SplayNode<T> | null = null;

  private rotateLeft(x: SplayNode<T>): void {
    const y = x.right!;
    x.right = y.left;
    if (y.left) y.left.parent = x;
    y.parent = x.parent;
    if (!x.parent) this.root = y;
    else if (x === x.parent.left) x.parent.left = y;
    else x.parent.right = y;
    y.left = x;
    x.parent = y;
  }

  private rotateRight(x: SplayNode<T>): void {
    const y = x.left!;
    x.left = y.right;
    if (y.right) y.right.parent = x;
    y.parent = x.parent;
    if (!x.parent) this.root = y;
    else if (x === x.parent.right) x.parent.right = y;
    else x.parent.left = y;
    y.right = x;
    x.parent = y;
  }

  private splay(x: SplayNode<T>): void {
    while (x.parent) {
      if (!x.parent.parent) {
        if (x === x.parent.left) this.rotateRight(x.parent);
        else this.rotateLeft(x.parent);
      } else if (x === x.parent.left && x.parent === x.parent.parent.left) {
        this.rotateRight(x.parent.parent);
        this.rotateRight(x.parent);
      } else if (x === x.parent.right && x.parent === x.parent.parent.right) {
        this.rotateLeft(x.parent.parent);
        this.rotateLeft(x.parent);
      } else if (x === x.parent.right && x.parent === x.parent.parent.left) {
        this.rotateLeft(x.parent);
        this.rotateRight(x.parent);
      } else {
        this.rotateRight(x.parent);
        this.rotateLeft(x.parent);
      }
    }
  }

  insert(key: T): void {
    if (!this.root) {
      this.root = new SplayNode(key);
      return;
    }
    let curr: SplayNode<T> | null = this.root;
    let p: SplayNode<T> | null = null;
    while (curr) {
      p = curr;
      if (key < curr.key) curr = curr.left;
      else if (key > curr.key) curr = curr.right;
      else {
        this.splay(curr);
        return;
      }
    }
    const newNode = new SplayNode(key);
    newNode.parent = p;
    if (key < p!.key) p!.left = newNode;
    else p!.right = newNode;
    this.splay(newNode);
  }

  search(key: T): boolean {
    let curr = this.root;
    while (curr) {
      if (key === curr.key) {
        this.splay(curr);
        return true;
      }
      curr = key < curr.key ? curr.left : curr.right;
    }
    return false;
  }
}

const splay = new SplayTree<number>();
[15, 10, 20, 5, 8].forEach((k) => splay.insert(k));
if (!splay.search(8)) throw new Error("Splay tree search failed");
console.log("Splay Tree verified successfully.");
