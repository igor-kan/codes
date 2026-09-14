fun lis(arr: IntArray): Int {
    val n = arr.size
    if (n == 0) return 0
    val dp = IntArray(n) { 1 }
    for (i in 1 until n)
        for (j in 0 until i)
            if (arr[j] < arr[i]) dp[i] = maxOf(dp[i], dp[j] + 1)
    return dp.max()
}

fun main() {
    check(lis(intArrayOf(10, 9, 2, 5, 3, 7, 101, 18)) == 4)
    check(lis(intArrayOf()) == 0)
    println("[Kotlin LIS] Longest increasing subsequence verified")
}
