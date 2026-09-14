fun computeLPS(pattern: String): IntArray {
    val lps = IntArray(pattern.length)
    var len = 0; var i = 1
    while (i < pattern.length) {
        if (pattern[i] == pattern[len]) { len++; lps[i] = len; i++ }
        else if (len != 0) len = lps[len - 1]
        else { lps[i] = 0; i++ }
    }
    return lps
}
fun kmpSearch(text: String, pattern: String): List<Int> {
    if (pattern.isEmpty()) return listOf(0)
    val lps = computeLPS(pattern); val res = mutableListOf<Int>()
    var i = 0; var j = 0
    while (i < text.length) {
        if (pattern[j] == text[i]) { i++; j++ }
        if (j == pattern.length) { res += i - j; j = lps[j - 1] }
        else if (i < text.length && pattern[j] != text[i]) { if (j != 0) j = lps[j - 1] else i++ }
    }
    return res
}
fun main() {
    println("[Kotlin KMP] Testing KMP string matching")
    println("Pattern at: ${kmpSearch("ABABDABACDABABCABAB", "ABABCABAB")} (expected [10])")
    println("Pattern at: ${kmpSearch("AAAA", "AA")} (expected [0, 1, 2])")
    println("Pattern at: ${kmpSearch("HELLO WORLD", "WORLD")} (expected [6])")
    println("[Kotlin KMP] Test completed.")
}