// Boyer-Moore-Horspool substring search.
func boyerMoore(_ text: String, _ pattern: String) -> Int {
    let t = Array(text.utf8)
    let p = Array(pattern.utf8)
    let n = t.count
    let m = p.count
    var skip = [Int](repeating: m, count: 256)
    for i in 0..<(m - 1) { skip[Int(p[i])] = m - 1 - i }
    var i = 0
    while i + m <= n {
        var j = m - 1
        while j >= 0 && t[i + j] == p[j] { j -= 1 }
        if j < 0 { return i }
        i += skip[Int(t[i + m - 1])]
    }
    return -1
}

assert(boyerMoore("here is a simple example", "example") == 17)
assert(boyerMoore("abc", "xyz") == -1)
print("boyer-moore ok")
