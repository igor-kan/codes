fun manacher(s: String): Int {
    val t = s.toList().joinToString(separator = "#", prefix = "#", postfix = "#")
    val n = t.length
    val p = IntArray(n)
    var c = 0
    var r = 0
    for (i in 0 until n) {
        if (i < r) p[i] = minOf(r - i, p[2 * c - i])
        while (i + p[i] + 1 < n && i - p[i] - 1 >= 0 &&
               t[i + p[i] + 1] == t[i - p[i] - 1])
            p[i]++
        if (i + p[i] > r) { c = i; r = i + p[i] }
    }
    return p.max()
}

fun main() {
    check(manacher("abba") == 4)
    check(manacher("racecar") == 7)
    println("[Kotlin Manacher] Longest palindromic substring verified")
}
