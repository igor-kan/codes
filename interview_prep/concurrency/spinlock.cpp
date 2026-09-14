// A simple spinlock built from std::atomic_flag.
#include <atomic>
#include <iostream>
#include <thread>
#include <vector>

class spinlock {
    std::atomic_flag flag_ = ATOMIC_FLAG_INIT;
  public:
    void lock() { while (flag_.test_and_set(std::memory_order_acquire)) {} }
    void unlock() { flag_.clear(std::memory_order_release); }
};

int main() {
    spinlock lock;
    int counter = 0;
    std::vector<std::thread> workers;
    for (int i = 0; i < 4; ++i)
        workers.emplace_back([&] {
            for (int n = 0; n < 10'000; ++n) {
                lock.lock();
                ++counter;
                lock.unlock();
            }
        });
    for (auto &t : workers) t.join();
    std::cout << "counter=" << counter << '\n';
    return counter == 40'000 ? 0 : 1;
}
