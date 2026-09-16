fn missing_number(nums: &[i32]) -> i32 {
    let n = nums.len() as i32;
    n * (n + 1) / 2 - nums.iter().sum::<i32>()
}

fn main() {
    assert_eq!(missing_number(&[3, 0, 1]), 2);
    assert_eq!(missing_number(&[9, 6, 4, 2, 3, 5, 7, 0, 1]), 8);
    println!("268 missing number ok");
}
