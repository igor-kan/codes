// Fractional knapsack (CLRS 16.2).
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>

struct Item { int value, weight; };

int main() {
    std::vector<Item> items{{60, 10}, {100, 20}, {120, 30}};
    std::sort(items.begin(), items.end(), [](const Item &a, const Item &b) {
        return static_cast<double>(a.value) / a.weight > static_cast<double>(b.value) / b.weight;
    });
    int capacity = 50;
    double total = 0.0;
    for (const auto &item : items) {
        if (capacity <= 0) break;
        int take = std::min(item.weight, capacity);
        total += static_cast<double>(item.value) * take / item.weight;
        capacity -= take;
    }
    assert(std::abs(total - 240.0) < 1e-9);
    std::cout << "fractional knapsack ok\n";
    return 0;
}
