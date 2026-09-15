// Enumerate a range with a C++20 views pipeline.
#include <iostream>
#include <ranges>
#include <string>
#include <utility>
#include <vector>

int main() {
    std::vector<std::string> names{"a", "b", "c"};

    auto indexed = std::views::iota(0u, names.size())
        | std::views::transform([&](std::size_t i) { return std::pair{i, names[i]}; });

    for (auto [index, name] : indexed) std::cout << index << ':' << name << ' ';
    std::cout << '\n';
    return 0;
}
