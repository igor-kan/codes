// Binary max-heap.
func pushHeap(_ a: inout [Int], _ v: Int) {
    a.append(v)
    var i = a.count - 1
    while i > 0 {
        let p = (i - 1) / 2
        if a[p] >= a[i] { break }
        a.swapAt(p, i)
        i = p
    }
}

func popHeap(_ a: inout [Int]) -> Int {
    let top = a[0]
    let last = a.removeLast()
    if !a.isEmpty {
        a[0] = last
        var i = 0
        while true {
            let l = 2 * i + 1
            let r = 2 * i + 2
            var b = i
            if l < a.count && a[l] > a[b] { b = l }
            if r < a.count && a[r] > a[b] { b = r }
            if b == i { break }
            a.swapAt(i, b)
            i = b
        }
    }
    return top
}

var heap: [Int] = []
for v in [5, 3, 8, 1, 4] { pushHeap(&heap, v) }
var previous = Int.max
while !heap.isEmpty {
    let x = popHeap(&heap)
    if x > previous { fatalError("not a max-heap order") }
    previous = x
}
print("max heap ok")
