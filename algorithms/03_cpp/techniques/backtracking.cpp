/**
 * Backtracking: subsets, permutations and combinations.
 */

#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>

void genSubsets(int start, std::vector<int>& cur, const std::vector<int>& a,
                std::vector<std::vector<int>>& out) {
    out.push_back(cur);
    for (int i = start; i < static_cast<int>(a.size()); ++i) {
        cur.push_back(a[i]);
        genSubsets(i + 1, cur, a, out);
        cur.pop_back();
    }
}

std::vector<std::vector<int>> subsets(const std::vector<int>& a) {
    std::vector<std::vector<int>> out;
    std::vector<int> cur;
    genSubsets(0, cur, a, out);
    return out;
}

void genPermutations(std::vector<int>& a, int idx, std::vector<std::vector<int>>& out) {
    if (idx == static_cast<int>(a.size())) {
        out.push_back(a);
        return;
    }
    for (int i = idx; i < static_cast<int>(a.size()); ++i) {
        std::swap(a[idx], a[i]);
        genPermutations(a, idx + 1, out);
        std::swap(a[idx], a[i]);
    }
}

std::vector<std::vector<int>> permutations(std::vector<int> a) {
    std::vector<std::vector<int>> out;
    genPermutations(a, 0, out);
    return out;
}

void genCombinations(int start, int k, std::vector<int>& cur, int n,
                     std::vector<std::vector<int>>& out) {
    if (static_cast<int>(cur.size()) == k) {
        out.push_back(cur);
        return;
    }
    for (int i = start; i <= n; ++i) {
        cur.push_back(i);
        genCombinations(i + 1, k, cur, n, out);
        cur.pop_back();
    }
}

std::vector<std::vector<int>> combinations(int n, int k) {
    std::vector<std::vector<int>> out;
    std::vector<int> cur;
    genCombinations(1, k, cur, n, out);
    return out;
}

int main() {
    auto s = subsets({1, 2, 3});
    assert(s.size() == 8);
    assert(std::find(s.begin(), s.end(), std::vector<int>{1, 3}) != s.end());

    auto p = permutations({1, 2, 3});
    assert(p.size() == 6);

    auto c = combinations(4, 2);
    assert(c.size() == 6);
    assert(std::find(c.begin(), c.end(), std::vector<int>{2, 4}) != c.end());
    std::cout << "[C++ Backtracking] Subsets, permutations and combinations verified." << std::endl;
    return 0;
}
