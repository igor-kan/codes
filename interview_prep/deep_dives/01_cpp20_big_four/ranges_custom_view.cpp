// A custom range adaptor with a view-like closure (C++20 views).
#include <iostream>
#include <ranges>
#include <vector>

class Even {
  public:
    explicit Even(std::vector<int> data) : data_(std::move(data)) {}
    auto begin() const { return data_.begin(); }
    auto end() const { return data_.end(); }

  private:
    std::vector<int> data_;
};

int main() {
    std::vector<int> data{1, 2, 3, 4, 5, 6};
    auto evens = data | std::views::filter([](int n) { return n % 2 == 0; });
    static_assert(std::ranges::range<decltype(evens)>);
    for (int n : evens) std::cout << n << ' ';
    std::cout << '\n';
    return 0;
}
