fn next_round(scores: &[i32], k: usize) -> usize {
    let threshold = scores[k - 1];
    scores.iter().filter(|&&score| score >= threshold && score > 0).count()
}

fn main() {
    assert_eq!(next_round(&[10, 9, 8, 7, 7, 7, 5, 5], 5), 6);
    assert_eq!(next_round(&[0, 0, 0, 0], 2), 0);
    println!("158A next round ok");
}
