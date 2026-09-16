fn move_zeroes(nums: &[i32]) -> Vec<i32> {
    let mut result: Vec<i32> = nums.iter().copied().filter(|&number| number != 0).collect();
    while result.len() < nums.len() { result.push(0); }
    result
}

fn main() {
    assert_eq!(move_zeroes(&[0, 1, 0, 3, 12]), vec![1, 3, 12, 0, 0]);
    assert_eq!(move_zeroes(&[0]), vec![0]);
    println!("283 move zeroes ok");
}
