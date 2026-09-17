// Brent's Root Finding in Swift (Numerical Recipes 3rd Ed. Chapter 9.3)
import Foundation

func brentRoot(_ f: (Double) -> Double, _ aIn: Double, _ bIn: Double, tol: Double = 1e-10, maxIter: Int = 100) -> Double {
    var a = aIn
    var b = bIn
    var fa = f(a)
    var fb = f(b)
    assert(fa * fb <= 0.0)

    if abs(fa) < abs(fb) {
        swap(&a, &b)
        swap(&fa, &fb)
    }

    var c = a, fc = fa, mflag = true, s = b, d = 0.0

    for _ in 0..<maxIter {
        if abs(fb) < tol || abs(b - a) < tol { return b }

        if fa != fc && fb != fc {
            s = (a * fb * fc) / ((fa - fb) * (fa - fc)) +
                (b * fa * fc) / ((fb - fa) * (fb - fc)) +
                (c * fa * fb) / ((fc - fa) * (fc - fb))
        } else {
            s = b - fb * (b - a) / (fb - fa)
        }

        let c1 = (s - (3 * a + b) / 4) * (s - b) > 0
        let c2 = mflag && abs(s - b) >= abs(b - c) / 2
        let c3 = !mflag && abs(s - b) >= abs(c - d) / 2

        if c1 || c2 || c3 {
            s = (a + b) / 2
            mflag = true
        } else {
            mflag = false
        }

        let fs = f(s)
        d = c; c = b; fc = fb
        if fa * fs < 0 { b = s; fb = fs } else { a = s; fa = fs }

        if abs(fa) < abs(fb) {
            swap(&a, &b)
            swap(&fa, &fb)
        }
    }
    return b
}

let r = brentRoot({ $0 * $0 - 2.0 }, 0.0, 2.0)
assert(abs(r - sqrt(2.0)) < 1e-6)
print("Swift Brent Root Finding verified.")
