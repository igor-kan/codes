def rabin_karp(text, pattern, base=256, mod=101):
    n, m = len(text), len(pattern)
    h = pow(base, m-1, mod)
    tp = pt = 0
    for i in range(m):
        tp = (base*tp + ord(text[i])) % mod
        pt = (base*pt + ord(pattern[i])) % mod
    matches = []
    for i in range(n - m + 1):
        if tp == pt and text[i:i+m] == pattern:
            matches.append(i)
        if i < n - m:
            tp = (base*(tp - ord(text[i])*h) + ord(text[i+m])) % mod
    return matches
