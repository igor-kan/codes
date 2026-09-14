func binarySearch<T: Comparable>(_ arr: [T], _ target: T) -> Int {
    var lo = 0, hi = arr.count - 1
    while lo <= hi {
        let mid = (lo + hi) / 2
        if arr[mid] == target { return mid }
        else if arr[mid] < target { lo = mid + 1 }
        else { hi = mid - 1 }
    }
    return -1
}

let arr = [1, 3, 5, 7, 9, 11, 13]
assert(binarySearch(arr, 7) == 3)
assert(binarySearch(arr, 8) == -1)
assert(binarySearch(arr, 1) == 0)
print("[Swift BinarySearch] Binary search verified")
