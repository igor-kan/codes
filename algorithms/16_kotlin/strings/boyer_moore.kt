// Boyer-Moore-Horspool substring search.
fun boyerMoore(text: String, pattern: String): Int {
    val n = text.length
    val m = pattern.length
    val skip = IntArray(256) { m }
    for (i in 0 until m - 1) skip[pattern[i].code] = m - 1 - i
    var i = 0
    while (i + m <= n) {
        var j = m - 1
        while (j >= 0 && text[i + j] == pattern[j]) j--
        if (j < 0) return i
        i += skip[text[i + m - 1].code]
    }
    return -1
}

fun main() {
    check(boyerMoore("here is a simple example", "example") == 17) { "search failed" }
    check(boyerMoore("abc", "xyz") == -1) { "search failed" }
    println("boyer-moore ok")
}
