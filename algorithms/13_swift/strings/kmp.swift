func computeLPS(_ pattern: String) -> [Int] {
    let p=Array(pattern), m=p.count
    var lps=Array(repeating:0,count:m), len=0, i=1
    while i<m { if p[i]==p[len] { len+=1; lps[i]=len; i+=1 }
        else if len>0 { len=lps[len-1] } else { lps[i]=0; i+=1 } }
    return lps
}
func kmpSearch(_ text: String, _ pattern: String) -> [Int] {
    let t=Array(text), p=Array(pattern), n=t.count, m=p.count
    if m==0 { return [0] }
    let lps=computeLPS(pattern); var res=[Int](), i=0, j=0
    while i<n { if p[j]==t[i] { i+=1; j+=1 }
        if j==m { res.append(i-j); j=lps[j-1] }
        else if i<n && p[j] != t[i] { if j>0 { j=lps[j-1] } else { i+=1 } } }
    return res
}
print("[Swift KMP] Testing KMP string matching")
print("Pattern at: \(kmpSearch("ABABDABACDABABCABAB", "ABABCABAB")) (expected [10])")
print("Pattern at: \(kmpSearch("AAAA", "AA")) (expected [0, 1, 2])")
print("Pattern at: \(kmpSearch("HELLO WORLD", "WORLD")) (expected [6])")
print("[Swift KMP] Test completed.")