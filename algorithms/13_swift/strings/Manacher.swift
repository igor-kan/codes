func manacher(_ s: String) -> Int {
    let chars = Array(s)
    let t = "#" + chars.map { String($0) }.joined(separator: "#") + "#"
    let tArr = Array(t)
    let n = tArr.count
    var p = Array(repeating: 0, count: n)
    var c = 0, r = 0
    for i in 0..<n {
        if i < r { p[i] = min(r - i, p[2 * c - i]) }
        while i + p[i] + 1 < n && i - p[i] - 1 >= 0 &&
              tArr[i + p[i] + 1] == tArr[i - p[i] - 1] {
            p[i] += 1
        }
        if i + p[i] > r { c = i; r = i + p[i] }
    }
    return p.max() ?? 0
}

assert(manacher("abba") == 4)
assert(manacher("racecar") == 7)
print("[Swift Manacher] Longest palindromic substring verified")
