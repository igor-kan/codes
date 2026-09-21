use modern_scientific_rust::fft::{fft_radix2, Complex};

#[test]
fn test_fft_roundtrip() {
    let orig = vec![
        Complex::new(1.0, 0.0),
        Complex::new(2.0, 0.0),
        Complex::new(3.0, 0.0),
        Complex::new(4.0, 0.0),
    ];
    let mut data = orig.clone();
    fft_radix2(&mut data, false);
    fft_radix2(&mut data, true);

    for (c, o) in data.iter().zip(orig.iter()) {
        assert!((c.re - o.re).abs() < 1e-12);
        assert!((c.im - o.im).abs() < 1e-12);
    }
}
