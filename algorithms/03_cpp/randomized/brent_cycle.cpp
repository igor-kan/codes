// Brent's cycle detection (Brent 1980).
#include <cassert>
#include <functional>
#include <iostream>
#include <utility>

std::pair<int, int> brentCycle(const std::function<int(int)> &nextNode, int start) {
    int power = 1, lam = 1, tortoise = start, hare = nextNode(start);
    while (tortoise != hare) {
        if (power == lam) { tortoise = hare; power *= 2; lam = 0; }
        hare = nextNode(hare);
        ++lam;
    }
    tortoise = hare = start;
    for (int i = 0; i < lam; ++i) hare = nextNode(hare);
    int mu = 0;
    while (tortoise != hare) { tortoise = nextNode(tortoise); hare = nextNode(hare); ++mu; }
    return {mu, lam};
}

int main() {
    std::vector<int> link{1, 2, 3, 4, 3};
    auto [mu, lam] = brentCycle([&](int i) { return link[i]; }, 0);
    assert(mu == 3 && lam == 2);
    std::cout << "brent cycle ok\n";
    return 0;
}
