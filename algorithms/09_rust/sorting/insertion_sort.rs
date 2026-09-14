//! Insertion sort in Rust.

pub fn insertion_sort(a: &mut [i64]) {
    for i in 1..a.len() {
        let key = a[i];
        let mut j = i;
        while j > 0 && a[j - 1] > key {
            a[j] = a[j - 1];
            j -= 1;
        }
        a[j] = key;
    }
}

fn main() {
    let mut data = [33i64, 7, 91, 12, 5, 5, 78, 2, 44, 19];
    insertion_sort(&mut data);
    assert_eq!(data, [2, 5, 5, 7, 12, 19, 33, 44, 78, 91]);
    println!("[Rust InsertionSort] Insertion sort verified: {:?}", data);
}
