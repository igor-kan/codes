//! Binary search: lower_bound / upper_bound and binary search on answer in Rust.

pub fn lower_bound(a: &[i64], x: i64) -> usize {
    let (mut lo, mut hi) = (0usize, a.len());
    while lo < hi {
        let mid = (lo + hi) / 2;
        if a[mid] < x {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    lo
}

pub fn upper_bound(a: &[i64], x: i64) -> usize {
    let (mut lo, mut hi) = (0usize, a.len());
    while lo < hi {
        let mid = (lo + hi) / 2;
        if a[mid] <= x {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    lo
}

fn feasible(cap: i64) -> bool {
    let workloads = [3i64, 2, 2, 4, 1, 4];
    let mut groups = 0;
    let mut cur = 0;
    for &w in &workloads {
        if w > cap {
            return false;
        }
        if cur + w > cap {
            groups += 1;
            cur = w;
        } else {
            cur += w;
        }
    }
    groups += 1;
    groups <= 3
}

fn main() {
    let a = [1i64, 2, 2, 3, 3, 3, 5];
    assert_eq!(lower_bound(&a, 3), 3);
    assert_eq!(lower_bound(&a, 0), 0);
    assert_eq!(lower_bound(&a, 6), 7);
    assert_eq!(upper_bound(&a, 3), 6);
    assert_eq!(upper_bound(&a, 0), 0);
    assert_eq!(upper_bound(&a, 5), 7);

    let (mut lo, mut hi) = (0i64, 16i64);
    while lo < hi {
        let mid = (lo + hi) / 2;
        if feasible(mid) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    assert_eq!(lo, 6);
    println!("[Rust BinarySearch] lower_bound/upper_bound + answer search verified.");
}
