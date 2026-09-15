//! Self-balancing AVL tree (insert + inorder).
use std::cmp::max;

struct Node {
    key: i32,
    height: i32,
    left: Option<Box<Node>>,
    right: Option<Box<Node>>,
}

impl Node {
    fn new(key: i32) -> Self {
        Node { key, height: 1, left: None, right: None }
    }
    fn height(node: &Option<Box<Node>>) -> i32 {
        node.as_ref().map_or(0, |n| n.height)
    }
    fn update(&mut self) {
        self.height = 1 + max(Self::height(&self.left), Self::height(&self.right));
    }
    fn balance_factor(&self) -> i32 {
        Self::height(&self.left) - Self::height(&self.right)
    }
}

fn rotate_right(mut y: Box<Node>) -> Box<Node> {
    let mut x = y.left.take().unwrap();
    y.left = x.right.take();
    y.update();
    x.right = Some(y);
    x.update();
    x
}

fn rotate_left(mut x: Box<Node>) -> Box<Node> {
    let mut y = x.right.take().unwrap();
    x.right = y.left.take();
    x.update();
    y.left = Some(x);
    y.update();
    y
}

fn balance(mut node: Box<Node>) -> Box<Node> {
    node.update();
    if node.balance_factor() > 1 {
        if Node::height(&node.left.as_ref().unwrap().left)
            < Node::height(&node.left.as_ref().unwrap().right)
        {
            let left = node.left.take().unwrap();
            node.left = Some(rotate_left(left));
        }
        return rotate_right(node);
    }
    if node.balance_factor() < -1 {
        if Node::height(&node.right.as_ref().unwrap().right)
            < Node::height(&node.right.as_ref().unwrap().left)
        {
            let right = node.right.take().unwrap();
            node.right = Some(rotate_right(right));
        }
        return rotate_left(node);
    }
    node
}

fn insert(node: Option<Box<Node>>, key: i32) -> Box<Node> {
    match node {
        None => Box::new(Node::new(key)),
        Some(mut n) => {
            if key < n.key {
                n.left = Some(insert(n.left.take(), key));
            } else if key > n.key {
                n.right = Some(insert(n.right.take(), key));
            } else {
                return n;
            }
            balance(n)
        }
    }
}

fn inorder(node: &Option<Box<Node>>, out: &mut Vec<i32>) {
    if let Some(n) = node {
        inorder(&n.left, out);
        out.push(n.key);
        inorder(&n.right, out);
    }
}

fn main() {
    let mut root = None;
    for key in [10, 20, 30, 40, 50, 25] {
        root = Some(insert(root, key));
    }
    let mut out = Vec::new();
    inorder(&root, &mut out);
    assert!(out.windows(2).all(|w| w[0] < w[1]));
    println!("avl tree ok");
}
