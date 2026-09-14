#include <stdio.h>
#include <string.h>

#define MAXN 100000

static char t[2 * MAXN + 3];
static int p[2 * MAXN + 3];

int manacher(const char *s) {
    int n = strlen(s);
    int len = 0;
    t[len++] = '#';
    for (int i = 0; i < n; ++i) { t[len++] = s[i]; t[len++] = '#'; }
    t[len] = '\0';

    int c = 0, r = 0, maxlen = 0;
    for (int i = 0; i < len; ++i) {
        int mirror = 2 * c - i;
        p[i] = (i < r) ? ((r - i) < p[mirror] ? (r - i) : p[mirror]) : 0;
        while (i + p[i] + 1 < len && i - p[i] - 1 >= 0 &&
               t[i + p[i] + 1] == t[i - p[i] - 1]) ++p[i];
        if (i + p[i] > r) { c = i; r = i + p[i]; }
        if (p[i] > maxlen) maxlen = p[i];
    }
    return maxlen;
}

int main(void) {
    if (manacher("babad") != 3) {
        printf("[C Manacher] FAILED: babad -> 3\n");
        return 1;
    }
    if (manacher("cbbd") != 2) {
        printf("[C Manacher] FAILED: cbbd -> 2\n");
        return 1;
    }
    if (manacher("racecar") != 7) {
        printf("[C Manacher] FAILED: racecar -> 7\n");
        return 1;
    }
    printf("[C Manacher] Longest palindromic substring verified\n");
    return 0;
}
