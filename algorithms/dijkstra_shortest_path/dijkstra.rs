use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[derive(Copy, Clone, PartialEq)]
struct State {
    cost: usize,
    position: usize,
}

impl Eq for State {}

impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other.cost.cmp(&self.cost)
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

#[derive(Clone)]
struct Edge {
    node: usize,
    cost: usize,
}

fn shortest_path(adj_list: &[Vec<Edge>], start: usize, goal: usize) -> Option<usize> {
    let mut dist: Vec<_> = (0..adj_list.len()).map(|_| usize::MAX).collect();
    let mut heap = BinaryHeap::new();

    dist[start] = 0;
    heap.push(State { cost: 0, position: start });

    while let Some(State { cost, position }) = heap.pop() {
        if position == goal { return Some(cost); }
        if cost > dist[position] { continue; }

        for edge in &adj_list[position] {
            let next = State { cost: cost + edge.cost, position: edge.node };
            if next.cost < dist[next.position] {
                dist[next.position] = next.cost;
                heap.push(next);
            }
        }
    }
    None
}

fn main() {
    let mut adj = vec![vec![]; 4];
    adj[0].push(Edge { node: 1, cost: 4 });
    adj[0].push(Edge { node: 2, cost: 1 });
    adj[2].push(Edge { node: 1, cost: 2 });
    adj[1].push(Edge { node: 3, cost: 1 });
    adj[2].push(Edge { node: 3, cost: 5 });

    let res = shortest_path(&adj, 0, 3);
    assert_eq!(res, Some(4));
    println!("[Rust Dijkstra] Shortest path 0 -> 3: {:?} verified.", res);
}
