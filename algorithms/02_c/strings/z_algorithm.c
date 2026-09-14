#include <stdio.h>
#include <string.h>

#define MAXN 100000

void z_function(const char *s, int *z) {
    int n = strlen(s);
    z[0] = n;
    int l = 0, r = 0;
    for (int i = 1; i < n; ++i) {
        if (i <= r) {
            int cand = z[i - l];
            int bound = r - i + 1;
            z[i] = cand < bound ? cand : bound;
        } else {
            z[i] = 0;
        }
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];
        if (i + z[i] - 1 > r) { l = i; r = i + z[i] - 1; }
    }
}

int main(void) {
    const char *s = "abacaba";
    int expected[] = {7, 0, 1, 0, 3, 0, 1};
    int z[MAXN];

    z_function(s, z);
    for (int i = 0; i < 7; ++i) {
        if (z[i] != expected[i]) {
            printf("[C ZAlgorithm] FAILED at index %d: got %d, want %d\n", i, z[i], expected[i]);
            return 1;
        }
    }
    printf("[C ZAlgorithm] Z-array of \"abacaba\" verified\n");
    return 0;
}
