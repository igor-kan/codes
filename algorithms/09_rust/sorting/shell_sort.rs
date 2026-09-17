pub fn shell_sort(arr: &mut [i32]) {
    let n = arr.len();
    let mut h = 1;
    while h < n / 3 { h = 3 * h + 1; }
    while h >= 1 {
        for i in h..n {
            let temp = arr[i];
            let mut j = i;
            while j >= h && arr[j - h] > temp {
                arr[j] = arr[j - h];
                j -= h;
            }
            arr[j] = temp;
        }
        h /= 3;
    }
}
fn main() {
    let mut a = [5, 2, 8, 1, 9];
    shell_sort(&mut a);
    assert_eq!(a, [1, 2, 5, 8, 9]);
    println!("Rust Shell Sort verified.");
}
