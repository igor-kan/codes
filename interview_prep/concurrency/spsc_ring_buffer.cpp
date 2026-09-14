// Single-producer/single-consumer lock-free ring buffer.
#include <array>
#include <atomic>
#include <iostream>

template <typename T, std::size_t N>
class spsc_queue {
    static_assert((N & (N - 1)) == 0, "N must be a power of two");
    std::array<T, N> buffer_{};
    std::atomic<std::size_t> head_{0};
    std::atomic<std::size_t> tail_{0};
  public:
    bool push(const T &value) {
        const std::size_t tail = tail_.load(std::memory_order_relaxed);
        const std::size_t next = (tail + 1) & (N - 1);
        if (next == head_.load(std::memory_order_acquire)) return false;
        buffer_[tail] = value;
        tail_.store(next, std::memory_order_release);
        return true;
    }
    bool pop(T &out) {
        const std::size_t head = head_.load(std::memory_order_relaxed);
        if (head == tail_.load(std::memory_order_acquire)) return false;
        out = buffer_[head];
        head_.store((head + 1) & (N - 1), std::memory_order_release);
        return true;
    }
};

int main() {
    spsc_queue<int, 8> queue;
    queue.push(42);
    int value = 0;
    queue.pop(value);
    std::cout << value << '\n';
    return value == 42 ? 0 : 1;
}
