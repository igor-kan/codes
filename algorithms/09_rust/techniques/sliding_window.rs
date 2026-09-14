//! Sliding window technique in Rust.

pub fn max_sum_fixed_window(nums: &[i64], k: usize) -> i64 {
    if k > nums.len() {
        return 0;
    }
    let mut sum: i64 = nums[..k].iter().sum();
    let mut best = sum;
    for i in k..nums.len() {
        sum += nums[i] - nums[i - k];
        best = best.max(sum);
    }
    best
}

fn main() {
    let nums = [2i64, 1, 5, 1, 3, 2];
    assert_eq!(max_sum_fixed_window(&nums, 3), 9);
    println!("[Rust SlidingWindow] Fixed-size max sum verified: 9");
}
