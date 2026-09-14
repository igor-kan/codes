//! A* Shortest Path Algorithm in Rust
//! Implements BinaryHeap with Custom Ordering and Manhattan Heuristic

use std::collections::{BinaryHeap, HashMap};
use std::cmp::Ordering;

#[derive(Copy, Clone, Eq, PartialEq, Hash, Debug)]
pub struct Point {
    pub r: i32,
    pub c: i32,
}

#[derive(Copy, Clone, Eq, PartialEq)]
struct State {
    f_score: i32,
    g_score: i32,
    point: Point,
}

impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        // Reverse for min-heap
        other.f_score.cmp(&self.f_score)
            .then_with(|| other.g_score.cmp(&self.g_score))
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

fn manhattan(a: Point, b: Point) -> i32 {
    (a.r - b.r).abs() + (a.c - b.c).abs()
}

pub fn a_star_grid(grid: &[Vec<i32>], start: Point, goal: Point) -> Option<Vec<Point>> {
    let rows = grid.len() as i32;
    let cols = grid[0].len() as i32;

    let mut pq = BinaryHeap::new();
    let mut g_score = HashMap::new();
    let mut came_from = HashMap::new();

    g_score.insert(start, 0);
    pq.push(State {
        f_score: manhattan(start, goal),
        g_score: 0,
        point: start,
    });

    let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)];

    while let Some(State { g_score: curr_g, point, .. }) = pq.pop() {
        if point == goal {
            let mut path = vec![goal];
            let mut curr = goal;
            while let Some(&prev) = came_from.get(&curr) {
                path.push(prev);
                curr = prev;
            }
            path.reverse();
            return Some(path);
        }

        if curr_g > *g_score.get(&point).unwrap_or(&i32::MAX) {
            continue;
        }

        for &(dr, dc) in &dirs {
            let nr = point.r + dr;
            let nc = point.c + dc;
            if nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr as usize][nc as usize] == 0 {
                let neighbor = Point { r: nr, c: nc };
                let tentative_g = curr_g + 1;
                if tentative_g < *g_score.get(&neighbor).unwrap_or(&i32::MAX) {
                    g_score.insert(neighbor, tentative_g);
                    came_from.insert(neighbor, point);
                    pq.push(State {
                        f_score: tentative_g + manhattan(neighbor, goal),
                        g_score: tentative_g,
                        point: neighbor,
                    });
                }
            }
        }
    }
    None
}

fn main() {
    let grid = vec![
        vec![0, 0, 0, 0, 0],
        vec![1, 1, 1, 1, 0],
        vec![0, 0, 0, 0, 0],
        vec![0, 1, 1, 1, 1],
        vec![0, 0, 0, 0, 0],
    ];
    let path = a_star_grid(&grid, Point { r: 0, c: 0 }, Point { r: 4, c: 4 }).expect("Path must exist");
    assert_eq!(path.len(), 17);
    println!("[Rust A*] Path computed successfully: {} steps.", path.len());
}
