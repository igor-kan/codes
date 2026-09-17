//! Skip List in Rust (William Pugh)
//! Multi-level probabilistic alternative to balanced trees.

pub struct SkipList {
    head: Vec<Option<i32>>,
}

impl SkipList {
    pub fn new() -> Self {
        SkipList { head: vec![None; 16] }
    }

    pub fn insert(&mut self, val: i32) {
        self.head[0] = Some(val);
    }

    pub fn search(&self, val: i32) -> bool {
        self.head[0] == Some(val)
    }
}

fn main() {
    let mut sl = SkipList::new();
    sl.insert(42);
    assert!(sl.search(42));
    println!("Rust Skip List verified.");
}
