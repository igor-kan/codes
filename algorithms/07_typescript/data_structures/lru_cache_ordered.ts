/**
 * Least Recently Used (LRU) Cache
 * O(1) get and put using a Hash Map and Doubly Linked List.
 */

class DNode<K, V> {
  key: K;
  val: V;
  prev: DNode<K, V> | null = null;
  next: DNode<K, V> | null = null;

  constructor(key: K, val: V) {
    this.key = key;
    this.val = val;
  }
}

export class LRUCache<K, V> {
  private capacity: number;
  private map = new Map<K, DNode<K, V>>();
  private head: DNode<K, V>;
  private tail: DNode<K, V>;

  constructor(capacity: number) {
    this.capacity = capacity;
    this.head = new DNode<K, V>(null as unknown as K, null as unknown as V);
    this.tail = new DNode<K, V>(null as unknown as K, null as unknown as V);
    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  private remove(node: DNode<K, V>): void {
    node.prev!.next = node.next;
    node.next!.prev = node.prev;
  }

  private insertToFront(node: DNode<K, V>): void {
    node.next = this.head.next;
    node.prev = this.head;
    this.head.next!.prev = node;
    this.head.next = node;
  }

  get(key: K): V | undefined {
    const node = this.map.get(key);
    if (!node) return undefined;
    this.remove(node);
    this.insertToFront(node);
    return node.val;
  }

  put(key: K, val: V): void {
    if (this.map.has(key)) {
      this.remove(this.map.get(key)!);
    }
    const newNode = new DNode(key, val);
    this.insertToFront(newNode);
    this.map.set(key, newNode);

    if (this.map.size > this.capacity) {
      const lru = this.tail.prev!;
      this.remove(lru);
      this.map.delete(lru.key);
    }
  }
}

const cache = new LRUCache<number, string>(2);
cache.put(1, "one");
cache.put(2, "two");
cache.get(1); // 1 is now most recent
cache.put(3, "three"); // evicts 2
if (cache.get(2) !== undefined || cache.get(1) !== "one") {
  throw new Error("LRU Cache eviction error");
}
console.log("LRU Cache verified successfully.");
