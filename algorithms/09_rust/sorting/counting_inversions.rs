//! Count inversions with a modified merge sort (CLRS 2.4 style).
fn merge_count(a: &mut [i32], buf: &mut [i32], lo: usize, hi: usize) -> i64 {
    if hi - lo <= 1 {
        return 0;
    }
    let mid = (lo + hi) / 2;
    let mut inversions = merge_count(a, buf, lo, mid) + merge_count(a, buf, mid, hi);
    let (mut i, mut j, mut k) = (lo, mid, lo);
    while i < mid && j < hi {
        if a[i] <= a[j] {
            buf[k] = a[i];
            i += 1;
        } else {
            buf[k] = a[j];
            j += 1;
            inversions += (mid - i) as i64;
        }
        k += 1;
    }
    while i < mid {
        buf[k] = a[i];
        i += 1;
        k += 1;
    }
    while j < hi {
        buf[k] = a[j];
        j += 1;
        k += 1;
    }
    a[lo..hi].copy_from_slice(&buf[lo..hi]);
    inversions
}

fn count_inversions(mut a: Vec<i32>) -> i64 {
    let mut buf = a.clone();
    let n = a.len();
    merge_count(&mut a, &mut buf, 0, n)
}

fn main() {
    assert_eq!(count_inversions(vec![2, 4, 1, 3, 5]), 3);
    assert_eq!(count_inversions(vec![5, 4, 3, 2, 1]), 10);
    println!("counting inversions ok");
}
