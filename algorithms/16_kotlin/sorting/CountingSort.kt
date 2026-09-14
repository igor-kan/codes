fun countingSort(arr: IntArray): IntArray {
    if (arr.isEmpty()) return IntArray(0)
    val maxVal = arr.max()
    val count = IntArray(maxVal + 1)
    for (x in arr) count[x]++
    for (i in 1..maxVal) count[i] += count[i - 1]
    val out = IntArray(arr.size)
    for (x in arr.reversed()) {
        count[x]--
        out[count[x]] = x
    }
    return out
}

fun main() {
    val data = intArrayOf(4, 2, 2, 8, 3, 3, 1)
    val sorted = countingSort(data)
    check(sorted.contentEquals(data.sortedArray()))
    println("[Kotlin CountingSort] Counting sort verified: ${sorted.joinToString(", ")}")
}
