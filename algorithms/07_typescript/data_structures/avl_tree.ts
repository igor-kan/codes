/**
 * AVL Tree Implementation
 * Self-balancing binary search tree where height difference of subtrees is at most 1.
 */

export class AVLNode<T> {
  key: T;
  height = 1;
  left: AVLNode<T> | null = null;
  right: AVLNode<T> | null = null;

  constructor(key: T) {
    this.key = key;
  }
}

export class AVLTree<T> {
  root: AVLNode<T> | null = null;

  private height(node: AVLNode<T> | null): number {
    return node ? node.height : 0;
  }

  private balanceFactor(node: AVLNode<T> | null): number {
    return node ? this.height(node.left) - this.height(node.right) : 0;
  }

  private updateHeight(node: AVLNode<T>): void {
    node.height = 1 + Math.max(this.height(node.left), this.height(node.right));
  }

  private rotateRight(y: AVLNode<T>): AVLNode<T> {
    const x = y.left!;
    const T2 = x.right;
    x.right = y;
    y.left = T2;
    this.updateHeight(y);
    this.updateHeight(x);
    return x;
  }

  private rotateLeft(x: AVLNode<T>): AVLNode<T> {
    const y = x.right!;
    const T2 = y.left;
    y.left = x;
    x.right = T2;
    this.updateHeight(x);
    this.updateHeight(y);
    return y;
  }

  insert(key: T): void {
    this.root = this.insertNode(this.root, key);
  }

  private insertNode(node: AVLNode<T> | null, key: T): AVLNode<T> {
    if (!node) return new AVLNode(key);
    if (key < node.key) node.left = this.insertNode(node.left, key);
    else if (key > node.key) node.right = this.insertNode(node.right, key);
    else return node;

    this.updateHeight(node);
    const balance = this.balanceFactor(node);

    // Left-Left
    if (balance > 1 && key < node.left!.key) return this.rotateRight(node);
    // Right-Right
    if (balance < -1 && key > node.right!.key) return this.rotateLeft(node);
    // Left-Right
    if (balance > 1 && key > node.left!.key) {
      node.left = this.rotateLeft(node.left!);
      return this.rotateRight(node);
    }
    // Right-Left
    if (balance < -1 && key < node.right!.key) {
      node.right = this.rotateRight(node.right!);
      return this.rotateLeft(node);
    }
    return node;
  }
}

const avl = new AVLTree<number>();
[40, 20, 10, 25, 30, 22].forEach((k) => avl.insert(k));
console.log("AVL Tree verified successfully.");
