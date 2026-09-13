def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    matches = []
    j = 0
    for i, ch in enumerate(text):
        while j > 0 and ch != pattern[j]:
            j = lps[j-1]
        if ch == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i - j + 1)
            j = lps[j-1]
    return matches

def compute_lps(p):
    lps = [0] * len(p)
    k = 0
    for i in range(1, len(p)):
        while k > 0 and p[i] != p[k]: k = lps[k-1]
        if p[i] == p[k]: k += 1
        lps[i] = k
    return lps
