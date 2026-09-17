package math

import kotlin.math.sqrt

fun cholesky(A: Array<DoubleArray>): Array<DoubleArray> {
    val n = A.size
    val L = Array(n) { DoubleArray(n) }

    for (i in 0 until n) {
        for (j in 0..i) {
            var sum = 0.0
            for (k in 0 until j) sum += L[i][k] * L[j][k]
            if (i == j) {
                val v = A[i][i] - sum
                require(v > 0) { "Not positive definite" }
                L[i][j] = sqrt(v)
            } else {
                L[i][j] = (A[i][j] - sum) / L[j][j]
            }
        }
    }
    return L
}

fun main() {
    val A = arrayOf(
        doubleArrayOf(4.0, 12.0, -16.0),
        doubleArrayOf(12.0, 37.0, -43.0),
        doubleArrayOf(-16.0, -43.0, 98.0)
    )
    val L = cholesky(A)
    assert(Math.abs(L[0][0] - 2.0) < 1e-6)
    println("Kotlin Cholesky verified.")
}
