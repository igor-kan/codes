//! Kadane's algorithm for maximum subarray sum in Rust.

pub fn max_subarray(nums: &[i64]) -> i64 {
    if nums.is_empty() {
        return 0;
    }
    let mut best = nums[0];
    let mut cur = nums[0];
    for &x in &nums[1..] {
        cur = (cur + x).max(x);
        best = best.max(cur);
    }
    best
}

fn main() {
    let nums = [-2i64, 1, -3, 4, -1, 2, 1, -5, 4];
    assert_eq!(max_subarray(&nums), 6);
    assert_eq!(max_subarray(&[-1, -2, -3]), -1);
    println!("[Rust Kadane] Maximum subarray sum verified: 6");
}
