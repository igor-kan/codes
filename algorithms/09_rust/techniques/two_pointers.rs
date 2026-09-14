//! Two pointers technique in Rust.

pub fn two_sum_sorted(nums: &[i64], target: i64) -> Option<(usize, usize)> {
    let (mut i, mut j) = (0usize, nums.len() - 1);
    while i < j {
        let s = nums[i] + nums[j];
        if s == target {
            return Some((i, j));
        } else if s < target {
            i += 1;
        } else {
            j -= 1;
        }
    }
    None
}

fn main() {
    let nums = [-3i64, -1, 0, 2, 4, 7, 9];
    let (i, j) = two_sum_sorted(&nums, 6).expect("pair should exist");
    assert_eq!(nums[i] + nums[j], 6);
    println!("[Rust TwoPointers] Sorted two-sum verified: {} + {} = 6", nums[i], nums[j]);
}
