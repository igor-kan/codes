//! Egg dropping: minimum trials with k eggs and n floors.
fn main() {
    let eggs = 2usize;
    let floors = 100i32;
    let mut dp = vec![vec![0i32; eggs + 1]; 101];
    let mut trials = 0usize;
    while dp[trials][eggs] < floors {
        trials += 1;
        for k in 1..=eggs {
            dp[trials][k] = dp[trials - 1][k - 1] + dp[trials - 1][k] + 1;
        }
    }
    assert_eq!(trials, 14);
    println!("egg drop={}", trials);
}
