/* Boyer-Moore-Horspool substring search. */
#include <stdio.h>
#include <string.h>
int boyer_moore(const char *t, const char *p) {
    int n = (int)strlen(t), m = (int)strlen(p);
    int skip[256];
    for (int i = 0; i < 256; i++) skip[i] = m;
    for (int i = 0; i < m - 1; i++) skip[(unsigned char)p[i]] = m - 1 - i;
    int i = 0;
    while (i <= n - m) {
        int j = m - 1;
        while (j >= 0 && t[i + j] == p[j]) j--;
        if (j < 0) return i;
        i += skip[(unsigned char)t[i + m - 1]];
    }
    return -1;
}
int main(void) {
    if (boyer_moore("here is a simple example", "example") != 17) return 1;
    if (boyer_moore("abc", "xyz") != -1) return 1;
    printf("boyer-moore ok\n");
    return 0;
}
