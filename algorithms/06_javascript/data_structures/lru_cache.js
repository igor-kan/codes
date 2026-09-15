// LRU cache using a Map's insertion order.
class LRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.store = new Map();
  }

  get(key) {
    if (!this.store.has(key)) return -1;
    const value = this.store.get(key);
    this.store.delete(key);
    this.store.set(key, value);
    return value;
  }

  put(key, value) {
    if (this.store.has(key)) this.store.delete(key);
    else if (this.store.size === this.capacity) this.store.delete(this.store.keys().next().value);
    this.store.set(key, value);
  }
}

const cache = new LRUCache(2);
cache.put(1, 1);
cache.put(2, 2);
if (cache.get(1) !== 1) throw new Error("expected 1");
cache.put(3, 3);
if (cache.get(2) !== -1) throw new Error("expected eviction");
console.log("lru cache ok");
