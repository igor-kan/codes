use modern_scientific_rust::quaternion::Quaternion;

#[test]
fn test_quaternion_rotation() {
    // 90 degree rotation around Z axis rotates (1, 0, 0) to (0, 1, 0)
    let q = Quaternion::from_axis_angle([0.0, 0.0, 1.0], std::f64::consts::FRAC_PI_2);
    let v = [1.0, 0.0, 0.0];
    let v_rot = q.rotate_vector(v);

    assert!(v_rot[0].abs() < 1e-12);
    assert!((v_rot[1] - 1.0).abs() < 1e-12);
    assert!(v_rot[2].abs() < 1e-12);
}
