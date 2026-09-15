//! Binary max-heap via std::collections::BinaryHeap.
use std::collections::BinaryHeap;

fn main() {
    let mut heap = BinaryHeap::new();
    for v in [5, 3, 8, 1, 4] {
        heap.push(v);
    }
    let mut prev = i32::MAX;
    while let Some(x) = heap.pop() {
        assert!(x <= prev, "not a max-heap order");
        prev = x;
    }
    println!("max heap ok");
}
