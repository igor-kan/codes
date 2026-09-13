pub fn quick_sort(a: &mut [i64]) {
    if a.len()<=1 { return; }
    let p=partition(a); let (l,r)=a.split_at_mut(p);
    quick_sort(l); quick_sort(&mut r[1..]);
}
fn partition(a: &mut [i64]) -> usize {
    let n=a.len(); let pivot=a[n/2]; let mut i=0;
    a.swap(n/2,n-1);
    for j in 0..n-1 { if a[j]<=pivot { a.swap(i,j); i+=1; } }
    a.swap(i,n-1); i
}