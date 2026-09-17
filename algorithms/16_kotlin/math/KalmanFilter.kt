package math

class KalmanFilter1D(var x: Double, var p: Double, var q: Double, var r: Double) {
    fun predict() { p += q }
    fun update(z: Double): Double {
        val k = p / (p + r)
        x += k * (z - x)
        p = (1.0 - k) * p
        return x
    }
}

fun main() {
    val kf = KalmanFilter1D(0.0, 1.0, 0.01, 0.1)
    for (z in doubleArrayOf(0.9, 1.1, 0.95, 1.05)) {
        kf.predict()
        kf.update(z)
    }
    assert(Math.abs(kf.x - 1.0) < 0.2)
    println("Kotlin Kalman Filter verified.")
}
