func lis(_ arr: [Int]) -> Int {
    let n = arr.count
    if n == 0 { return 0 }
    var dp = Array(repeating: 1, count: n)
    for i in 1..<n {
        for j in 0..<i {
            if arr[j] < arr[i] { dp[i] = max(dp[i], dp[j] + 1) }
        }
    }
    return dp.max()!
}

assert(lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4)
assert(lis([]) == 0)
print("[Swift LIS] Longest increasing subsequence verified")
