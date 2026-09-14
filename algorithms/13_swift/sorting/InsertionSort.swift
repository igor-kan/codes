func insertionSort<T: Comparable>(_ arr: [T]) -> [T] {
    var a = arr
    for i in 1..<a.count {
        let key = a[i]
        var j = i - 1
        while j >= 0 && a[j] > key {
            a[j + 1] = a[j]
            j -= 1
        }
        a[j + 1] = key
    }
    return a
}

let data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19]
let sorted = insertionSort(data)
assert(sorted == data.sorted())
print("[Swift InsertionSort] Insertion sort verified: \(sorted)")
