//! Rod cutting (CLRS 15.1).
fn cut_rod(prices: &[i32], n: usize) -> i32 {
    let mut best = vec![0i32; n + 1];
    for len in 1..=n {
        for i in 1..=len {
            best[len] = best[len].max(prices[i - 1] + best[len - i]);
        }
    }
    best[n]
}

fn main() {
    let prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30];
    assert_eq!(cut_rod(&prices, 4), 10);
    assert_eq!(cut_rod(&prices, 7), 18);
    assert_eq!(cut_rod(&prices, 10), 30);
    println!("rod cutting ok");
}
