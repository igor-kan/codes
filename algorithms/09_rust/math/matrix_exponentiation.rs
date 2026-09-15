//! Fibonacci by matrix exponentiation.
type Mat = [[i64; 2]; 2];

fn mul(a: Mat, b: Mat) -> Mat {
    let mut r = [[0i64; 2]; 2];
    for i in 0..2 {
        for j in 0..2 {
            for k in 0..2 {
                r[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    r
}

fn fib(mut n: u32) -> i64 {
    let mut r: Mat = [[1, 0], [0, 1]];
    let mut m: Mat = [[1, 1], [1, 0]];
    while n > 0 {
        if n & 1 == 1 {
            r = mul(r, m);
        }
        m = mul(m, m);
        n >>= 1;
    }
    r[0][1]
}

fn main() {
    assert_eq!(fib(10), 55);
    assert_eq!(fib(20), 6765);
    println!("fib(20)={}", fib(20));
}
