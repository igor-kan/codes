// Effective C++ -- noexcept enables vector reallocation via move.
#include <iostream>
#include <utility>
#include <vector>

class Movable {
  public:
    Movable() = default;
    Movable(const Movable &) { std::cout << "copy\n"; }
    Movable(Movable &&) noexcept { std::cout << "move\n"; }
    Movable &operator=(const Movable &) = default;
    Movable &operator=(Movable &&) noexcept = default;
};

int main() {
    std::vector<Movable> items;
    items.reserve(3);
    items.push_back(Movable{});
    items.emplace_back(Movable{});
    std::cout << "size=" << items.size() << '\n';
    return 0;
}
