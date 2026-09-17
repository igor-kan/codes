pub fn comb_sort(arr: &mut [i32]) {
    let n = arr.len();
    let mut gap = n;
    let shrink = 1.3;
    let mut sorted = false;
    while !sorted {
        gap = (gap as f64 / shrink).floor() as usize;
        if gap <= 1 { gap = 1; sorted = true; }
        for i in 0..n - gap {
            if arr[i] > arr[i + gap] {
                arr.swap(i, i + gap);
                sorted = false;
            }
        }
    }
}
fn main() {
    let mut a = [8, 4, 1, 56, 3];
    comb_sort(&mut a);
    assert_eq!(a, [1, 3, 4, 8, 56]);
    println!("Rust Comb Sort verified.");
}
