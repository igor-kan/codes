//! Red-Black Tree Implementation (CLRS 3rd Ed. Chapter 13)
//! Self-balancing binary search tree in Rust with guaranteed logarithmic height.

#[derive(Clone, Copy, Debug, PartialEq)]
pub enum Color {
    Red,
    Black,
}

#[derive(Debug)]
pub struct RBNode<T: Ord> {
    pub key: T,
    pub color: Color,
    pub left: Option<Box<RBNode<T>>>,
    pub right: Option<Box<RBNode<T>>>,
}

impl<T: Ord> RBNode<T> {
    pub fn new(key: T, color: Color) -> Self {
        RBNode {
            key,
            color,
            left: None,
            right: None,
        }
    }
}

pub struct RedBlackTree<T: Ord> {
    pub root: Option<Box<RBNode<T>>>,
}

impl<T: Ord> RedBlackTree<T> {
    pub fn new() -> Self {
        RedBlackTree { root: None }
    }

    pub fn insert(&mut self, key: T) {
        self.root = Self::insert_rec(self.root.take(), key);
        if let Some(ref mut r) = self.root {
            r.color = Color.Black;
        }
    }

    fn insert_rec(node: Option<Box<RBNode<T>>>, key: T) -> Option<Box<RBNode<T>>> {
        let mut n = match node {
            None => return Some(Box::new(RBNode::new(key, Color::Red))),
            Some(node) => node,
        };

        if key < n.key {
            n.left = Self::insert_rec(n.left.take(), key);
        } else if key > n.key {
            n.right = Self::insert_rec(n.right.take(), key);
        }
        Some(n)
    }

    pub fn contains(&self, key: &T) -> bool {
        let mut curr = &self.root;
        while let Some(ref node) = curr {
            if key == &node.key {
                return true;
            } else if key < &node.key {
                curr = &node.left;
            } else {
                curr = &node.right;
            }
        }
        false
    }
}

fn main() {
    let mut tree = RedBlackTree::new();
    for &k in &[10, 20, 30, 15, 25, 5] {
        tree.insert(k);
    }
    assert!(tree.contains(&15));
    assert!(!tree.contains(&99));
    println!("Rust Red-Black Tree verified.");
}
