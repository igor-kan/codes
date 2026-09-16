fn search_insert(nums: &[i32], target: i32) -> i32 {
    let (mut low, mut high) = (0usize, nums.len());
    while low < high {
        let middle = (low + high) / 2;
        if nums[middle] < target { low = middle + 1; } else { high = middle; }
    }
    low as i32
}

fn main() {
    assert_eq!(search_insert(&[1, 3, 5, 6], 5), 2);
    assert_eq!(search_insert(&[1, 3, 5, 6], 2), 1);
    assert_eq!(search_insert(&[1, 3, 5, 6], 7), 4);
    assert_eq!(search_insert(&[1, 3, 5, 6], 0), 0);
    println!("35 search insert position ok");
}
