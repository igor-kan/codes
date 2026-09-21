use modern_scientific_rust::lu_decomp::{lu_factor, lu_solve};

#[test]
fn test_lu_solver() {
    let mut a = vec![2.0, 1.0, -1.0,
                     -3.0, -1.0, 2.0,
                     -2.0, 1.0, 2.0];
    let b = vec![8.0, -11.0, -3.0];
    let piv = lu_factor(&mut a, 3).unwrap();
    let x = lu_solve(&a, &piv, &b, 3);

    assert!((x[0] - 2.0).abs() < 1e-10);
    assert!((x[1] - 3.0).abs() < 1e-10);
    assert!((x[2] - (-1.0)).abs() < 1e-10);
}
