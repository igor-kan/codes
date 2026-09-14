func kadane(_ arr: [Int]) -> Int {
    var best = arr[0], cur = arr[0]
    for x in arr.dropFirst() {
        cur = max(x, cur + x)
        best = max(best, cur)
    }
    return best
}

assert(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
assert(kadane([-5, -2, -3]) == -2)
print("[Swift Kadane] Maximum subarray sum verified")
