fn remove_duplicates(nums: &[i32]) -> Vec<i32> {
    let mut result: Vec<i32> = Vec::new();
    for &value in nums {
        if result.last() != Some(&value) { result.push(value); }
    }
    result
}

fn main() {
    assert_eq!(remove_duplicates(&[1, 1, 2]), vec![1, 2]);
    assert_eq!(remove_duplicates(&[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), vec![0, 1, 2, 3, 4]);
    println!("26 remove duplicates ok");
}
