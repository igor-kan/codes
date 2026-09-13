pub fn bubble_sort(a: &mut Vec<i64>) {
    let n = a.len();
    for i in 0..n { for j in 0..n-i-1 { if a[j]>a[j+1] { a.swap(j,j+1); } } }
}