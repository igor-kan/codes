fun zAlgorithm(s: String): IntArray {
    val n = s.length
    val z = IntArray(n)
    if (n > 0) z[0] = n
    var l = 0
    var r = 0
    for (i in 1 until n) {
        if (i <= r) z[i] = minOf(r - i + 1, z[i - l])
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++
        if (i + z[i] - 1 > r) { l = i; r = i + z[i] - 1 }
    }
    return z
}

fun main() {
    check(zAlgorithm("abacaba").contentEquals(intArrayOf(7, 0, 1, 0, 3, 0, 1)))
    println("[Kotlin ZAlgorithm] Z-algorithm verified")
}
