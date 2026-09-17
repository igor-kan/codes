/**
 * Skip List Implementation (William Pugh)
 * Probabilistic alternative to balanced binary search trees with expected O(log n) operations.
 */

export class SkipNode<T> {
  value: T;
  forward: (SkipNode<T> | null)[];

  constructor(value: T, level: number) {
    this.value = value;
    this.forward = new Array(level + 1).fill(null);
  }
}

export class SkipList<T> {
  private maxLevel: number;
  private p: number;
  private level = 0;
  private header: SkipNode<T>;

  constructor(maxLevel = 16, p = 0.5) {
    this.maxLevel = maxLevel;
    this.p = p;
    this.header = new SkipNode<T>(null as unknown as T, maxLevel);
  }

  private randomLevel(): number {
    let lvl = 0;
    while (Math.random() < this.p && lvl < this.maxLevel) lvl++;
    return lvl;
  }

  insert(value: T): void {
    const update = new Array<SkipNode<T>>(this.maxLevel + 1);
    let current = this.header;

    for (let i = this.level; i >= 0; i--) {
      while (current.forward[i] && current.forward[i]!.value < value) {
        current = current.forward[i]!;
      }
      update[i] = current;
    }

    const rlevel = this.randomLevel();
    if (rlevel > this.level) {
      for (let i = this.level + 1; i <= rlevel; i++) update[i] = this.header;
      this.level = rlevel;
    }

    const newNode = new SkipNode(value, rlevel);
    for (let i = 0; i <= rlevel; i++) {
      newNode.forward[i] = update[i].forward[i];
      update[i].forward[i] = newNode;
    }
  }

  search(value: T): boolean {
    let current = this.header;
    for (let i = this.level; i >= 0; i--) {
      while (current.forward[i] && current.forward[i]!.value < value) {
        current = current.forward[i]!;
      }
    }
    current = current.forward[0]!;
    return current !== null && current.value === value;
  }
}

const sl = new SkipList<number>();
[3, 6, 7, 9, 12, 19, 17, 26, 21, 25].forEach((x) => sl.insert(x));
if (!sl.search(19)) throw new Error("Skip List search failed");
console.log("Skip List verified successfully.");
