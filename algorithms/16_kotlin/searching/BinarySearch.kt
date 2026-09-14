fun binarySearch(arr: IntArray, target: Int): Int {
    var lo = 0
    var hi = arr.size - 1
    while (lo <= hi) {
        val mid = (lo + hi) / 2
        when {
            arr[mid] == target -> return mid
            arr[mid] < target -> lo = mid + 1
            else -> hi = mid - 1
        }
    }
    return -1
}

fun main() {
    val arr = intArrayOf(1, 3, 5, 7, 9, 11, 13)
    check(binarySearch(arr, 7) == 3)
    check(binarySearch(arr, 8) == -1)
    check(binarySearch(arr, 1) == 0)
    println("[Kotlin BinarySearch] Binary search verified")
}
