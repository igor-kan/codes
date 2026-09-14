//! LSD radix sort for `u32` values.
fn radix_sort(values: &mut [u32]) {
    if values.is_empty() {
        return;
    }
    let max = *values.iter().max().unwrap();
    let mut exp = 1u32;
    let mut buffer = vec![0u32; values.len()];
    while max / exp > 0 {
        let mut counts = [0usize; 10];
        for &value in values.iter() {
            counts[((value / exp) % 10) as usize] += 1;
        }
        for i in 1..10 {
            counts[i] += counts[i - 1];
        }
        for &value in values.iter().rev() {
            let digit = ((value / exp) % 10) as usize;
            counts[digit] -= 1;
            buffer[counts[digit]] = value;
        }
        values.copy_from_slice(&buffer);
        exp *= 10;
    }
}

fn main() {
    let mut data = [170u32, 45, 75, 90, 802, 24, 2, 66];
    radix_sort(&mut data);
    assert!(data.windows(2).all(|w| w[0] <= w[1]));
    println!("{data:?}");
}
