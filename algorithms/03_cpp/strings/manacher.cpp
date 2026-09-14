/**
 * Manacher's algorithm: longest palindromic substrings (odd and even).
 */

#include <string>
#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>

// d1[i] = number of palindromes with center i (odd length, radius count).
std::vector<int> manacherOdd(const std::string& s) {
    int n = static_cast<int>(s.size());
    std::vector<int> d1(n);
    int l = 0, r = -1;
    for (int i = 0; i < n; ++i) {
        int k = (i > r) ? 1 : std::min(d1[l + r - i], r - i + 1);
        while (i - k >= 0 && i + k < n && s[i - k] == s[i + k]) ++k;
        d1[i] = k;
        if (i + k - 1 > r) {
            l = i - k + 1;
            r = i + k - 1;
        }
    }
    return d1;
}

// d2[i] = number of even palindromes with center between i-1 and i.
std::vector<int> manacherEven(const std::string& s) {
    int n = static_cast<int>(s.size());
    std::vector<int> d2(n);
    int l = 0, r = -1;
    for (int i = 0; i < n; ++i) {
        int k = (i > r) ? 0 : std::min(d2[l + r - i + 1], r - i + 1);
        while (i + k < n && i - k - 1 >= 0 && s[i + k] == s[i - k - 1]) ++k;
        d2[i] = k;
        if (i + k - 1 > r) {
            l = i - k;
            r = i + k - 1;
        }
    }
    return d2;
}

int longestPalindromicSubstring(const std::string& s) {
    auto d1 = manacherOdd(s);
    auto d2 = manacherEven(s);
    int best = 0;
    for (int v : d1) best = std::max(best, 2 * v - 1);
    for (int v : d2) best = std::max(best, 2 * v);
    return best;
}

int main() {
    auto d1 = manacherOdd("abacaba");
    assert((d1 == std::vector<int>{1, 2, 1, 4, 1, 2, 1}));
    assert(longestPalindromicSubstring("abacaba") == 7);
    assert(longestPalindromicSubstring("babad") == 3);
    assert(longestPalindromicSubstring("cbbd") == 2);
    std::cout << "[C++ Manacher] Longest palindromic substring verified." << std::endl;
    return 0;
}
