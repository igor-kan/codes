/**
 * B-Tree Implementation (CLRS 3rd Ed. Chapter 18)
 * Self-balancing multi-way search tree with minimum degree t.
 */

export class BTreeNode<T> {
  keys: T[] = [];
  children: BTreeNode<T>[] = [];
  isLeaf: boolean;

  constructor(isLeaf = true) {
    this.isLeaf = isLeaf;
  }
}

export class BTree<T> {
  root: BTreeNode<T>;
  t: number; // Minimum degree

  constructor(t = 3) {
    this.t = t;
    this.root = new BTreeNode<T>(true);
  }

  search(key: T, node: BTreeNode<T> = this.root): boolean {
    let i = 0;
    while (i < node.keys.length && key > node.keys[i]) i++;
    if (i < node.keys.length && key === node.keys[i]) return true;
    if (node.isLeaf) return false;
    return this.search(key, node.children[i]);
  }

  insert(key: T): void {
    const r = this.root;
    if (r.keys.length === 2 * this.t - 1) {
      const s = new BTreeNode<T>(false);
      this.root = s;
      s.children.push(r);
      this.splitChild(s, 0);
      this.insertNonFull(s, key);
    } else {
      this.insertNonFull(r, key);
    }
  }

  private splitChild(x: BTreeNode<T>, i: number): void {
    const t = this.t;
    const y = x.children[i];
    const z = new BTreeNode<T>(y.isLeaf);

    z.keys = y.keys.splice(t);
    const median = y.keys.pop()!;
    if (!y.isLeaf) {
      z.children = y.children.splice(t);
    }

    x.children.splice(i + 1, 0, z);
    x.keys.splice(i, 0, median);
  }

  private insertNonFull(x: BTreeNode<T>, key: T): void {
    let i = x.keys.length - 1;
    if (x.isLeaf) {
      while (i >= 0 && key < x.keys[i]) i--;
      x.keys.splice(i + 1, 0, key);
    } else {
      while (i >= 0 && key < x.keys[i]) i--;
      i++;
      if (x.children[i].keys.length === 2 * this.t - 1) {
        this.splitChild(x, i);
        if (key > x.keys[i]) i++;
      }
      this.insertNonFull(x.children[i], key);
    }
  }
}

const btree = new BTree<number>(2);
[10, 20, 5, 6, 12, 30, 7, 17].forEach((v) => btree.insert(v));
if (!btree.search(12)) throw new Error("B-Tree search failed");
console.log("CLRS B-Tree verified successfully.");
