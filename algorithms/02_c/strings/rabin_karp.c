#include <stdio.h>
#include <string.h>
#include <assert.h>
int rabinKarp(const char* text, const char* pat) {
    int n = strlen(text), m = strlen(pat);
    if (m > n) return -1;
    long long d = 256, q = 1000000007, h = 1;
    for (int i = 0; i < m - 1; i++) h = (h * d) % q;
    long long pHash = 0, tHash = 0;
    for (int i = 0; i < m; i++) {
        pHash = (d * pHash + pat[i]) % q;
        tHash = (d * tHash + text[i]) % q;
    }
    for (int i = 0; i <= n - m; i++) {
        if (pHash == tHash && strncmp(text + i, pat, m) == 0) return i;
        if (i < n - m) {
            tHash = (d * (tHash - text[i] * h) + text[i + m]) % q;
            if (tHash < 0) tHash += q;
        }
    }
    return -1;
}
int main(void) {
    assert(rabinKarp("HELLO WORLD", "WORLD") == 6);
    printf("C Rabin-Karp verified.\n");
    return 0;
}
