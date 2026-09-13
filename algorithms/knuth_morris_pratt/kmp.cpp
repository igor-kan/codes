/**
 * Knuth-Morris-Pratt (KMP) String Search Algorithm in C++.
 */

#include <iostream>
#include <vector>
#include <string>
#include <cassert>

std::vector<int> compute_lps(const std::string& pattern) {
    int m = pattern.length();
    std::vector<int> lps(m, 0);
    int len = 0;
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
    return lps;
}

std::vector<int> kmp_search(const std::string& text, const std::string& pattern) {
    int n = text.length();
    int m = pattern.length();
    if (m == 0 || n == 0) return {};

    std::vector<int> lps = compute_lps(pattern);
    std::vector<int> occurrences;

    int i = 0;
    int j = 0;

    while (i < n) {
        if (text[i] == pattern[j]) {
            i++;
            j++;
        }

        if (j == m) {
            occurrences.push_back(i - j);
            j = lps[j - 1];
        } else if (i < n && text[i] != pattern[j]) {
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }

    return occurrences;
}

int main() {
    std::string txt = "ABABDABACDABABCABABABABCABAB";
    std::string pat = "ABABCABAB";
    auto matches = kmp_search(txt, pat);

    assert(matches.size() == 2);
    assert(matches[0] == 10 && matches[1] == 19);

    std::cout << "[C++ KMP] Matches confirmed: " << matches[0] << ", " << matches[1] << std::endl;
    return 0;
}
