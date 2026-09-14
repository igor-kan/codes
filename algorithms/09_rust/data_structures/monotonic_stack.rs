//! Monotonic stack (next greater element) in Rust.

pub fn next_greater(nums: &[i64]) -> Vec<i64> {
    let n = nums.len();
    let mut res = vec![-1; n];
    let mut stack: Vec<usize> = Vec::new();
    for i in 0..n {
        while let Some(&top) = stack.last() {
            if nums[top] < nums[i] {
                res[top] = nums[i];
                stack.pop();
            } else {
                break;
            }
        }
        stack.push(i);
    }
    res
}

fn main() {
    let nums = [2i64, 1, 2, 4, 3];
    let got = next_greater(&nums);
    assert_eq!(got, vec![4, 2, 4, -1, -1]);
    println!("[Rust MonotonicStack] Next greater element verified: {:?}", got);
}
