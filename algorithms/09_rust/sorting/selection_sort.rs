//! Selection sort in Rust.

pub fn selection_sort(a: &mut [i64]) {
    for i in 0..a.len() {
        let mut min_idx = i;
        for j in i + 1..a.len() {
            if a[j] < a[min_idx] {
                min_idx = j;
            }
        }
        a.swap(i, min_idx);
    }
}

fn main() {
    let mut data = [33i64, 7, 91, 12, 5, 5, 78, 2, 44, 19];
    selection_sort(&mut data);
    assert_eq!(data, [2, 5, 5, 7, 12, 19, 33, 44, 78, 91]);
    println!("[Rust SelectionSort] Selection sort verified: {:?}", data);
}
