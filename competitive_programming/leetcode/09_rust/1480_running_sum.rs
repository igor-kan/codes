fn running_sum(nums: &[i32]) -> Vec<i32> {
    let mut total = 0;
    nums.iter().map(|&value| { total += value; total }).collect()
}

fn main() {
    assert_eq!(running_sum(&[1, 2, 3, 4]), vec![1, 3, 6, 10]);
    assert_eq!(running_sum(&[1, 1, 1, 1, 1]), vec![1, 2, 3, 4, 5]);
    println!("1480 running sum ok");
}
