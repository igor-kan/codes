//! Jacobi eigenvalue algorithm for real symmetric matrices.
fn jacobi_eigenvalue(mut a: Vec<Vec<f64>>) -> Vec<f64> {
    let n = a.len();
    let mut vectors = vec![vec![0.0; n]; n];
    for i in 0..n {
        vectors[i][i] = 1.0;
    }
    for _ in 0..100 {
        let (mut p, mut q, mut largest) = (0, 1, 0.0f64);
        for i in 0..n {
            for j in (i + 1)..n {
                if a[i][j].abs() > largest {
                    largest = a[i][j].abs();
                    p = i;
                    q = j;
                }
            }
        }
        if largest < 1e-12 {
            break;
        }
        let theta = 0.5 * (2.0 * a[p][q]).atan2(a[q][q] - a[p][p]);
        let (c, s) = (theta.cos(), theta.sin());
        for k in 0..n {
            let (akp, akq) = (a[k][p], a[k][q]);
            a[k][p] = c * akp - s * akq;
            a[k][q] = s * akp + c * akq;
        }
        for k in 0..n {
            let (apk, aqk) = (a[p][k], a[q][k]);
            a[p][k] = c * apk - s * aqk;
            a[q][k] = s * apk + c * aqk;
        }
        for k in 0..n {
            let (vkp, vkq) = (vectors[k][p], vectors[k][q]);
            vectors[k][p] = c * vkp - s * vkq;
            vectors[k][q] = s * vkp + c * vkq;
        }
    }
    (0..n).map(|i| a[i][i]).collect()
}

fn main() {
    let eigenvalues = jacobi_eigenvalue(vec![
        vec![4.0, 1.0, 0.0],
        vec![1.0, 3.0, 1.0],
        vec![0.0, 1.0, 2.0],
    ]);
    let sum: f64 = eigenvalues.iter().sum();
    let product: f64 = eigenvalues.iter().product();
    assert!((sum - 9.0).abs() < 1e-9 && (product - 18.0).abs() < 1e-9);
    println!("jacobi eigenvalue ok");
}
