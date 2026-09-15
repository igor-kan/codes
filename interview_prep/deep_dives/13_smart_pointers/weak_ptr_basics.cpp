// weak_ptr breaks reference cycles and enables safe observer access.
#include <iostream>
#include <memory>

struct Node {
    int value;
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;  // weak to avoid a cycle
    explicit Node(int v) : value(v) {}
};

int main() {
    auto a = std::make_shared<Node>(1);
    auto b = std::make_shared<Node>(2);
    a->next = b;
    b->prev = a;

    if (auto locked = b->prev.lock()) std::cout << "prev=" << locked->value << '\n';
    a.reset();
    std::cout << "after reset expired=" << b->prev.expired() << '\n';
    return 0;
}
