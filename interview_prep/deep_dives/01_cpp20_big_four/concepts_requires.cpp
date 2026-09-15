// Nested requirements, compound requirements and ad-hoc constraints.
#include <concepts>
#include <iostream>
#include <vector>

template <typename T>
concept Container = requires(T c) {
    typename T::value_type;
    { c.size() } -> std::convertible_to<std::size_t>;
    { c.begin() } -> std::input_iterator;
    { c.end() };
};

template <Container C>
void describe(const C &container) {
    std::cout << "container size=" << container.size() << '\n';
}

int main() {
    describe(std::vector<int>{1, 2, 3});
    return 0;
}
