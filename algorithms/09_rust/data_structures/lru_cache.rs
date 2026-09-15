//! LRU cache using a Vec of (key, value) with recency ordering.
struct LruCache {
    capacity: usize,
    entries: Vec<(i32, i32)>,
}

impl LruCache {
    fn new(capacity: usize) -> Self {
        LruCache { capacity, entries: Vec::new() }
    }
    fn touch(&mut self, index: usize) {
        let entry = self.entries.remove(index);
        self.entries.insert(0, entry);
    }
    fn get(&mut self, key: i32) -> i32 {
        if let Some(index) = self.entries.iter().position(|(k, _)| *k == key) {
            self.touch(index);
            return self.entries[0].1;
        }
        -1
    }
    fn put(&mut self, key: i32, value: i32) {
        if let Some(index) = self.entries.iter().position(|(k, _)| *k == key) {
            self.entries[index].1 = value;
            self.touch(index);
            return;
        }
        if self.entries.len() == self.capacity {
            self.entries.pop();
        }
        self.entries.insert(0, (key, value));
    }
}

fn main() {
    let mut cache = LruCache::new(2);
    cache.put(1, 1);
    cache.put(2, 2);
    assert_eq!(cache.get(1), 1);
    cache.put(3, 3);
    assert_eq!(cache.get(2), -1);
    println!("lru cache ok");
}
