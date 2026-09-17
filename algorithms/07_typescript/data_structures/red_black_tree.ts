/**
 * Red-Black Tree Implementation (CLRS 3rd Ed. Chapter 13)
 * A self-balancing binary search tree with logarithmic height guarantee.
 */

export enum Color {
  RED,
  BLACK,
}

export class RBNode<T> {
  key: T;
  color: Color;
  left: RBNode<T> | null = null;
  right: RBNode<T> | null = null;
  parent: RBNode<T> | null = null;

  constructor(key: T, color: Color = Color.RED) {
    this.key = key;
    this.color = color;
  }
}

export class RedBlackTree<T> {
  root: RBNode<T> | null = null;

  private leftRotate(x: RBNode<T>): void {
    const y = x.right;
    if (!y) return;
    x.right = y.left;
    if (y.left) y.left.parent = x;
    y.parent = x.parent;
    if (!x.parent) {
      this.root = y;
    } else if (x === x.parent.left) {
      x.parent.left = y;
    } else {
      x.parent.right = y;
    }
    y.left = x;
    x.parent = y;
  }

  private rightRotate(y: RBNode<T>): void {
    const x = y.left;
    if (!x) return;
    y.left = x.right;
    if (x.right) x.right.parent = y;
    x.parent = y.parent;
    if (!y.parent) {
      this.root = x;
    } else if (y === y.parent.right) {
      y.parent.right = x;
    } else {
      y.parent.left = x;
    }
    x.right = y;
    y.parent = x;
  }

  insert(key: T): void {
    const z = new RBNode(key, Color.RED);
    let y: RBNode<T> | null = null;
    let x = this.root;

    while (x !== null) {
      y = x;
      if (z.key < x.key) x = x.left;
      else x = x.right;
    }

    z.parent = y;
    if (y === null) {
      this.root = z;
    } else if (z.key < y.key) {
      y.left = z;
    } else {
      y.right = z;
    }

    this.insertFixup(z);
  }

  private insertFixup(z: RBNode<T>): void {
    while (z.parent && z.parent.color === Color.RED) {
      if (z.parent === z.parent.parent?.left) {
        const y = z.parent.parent.right;
        if (y && y.color === Color.RED) {
          z.parent.color = Color.BLACK;
          y.color = Color.BLACK;
          z.parent.parent.color = Color.RED;
          z = z.parent.parent;
        } else {
          if (z === z.parent.right) {
            z = z.parent;
            this.leftRotate(z);
          }
          if (z.parent && z.parent.parent) {
            z.parent.color = Color.BLACK;
            z.parent.parent.color = Color.RED;
            this.rightRotate(z.parent.parent);
          }
        }
      } else if (z.parent.parent) {
        const y = z.parent.parent.left;
        if (y && y.color === Color.RED) {
          z.parent.color = Color.BLACK;
          y.color = Color.BLACK;
          z.parent.parent.color = Color.RED;
          z = z.parent.parent;
        } else {
          if (z === z.parent.left) {
            z = z.parent;
            this.rightRotate(z);
          }
          if (z.parent && z.parent.parent) {
            z.parent.color = Color.BLACK;
            z.parent.parent.color = Color.RED;
            this.leftRotate(z.parent.parent);
          }
        }
      }
    }
    if (this.root) this.root.color = Color.BLACK;
  }

  search(key: T): RBNode<T> | null {
    let curr = this.root;
    while (curr !== null) {
      if (key === curr.key) return curr;
      curr = key < curr.key ? curr.left : curr.right;
    }
    return null;
  }
}

// Verification
const rbt = new RedBlackTree<number>();
[10, 20, 30, 15, 25, 5].forEach((v) => rbt.insert(v));
if (!rbt.search(15)) throw new Error("Red-Black Tree search failed");
console.log("CLRS Red-Black Tree verified successfully.");
