#include <string>
#include <vector>
#include <cassert>
#include <iostream>
std::vector<int> rabinKarp(const std::string& text, const std::string& pat) {
    std::vector<int> matches;
    int n = text.size(), m = pat.size();
    if (m == 0 || m > n) return matches;
    long long d = 256, q = 1000000007, h = 1;
    for (int i = 0; i < m - 1; i++) h = (h * d) % q;
    long long pHash = 0, tHash = 0;
    for (int i = 0; i < m; i++) {
        pHash = (d * pHash + text[i]) % q;
        tHash = (d * tHash + pat[i]) % q;
    }
    for (int i = 0; i <= n - m; i++) {
        if (pHash == tHash && text.substr(i, m) == pat) matches.push_back(i);
        if (i < n - m) {
            tHash = (d * (tHash - text[i] * h) + text[i + m]) % q;
            if (tHash < 0) tHash += q;
        }
    }
    return matches;
}
int main() {
    auto m = rabinKarp("GEEKS FOR GEEKS", "GEEK");
    assert(!m.empty());
    std::cout << "C++ Rabin-Karp verified.\n";
}
