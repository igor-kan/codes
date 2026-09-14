//! Prefix sums technique in Rust.

pub fn prefix_sums(nums: &[i64]) -> Vec<i64> {
    let mut pref = vec![0i64; nums.len() + 1];
    for (i, &v) in nums.iter().enumerate() {
        pref[i + 1] = pref[i] + v;
    }
    pref
}

pub fn range_sum(pref: &[i64], l: usize, r: usize) -> i64 {
    pref[r + 1] - pref[l]
}

fn main() {
    let nums = [3i64, 1, 4, 1, 5, 9, 2, 6];
    let pref = prefix_sums(&nums);
    assert_eq!(range_sum(&pref, 2, 4), 10);
    assert_eq!(range_sum(&pref, 0, nums.len() - 1), 31);
    println!("[Rust PrefixSum] Range sum queries verified.");
}
