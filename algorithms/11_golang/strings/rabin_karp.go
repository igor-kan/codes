package strings
func RabinKarp(text, pattern string) []int {
    matches := []int{}
    n, m := len(text), len(pattern)
    if m == 0 || m > n { return matches }
    d, q := 256, 1000000007
    h := 1
    for i := 0; i < m-1; i++ { h = (h * d) % q }
    pHash, tHash := 0, 0
    for i := 0; i < m; i++ {
        pHash = (d*pHash + int(pattern[i])) % q
        tHash = (d*tHash + int(text[i])) % q
    }
    for i := 0; i <= n-m; i++ {
        if pHash == tHash && text[i:i+m] == pattern { matches = append(matches, i) }
        if i < n-m {
            tHash = (d*(tHash-int(text[i])*h) + int(text[i+m])) % q
            if tHash < 0 { tHash += q }
        }
    }
    return matches
}
