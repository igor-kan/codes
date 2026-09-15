// Egg dropping.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

int main() {
    const int eggs = 2, floors = 100;
    std::vector<std::vector<int>> dp(101, std::vector<int>(eggs + 1, 0));
    int t = 0;
    while (dp[t][eggs] < floors) {
        ++t;
        for (int k = 1; k <= eggs; ++k) dp[t][k] = dp[t - 1][k - 1] + dp[t - 1][k] + 1;
    }
    assert(t == 14);
    std::cout << "egg drop=" << t << '\n';
    return 0;
}
