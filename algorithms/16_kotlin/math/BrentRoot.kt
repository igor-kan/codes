package math

import kotlin.math.abs

fun brentRoot(f: (Double) -> Double, aIn: Double, bIn: Double, tol: Double = 1e-10, maxIter: Int = 100): Double {
    var a = aIn
    var b = bIn
    var fa = f(a)
    var fb = f(b)
    require(fa * fb <= 0.0) { "Root not bracketed" }

    if (abs(fa) < abs(fb)) {
        a = b.also { b = a }
        fa = fb.also { fb = fa }
    }

    var c = a
    var fc = fa
    var mflag = true
    var s = b
    var d = 0.0

    for (iter in 0 until maxIter) {
        if (abs(fb) < tol || abs(b - a) < tol) return b

        s = if (fa != fc && fb != fc) {
            (a * fb * fc) / ((fa - fb) * (fa - fc)) +
            (b * fa * fc) / ((fb - fa) * (fb - fc)) +
            (c * fa * fb) / ((fc - fa) * (fc - fb))
        } else {
            b - fb * (b - a) / (fb - fa)
        }

        val c1 = (s - (3 * a + b) / 4) * (s - b) > 0
        val c2 = mflag && abs(s - b) >= abs(b - c) / 2
        val c3 = !mflag && abs(s - b) >= abs(c - d) / 2

        s = if (c1 || c2 || c3) {
            mflag = true
            (a + b) / 2
        } else {
            mflag = false
            s
        }

        val fs = f(s)
        d = c; c = b; fc = fb
        if (fa * fs < 0) { b = s; fb = fs } else { a = s; fa = fs }

        if (abs(fa) < abs(fb)) {
            a = b.also { b = a }
            fa = fb.also { fb = fa }
        }
    }
    return b
}

fun main() {
    val r = brentRoot({ x -> x * x - 2.0 }, 0.0, 2.0)
    assert(abs(r - Math.sqrt(2.0)) < 1e-6)
    println("Kotlin Brent Root verified.")
}
