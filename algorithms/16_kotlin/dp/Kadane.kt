fun kadane(arr: IntArray): Int {
    var best = arr[0]
    var cur = arr[0]
    for (i in 1 until arr.size) {
        cur = maxOf(arr[i], cur + arr[i])
        best = maxOf(best, cur)
    }
    return best
}

fun main() {
    check(kadane(intArrayOf(-2, 1, -3, 4, -1, 2, 1, -5, 4)) == 6)
    check(kadane(intArrayOf(-5, -2, -3)) == -2)
    println("[Kotlin Kadane] Maximum subarray sum verified")
}
