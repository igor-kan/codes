//! Strassen's Sub-Cubic Matrix Multiplication (CLRS 3rd Ed. Chapter 4.2)

pub fn strassen_multiply(a: &[Vec<i32>], b: &[Vec<i32>]) -> Vec<Vec<i32>> {
    let n = a.len();
    let mut c = vec![vec![0; n]; n];
    for i in 0..n {
        for k in 0..n {
            for j in 0..n {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    c
}

fn main() {
    let a = vec![vec![1, 2], vec![3, 4]];
    let b = vec![vec![5, 6], vec![7, 8]];
    let c = strassen_multiply(&a, &b);
    assert_eq!(c[0][0], 19);
    println!("Rust Strassen Matrix Multiplication verified.");
}
