fun selectionSort(arr: IntArray): IntArray {
    val a = arr.copyOf()
    for (i in 0 until a.size - 1) {
        var minIdx = i
        for (j in i + 1 until a.size) if (a[j] < a[minIdx]) minIdx = j
        val tmp = a[i]; a[i] = a[minIdx]; a[minIdx] = tmp
    }
    return a
}

fun main() {
    val data = intArrayOf(33, 7, 91, 12, 5, 5, 78, 2, 44, 19)
    val sorted = selectionSort(data)
    check(sorted.contentEquals(data.sortedArray()))
    println("[Kotlin SelectionSort] Selection sort verified: ${sorted.joinToString(", ")}")
}
