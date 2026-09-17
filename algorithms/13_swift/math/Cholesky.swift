// Cholesky LL^T Decomposition in Swift (Numerical Recipes 3rd Ed. Chapter 2.6)
import Foundation

func cholesky(_ A: [[Double]]) -> [[Double]] {
    let n = A.count
    var L = Array(repeating: Array(repeating: 0.0, count: n), count: n)

    for i in 0..<n {
        for j in 0...i {
            var sum = 0.0
            for k in 0..<j { sum += L[i][k] * L[j][k] }
            if i == j {
                let v = A[i][i] - sum
                assert(v > 0)
                L[i][j] = sqrt(v)
            } else {
                L[i][j] = (A[i][j] - sum) / L[j][j]
            }
        }
    }
    return L
}

let A = [
    [4.0, 12.0, -16.0],
    [12.0, 37.0, -43.0],
    [-16.0, -43.0, 98.0]
]
let L = cholesky(A)
assert(abs(L[0][0] - 2.0) < 1e-6)
print("Swift Cholesky verified.")
