// Catalan numbers by the recurrence.
var catalan = [Int](repeating: 0, count: 11)
catalan[0] = 1
for i in 1...10 {
    var sum = 0
    for j in 0..<i { sum += catalan[j] * catalan[i - 1 - j] }
    catalan[i] = sum
}
assert(catalan[5] == 42 && catalan[10] == 16796)
print("catalan(10)=\(catalan[10])")
