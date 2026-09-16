fn binary_search(nums: &[i32], target: i32) -> i32 {
    let (mut low, mut high) = (0i32, nums.len() as i32 - 1);
    while low <= high {
        let middle = (low + high) / 2;
        if nums[middle as usize] == target { return middle; }
        if nums[middle as usize] < target { low = middle + 1; } else { high = middle - 1; }
    }
    -1
}

fn main() {
    assert_eq!(binary_search(&[-1, 0, 3, 5, 9, 12], 9), 4);
    assert_eq!(binary_search(&[-1, 0, 3, 5, 9, 12], 2), -1);
    println!("704 binary search ok");
}
