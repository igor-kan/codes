func bubbleSort<T: Comparable>(_ arr: [T]) -> [T] {
    var a = arr
    for i in 0..<a.count { for j in 0..<a.count-i-1 { if a[j]>a[j+1] { a.swapAt(j,j+1) } } }
    return a
}