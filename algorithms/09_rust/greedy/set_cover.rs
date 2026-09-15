//! Greedy set cover.
fn set_cover(universe_size: usize, subsets: &[Vec<usize>]) -> Vec<Vec<usize>> {
    let mut covered = vec![false; universe_size + 1];
    let mut remaining = universe_size;
    let mut chosen = Vec::new();
    while remaining > 0 {
        let mut best: Option<&Vec<usize>> = None;
        let mut best_count = 0;
        for subset in subsets {
            let count = subset.iter().filter(|&&value| !covered[value]).count();
            if count > best_count {
                best_count = count;
                best = Some(subset);
            }
        }
        match best {
            Some(subset) if best_count > 0 => {
                for &value in subset {
                    if !covered[value] {
                        covered[value] = true;
                        remaining -= 1;
                    }
                }
                chosen.push(subset.clone());
            }
            _ => break,
        }
    }
    chosen
}

fn main() {
    let chosen = set_cover(5, &[vec![1, 2, 3], vec![2, 4], vec![3, 4], vec![4, 5]]);
    assert_eq!(chosen.len(), 2);
    println!("set cover ok");
}
