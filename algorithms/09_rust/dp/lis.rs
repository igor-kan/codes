//! Longest Increasing Subsequence in O(n log n) in Rust.

pub fn lis(nums: &[i64]) -> usize {
    let mut tails: Vec<i64> = Vec::new();
    for &x in nums {
        let mut lo = 0usize;
        let mut hi = tails.len();
        while lo < hi {
            let mid = (lo + hi) / 2;
            if tails[mid] < x {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        if lo == tails.len() {
            tails.push(x);
        } else {
            tails[lo] = x;
        }
    }
    tails.len()
}

fn main() {
    let nums = [10i64, 9, 2, 5, 3, 7, 101, 18];
    assert_eq!(lis(&nums), 4);
    assert_eq!(lis(&[1, 2, 3, 4]), 4);
    assert_eq!(lis(&[4, 3, 2, 1]), 1);
    println!("[Rust LIS] O(n log n) length verified: 4");
}
