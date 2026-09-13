//! Huffman Encoding and Decoding Algorithm in Rust.

use std::collections::{BinaryHeap, HashMap};
use std::cmp::Ordering;

#[derive(Eq, PartialEq)]
enum NodeType {
    Leaf(char),
    Internal(Box<HuffmanNode>, Box<HuffmanNode>),
}

#[derive(Eq, PartialEq)]
struct HuffmanNode {
    freq: usize,
    node_type: NodeType,
}

impl Ord for HuffmanNode {
    fn cmp(&self, other: &Self) -> Ordering {
        // Reverse ordering for min-heap
        other.freq.cmp(&self.freq)
    }
}

impl PartialOrd for HuffmanNode {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

fn build_codes(node: &HuffmanNode, prefix: String, map: &mut HashMap<char, String>) {
    match &node.node_type {
        NodeType::Leaf(c) => {
            map.insert(*c, prefix);
        }
        NodeType::Internal(left, right) => {
            build_codes(left, format!("{}0", prefix), map);
            build_codes(right, format!("{}1", prefix), map);
        }
    }
}

fn build_tree(text: &str) -> Option<HuffmanNode> {
    if text.is_empty() { return None; }
    let mut freqs = HashMap::new();
    for c in text.chars() {
        *freqs.entry(c).or_insert(0) += 1;
    }

    let mut heap = BinaryHeap::new();
    for (c, freq) in freqs {
        heap.push(HuffmanNode { freq, node_type: NodeType::Leaf(c) });
    }

    if heap.len() == 1 {
        let single = heap.pop().unwrap();
        return Some(HuffmanNode {
            freq: single.freq,
            node_type: NodeType::Internal(Box::new(single), Box::new(HuffmanNode { freq: 0, node_type: NodeType::Leaf('\0') }))
        });
    }

    while heap.len() > 1 {
        let n1 = heap.pop().unwrap();
        let n2 = heap.pop().unwrap();
        let parent = HuffmanNode {
            freq: n1.freq + n2.freq,
            node_type: NodeType::Internal(Box::new(n1), Box::new(n2)),
        };
        heap.push(parent);
    }

    heap.pop()
}

fn decode(root: &HuffmanNode, encoded: &str) -> String {
    let mut result = String::new();
    let mut curr = root;

    for bit in encoded.chars() {
        if let NodeType::Internal(ref left, ref right) = curr.node_type {
            curr = if bit == '0' { left } else { right };
        }
        if let NodeType::Leaf(c) = curr.node_type {
            result.push(c);
            curr = root;
        }
    }

    result
}

fn main() {
    let message = "this is an example for a huffman encoding demonstration";
    let tree = build_tree(message).expect("Tree must build");

    let mut code_map = HashMap::new();
    build_codes(&tree, String::new(), &mut code_map);

    let mut encoded = String::new();
    for c in message.chars() {
        encoded.push_str(&code_map[&c]);
    }

    let decoded = decode(&tree, &encoded);
    assert_eq!(decoded, message);

    println!("[Rust Huffman] Verified: decoded string matches original ({} chars)", decoded.len());
}
