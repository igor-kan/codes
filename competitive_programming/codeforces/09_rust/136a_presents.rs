fn presents(permutation: &[usize]) -> Vec<usize> {
    let mut result = vec![0; permutation.len()];
    for (index, &giver) in permutation.iter().enumerate() {
        result[giver - 1] = index + 1;
    }
    result
}

fn main() {
    assert_eq!(presents(&[2, 3, 4, 1]), vec![4, 1, 2, 3]);
    println!("136A presents ok");
}
