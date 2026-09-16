fn remove_element(nums: &[i32], value: i32) -> Vec<i32> {
    nums.iter().copied().filter(|&number| number != value).collect()
}

fn main() {
    assert_eq!(remove_element(&[3, 2, 2, 3], 3), vec![2, 2]);
    assert_eq!(remove_element(&[0, 1, 2, 2, 3, 0, 4, 2], 2), vec![0, 1, 3, 0, 4]);
    println!("27 remove element ok");
}
