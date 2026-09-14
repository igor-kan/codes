func zAlgorithm(_ s: String) -> [Int] {
    let chars = Array(s)
    let n = chars.count
    var z = Array(repeating: 0, count: n)
    if n > 0 { z[0] = n }
    var l = 0, r = 0
    for i in 1..<n {
        if i <= r { z[i] = min(r - i + 1, z[i - l]) }
        while i + z[i] < n && chars[z[i]] == chars[i + z[i]] { z[i] += 1 }
        if i + z[i] - 1 > r { l = i; r = i + z[i] - 1 }
    }
    return z
}

assert(zAlgorithm("abacaba") == [7, 0, 1, 0, 3, 0, 1])
print("[Swift ZAlgorithm] Z-algorithm verified")
