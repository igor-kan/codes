fn sift_down(a: &mut [i64], mut root: usize, end: usize) {
    loop {
        let mut swap = root;
        let left = 2 * root + 1;
        let right = left + 1;
        if left <= end && a[swap] < a[left] {
            swap = left;
        }
        if right <= end && a[swap] < a[right] {
            swap = right;
        }
        if swap == root {
            return;
        }
        a.swap(root, swap);
        root = swap;
    }
}

pub fn heap_sort(a: &mut [i64]) {
    let n = a.len();
    if n <= 1 {
        return;
    }
    for start in (0..=(n - 2) / 2).rev() {
        sift_down(a, start, n - 1);
    }
    for end in (1..n).rev() {
        a.swap(0, end);
        sift_down(a, 0, end - 1);
    }
}

fn main() {
    let mut data = [33i64, 7, 91, 12, 5, 5, 78, 2, 44, 19];
    heap_sort(&mut data);
    assert_eq!(data, [2, 5, 5, 7, 12, 19, 33, 44, 78, 91]);
    println!("[Rust HeapSort] Sift-down heap sort verified: {:?}", data);
}
