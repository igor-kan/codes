// Boyer-Moore-Horspool substring search.
#include <array>
#include <cassert>
#include <iostream>
#include <string>

int boyer_moore(const std::string &text, const std::string &pat) {
    const int n = static_cast<int>(text.size()), m = static_cast<int>(pat.size());
    std::array<int, 256> skip;
    skip.fill(m);
    for (int i = 0; i < m - 1; ++i) skip[static_cast<unsigned char>(pat[i])] = m - 1 - i;
    int i = 0;
    while (i <= n - m) {
        int j = m - 1;
        while (j >= 0 && text[i + j] == pat[j]) --j;
        if (j < 0) return i;
        i += skip[static_cast<unsigned char>(text[i + m - 1])];
    }
    return -1;
}

int main() {
    assert(boyer_moore("here is a simple example", "example") == 17);
    assert(boyer_moore("abc", "xyz") == -1);
    std::cout << "boyer-moore ok\n";
    return 0;
}
