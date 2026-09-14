// A lock-free-ish stack guarded by a mutex, returning shared_ptr.
#include <iostream>
#include <memory>
#include <mutex>
#include <stack>
#include <utility>

template <typename T>
class threadsafe_stack {
    std::stack<T> data_;
    mutable std::mutex mtx_;
  public:
    void push(T value) {
        std::lock_guard<std::mutex> lock(mtx_);
        data_.push(std::move(value));
    }
    std::shared_ptr<T> pop() {
        std::lock_guard<std::mutex> lock(mtx_);
        if (data_.empty()) return nullptr;
        auto result = std::make_shared<T>(std::move(data_.top()));
        data_.pop();
        return result;
    }
    bool empty() const {
        std::lock_guard<std::mutex> lock(mtx_);
        return data_.empty();
    }
};

int main() {
    threadsafe_stack<int> stack;
    stack.push(10);
    auto value = stack.pop();
    std::cout << (value ? *value : -1) << '\n';
    return value && *value == 10 ? 0 : 1;
}
