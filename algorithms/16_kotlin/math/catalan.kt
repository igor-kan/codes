// Catalan numbers by the recurrence.
fun main() {
    val catalan = LongArray(11)
    catalan[0] = 1
    for (i in 1..10) {
        var sum = 0L
        for (j in 0 until i) sum += catalan[j] * catalan[i - 1 - j]
        catalan[i] = sum
    }
    check(catalan[5] == 42L && catalan[10] == 16796L) { "wrong Catalan numbers" }
    println("catalan(10)=${catalan[10]}")
}
