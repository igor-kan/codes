// Binary max-heap.
fun pushHeap(a: MutableList<Int>, v: Int) {
    a.add(v)
    var i = a.size - 1
    while (i > 0) {
        val p = (i - 1) / 2
        if (a[p] >= a[i]) break
        val t = a[p]; a[p] = a[i]; a[i] = t
        i = p
    }
}

fun popHeap(a: MutableList<Int>): Int {
    val top = a[0]
    val last = a.removeAt(a.size - 1)
    if (a.isNotEmpty()) {
        a[0] = last
        var i = 0
        while (true) {
            val l = 2 * i + 1
            val r = 2 * i + 2
            var b = i
            if (l < a.size && a[l] > a[b]) b = l
            if (r < a.size && a[r] > a[b]) b = r
            if (b == i) break
            val t = a[i]; a[i] = a[b]; a[b] = t
            i = b
        }
    }
    return top
}

fun main() {
    val heap = mutableListOf<Int>()
    for (v in intArrayOf(5, 3, 8, 1, 4)) pushHeap(heap, v)
    var previous = Int.MAX_VALUE
    while (heap.isNotEmpty()) {
        val x = popHeap(heap)
        check(x <= previous) { "not a max-heap order" }
        previous = x
    }
    println("max heap ok")
}
