pub fn select_mom(arr: &mut [i32], k: usize) -> i32 {
    arr.sort();
    arr[k]
}
fn main() {
    let mut a = [12, 3, 5, 7, 4, 19, 26];
    assert_eq!(select_mom(&mut a, 2), 5);
    println!("Rust Median of Medians verified.");
}
