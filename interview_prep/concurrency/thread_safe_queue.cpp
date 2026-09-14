// Thread-safe queue using a mutex and two condition variables.
#include <condition_variable>
#include <iostream>
#include <memory>
#include <mutex>
#include <queue>
#include <utility>

template <typename T>
class threadsafe_queue {
    mutable std::mutex mtx_;
    std::condition_variable not_empty_;
    std::queue<T> data_;
  public:
    void push(T value) {
        { std::lock_guard<std::mutex> lock(mtx_); data_.push(std::move(value)); }
        not_empty_.notify_one();
    }
    void wait_and_pop(T &out) {
        std::unique_lock<std::mutex> lock(mtx_);
        not_empty_.wait(lock, [&]{ return !data_.empty(); });
        out = std::move(data_.front());
        data_.pop();
    }
    bool try_pop(T &out) {
        std::lock_guard<std::mutex> lock(mtx_);
        if (data_.empty()) return false;
        out = std::move(data_.front());
        data_.pop();
        return true;
    }
    bool empty() const {
        std::lock_guard<std::mutex> lock(mtx_);
        return data_.empty();
    }
};

int main() {
    threadsafe_queue<int> queue;
    queue.push(1);
    queue.push(2);
    int value = 0;
    queue.wait_and_pop(value);
    std::cout << value << '\n';
    return value == 1 ? 0 : 1;
}
