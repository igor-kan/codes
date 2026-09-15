// Reservoir sampling for a uniform sample of a stream (CLRS 5.3).
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <vector>

int main() {
    std::srand(42);
    const int k = 5, n = 100;
    std::vector<int> reservoir;
    for (int i = 0; i < n; ++i) {
        if (i < k) reservoir.push_back(i);
        else {
            int j = std::rand() % (i + 1);
            if (j < k) reservoir[j] = i;
        }
    }
    assert(static_cast<int>(reservoir.size()) == k);
    std::cout << "reservoir sampling ok\n";
    return 0;
}
