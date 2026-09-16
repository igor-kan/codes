fn plus_one(digits: &[i32]) -> Vec<i32> {
    let mut result = digits.to_vec();
    for i in (0..result.len()).rev() {
        if result[i] < 9 { result[i] += 1; return result; }
        result[i] = 0;
    }
    let mut extended = vec![1];
    extended.extend(result);
    extended
}

fn main() {
    assert_eq!(plus_one(&[1, 2, 3]), vec![1, 2, 4]);
    assert_eq!(plus_one(&[9, 9]), vec![1, 0, 0]);
    println!("66 plus one ok");
}
