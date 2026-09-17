// 1D Kalman Filter in Swift (Numerical Recipes 3rd Ed. Chapter 15)

class KalmanFilter1D {
    var x: Double
    var p: Double
    var q: Double
    var r: Double

    init(x: Double, p: Double, q: Double, r: Double) {
        self.x = x; self.p = p; self.q = q; self.r = r
    }

    func predict() { p += q }
    func update(_ z: Double) -> Double {
        let k = p / (p + r)
        x += k * (z - x)
        p = (1.0 - k) * p
        return x
    }
}

let kf = KalmanFilter1D(x: 0, p: 1, q: 0.01, r: 0.1)
for z in [0.9, 1.1, 0.95, 1.05] {
    kf.predict()
    _ = kf.update(z)
}
assert(abs(kf.x - 1.0) < 0.2)
print("Swift Kalman Filter verified.")
