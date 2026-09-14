use std::collections::BTreeMap;
use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};

pub struct ConsistentHashRing {
    ring: BTreeMap<u64, String>,
    replicas: usize,
}

impl ConsistentHashRing {
    pub fn new(replicas: usize) -> Self {
        Self { ring: BTreeMap::new(), replicas }
    }

    fn hash<T: Hash>(&self, key: &T) -> u64 {
        let mut hasher = DefaultHasher::new();
        key.hash(&mut hasher);
        hasher.finish()
    }

    pub fn add_node(&mut self, node: &str) {
        for i in 0..self.replicas {
            let virtual_key = format!("{}:{}", node, i);
            let h = self.hash(&virtual_key);
            self.ring.insert(h, node.to_string());
        }
    }

    pub fn get_node(&self, key: &str) -> Option<&String> {
        if self.ring.is_empty() { return None; }
        let h = self.hash(&key);
        match self.ring.range(h..).next() {
            Some((_, node)) => Some(node),
            None => self.ring.values().next(),
        }
    }
}
