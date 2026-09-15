//! Quickselect: expected linear-time order statistic (CLRS 9.2).
fn quickselect(mut a: Vec<i32>, k: usize) -> i32 {
    let (mut lo, mut hi) = (0usize, a.len() - 1);
    loop {
        let pivot = a[hi];
        let mut i = lo;
        for j in lo..hi {
            if a[j] < pivot {
                a.swap(i, j);
                i += 1;
            }
        }
        a.swap(i, hi);
        if i == k {
            return a[i];
        }
        if k < i {
            hi = i - 1;
        } else {
            lo = i + 1;
        }
    }
}

fn main() {
    let data = vec![3, 2, 1, 5, 6, 4];
    let mut sorted = data.clone();
    sorted.sort();
    for k in 0..data.len() {
        assert_eq!(quickselect(data.clone(), k), sorted[k]);
    }
    println!("quickselect ok");
}
