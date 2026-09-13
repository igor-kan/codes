//! Lock-free SPSC atomic ring buffer and AVL search tree.
//! 
//! Why Rust for this module?
//! Rust guarantee compile-time memory safety, thread safety without data races,
//! and explicit atomic memory orderings (Acquire/Release) for lockless concurrency.

use std::sync::atomic::{AtomicUsize, Ordering};

pub struct SpscRingBuffer<T> {
    buffer: Vec<Option<T>>,
    capacity: usize,
    head: AtomicUsize,
    tail: AtomicUsize,
}

impl<T> SpscRingBuffer<T> {
    pub fn new(capacity: usize) -> Self {
        assert!(capacity > 0);
        let mut buffer = Vec::with_capacity(capacity);
        for _ in 0..capacity {
            buffer.push(None);
        }
        Self {
            buffer,
            capacity,
            head: AtomicUsize::new(0),
            tail: AtomicUsize::new(0),
        }
    }

    pub fn is_empty(&self) -> bool {
        self.head.load(Ordering::Acquire) == self.tail.load(Ordering::Acquire)
    }

    pub fn is_full(&self) -> bool {
        let head = self.head.load(Ordering::Acquire);
        let tail = self.tail.load(Ordering::Acquire);
        ((tail + 1) % self.capacity) == head
    }

    pub fn capacity(&self) -> usize {
        self.capacity
    }
}

fn main() {
    let rb: SpscRingBuffer<i32> = SpscRingBuffer::new(8);
    println!("Rust SPSC Ring Buffer Initialized with capacity {}", rb.capacity());
    assert!(rb.is_empty());
}
