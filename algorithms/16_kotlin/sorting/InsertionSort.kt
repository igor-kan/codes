fun insertionSort(arr: IntArray): IntArray {
    val a = arr.copyOf()
    for (i in 1 until a.size) {
        val key = a[i]
        var j = i - 1
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j]
            j--
        }
        a[j + 1] = key
    }
    return a
}

fun main() {
    val data = intArrayOf(33, 7, 91, 12, 5, 5, 78, 2, 44, 19)
    val sorted = insertionSort(data)
    check(sorted.contentEquals(data.sortedArray()))
    println("[Kotlin InsertionSort] Insertion sort verified: ${sorted.joinToString(", ")}")
}
