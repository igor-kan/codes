func countingSort(_ arr: [Int]) -> [Int] {
    guard let maxVal = arr.max() else { return [] }
    var count = Array(repeating: 0, count: maxVal + 1)
    for x in arr { count[x] += 1 }
    for i in 1...maxVal { count[i] += count[i - 1] }
    var out = Array(repeating: 0, count: arr.count)
    for x in arr.reversed() {
        count[x] -= 1
        out[count[x]] = x
    }
    return out
}

let data = [4, 2, 2, 8, 3, 3, 1]
let sorted = countingSort(data)
assert(sorted == data.sorted())
print("[Swift CountingSort] Counting sort verified: \(sorted)")
