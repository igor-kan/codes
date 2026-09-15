// Rod cutting (CLRS 15.1).
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

int cutRod(const std::vector<int> &prices, int n) {
    std::vector<int> best(n + 1, 0);
    for (int length = 1; length <= n; ++length)
        for (int i = 1; i <= length; ++i)
            best[length] = std::max(best[length], prices[i - 1] + best[length - i]);
    return best[n];
}

int main() {
    std::vector<int> prices{1, 5, 8, 9, 10, 17, 17, 20, 24, 30};
    assert(cutRod(prices, 4) == 10);
    assert(cutRod(prices, 7) == 18);
    assert(cutRod(prices, 10) == 30);
    std::cout << "rod cutting ok\n";
    return 0;
}
