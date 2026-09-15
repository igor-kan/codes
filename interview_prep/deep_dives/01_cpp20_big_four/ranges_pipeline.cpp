// Ranges pipelines with views.
#include <iostream>
#include <ranges>
#include <vector>

int main() {
    std::vector<int> values{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    auto result = values
        | std::views::filter([](int n) { return n % 2 == 0; })
        | std::views::transform([](int n) { return n * n; })
        | std::views::take(3);

    for (int n : result) std::cout << n << ' ';
    std::cout << '\n';
    return 0;
}
