/**
 * Knuth-Morris-Pratt (KMP) String Search Algorithm in C.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

void compute_lps(const char* pattern, int m, int* lps) {
    int len = 0;
    lps[0] = 0;
    int i = 1;
    while (i < m) {
        if (pattern[i] == pattern[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len != 0) {
                len = lps[len - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
}

int kmp_search(const char* text, const char* pattern, int* matches, int max_matches) {
    int n = strlen(text);
    int m = strlen(pattern);
    if (m == 0 || n == 0) return 0;

    int* lps = (int*)malloc(sizeof(int) * m);
    compute_lps(pattern, m, lps);

    int count = 0;
    int i = 0; // index for text
    int j = 0; // index for pattern

    while (i < n) {
        if (text[i] == pattern[j]) {
            i++;
            j++;
        }

        if (j == m) {
            if (count < max_matches) {
                matches[count++] = i - j;
            }
            j = lps[j - 1];
        } else if (i < n && text[i] != pattern[j]) {
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }

    free(lps);
    return count;
}

int main(void) {
    const char* txt = "ABABDABACDABABCABABABABCABAB";
    const char* pat = "ABABCABAB";
    int matches[10];
    int found = kmp_search(txt, pat, matches, 10);

    assert(found == 2);
    assert(matches[0] == 10);
    assert(matches[1] == 19);

    printf("[C KMP] Matches verified at offsets: %d and %d\n", matches[0], matches[1]);
    return 0;
}
