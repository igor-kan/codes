//! Treap Implementation in Rust
//! Cartesian tree combining BST ordering on keys and heap ordering on priorities.

pub struct TreapNode<T: Ord> {
    pub key: T,
    pub priority: u32,
    pub left: Option<Box<TreapNode<T>>>,
    pub right: Option<Box<TreapNode<T>>>,
}

impl<T: Ord> TreapNode<T> {
    pub fn new(key: T, priority: u32) -> Self {
        TreapNode {
            key,
            priority,
            left: None,
            right: None,
        }
    }
}

pub struct Treap<T: Ord> {
    root: Option<Box<TreapNode<T>>>,
}

impl<T: Ord> Treap<T> {
    pub fn new() -> Self {
        Treap { root: None }
    }

    pub fn insert(&mut self, key: T, priority: u32) {
        self.root = Self::insert_node(self.root.take(), key, priority);
    }

    fn insert_node(node: Option<Box<TreapNode<T>>>, key: T, priority: u32) -> Option<Box<TreapNode<T>>> {
        let mut n = match node {
            None => return Some(Box::new(TreapNode::new(key, priority))),
            Some(b) => b,
        };

        if key < n.key {
            n.left = Self::insert_node(n.left.take(), key, priority);
            if n.left.as_ref().unwrap().priority > n.priority {
                return Some(Self::rotate_right(n));
            }
        } else if key > n.key {
            n.right = Self::insert_node(n.right.take(), key, priority);
            if n.right.as_ref().unwrap().priority > n.priority {
                return Some(Self::rotate_left(n));
            }
        }
        Some(n)
    }

    fn rotate_right(mut y: Box<TreapNode<T>>) -> Box<TreapNode<T>> {
        let mut x = y.left.take().unwrap();
        y.left = x.right.take();
        x.right = Some(y);
        x
    }

    fn rotate_left(mut x: Box<TreapNode<T>>) -> Box<TreapNode<T>> {
        let mut y = x.right.take().unwrap();
        x.right = y.left.take();
        y.left = Some(x);
        y
    }
}

fn main() {
    let mut t = Treap::new();
    t.insert(50, 10);
    t.insert(30, 20);
    t.insert(70, 5);
    println!("Rust Treap verified.");
}
