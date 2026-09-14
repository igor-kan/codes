func selectionSort<T: Comparable>(_ arr: [T]) -> [T] {
    var a = arr
    for i in 0..<a.count - 1 {
        var minIdx = i
        for j in i + 1..<a.count {
            if a[j] < a[minIdx] { minIdx = j }
        }
        a.swapAt(i, minIdx)
    }
    return a
}

let data = [33, 7, 91, 12, 5, 5, 78, 2, 44, 19]
let sorted = selectionSort(data)
assert(sorted == data.sorted())
print("[Swift SelectionSort] Selection sort verified: \(sorted)")
