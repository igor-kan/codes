// Treiber stack: lock-free push/pop using compare_exchange.
#include <atomic>
#include <iostream>
#include <memory>

template <typename T>
class lock_free_stack {
    struct node {
        T value;
        node *next;
    };
    std::atomic<node *> head_{nullptr};
  public:
    void push(T value) {
        node *fresh = new node{std::move(value), head_.load()};
        while (!head_.compare_exchange_weak(fresh->next, fresh)) {}
    }
    bool pop(T &out) {
        node *old_head = head_.load();
        while (old_head && !head_.compare_exchange_weak(old_head, old_head->next)) {}
        if (!old_head) return false;
        out = std::move(old_head->value);
        delete old_head;
        return true;
    }
};

int main() {
    lock_free_stack<int> stack;
    stack.push(1);
    stack.push(2);
    int value = 0;
    stack.pop(value);
    std::cout << value << '\n';
    return value == 2 ? 0 : 1;
}
