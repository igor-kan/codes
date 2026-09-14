// A Tour of C++ -- unique_ptr, shared_ptr and weak_ptr.
#include <iostream>
#include <memory>

struct Node {
    int value;
    explicit Node(int v) : value(v) {}
};

int main() {
    auto unique = std::make_unique<Node>(1);
    auto shared = std::make_shared<Node>(2);
    std::weak_ptr<Node> observer = shared;

    std::cout << unique->value << ' ' << shared->value
              << " count=" << shared.use_count();
    shared.reset();
    std::cout << " expired=" << std::boolalpha << observer.expired() << '\n';
    return 0;
}
