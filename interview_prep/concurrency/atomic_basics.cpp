// Atomic operations and compare_exchange loops.
#include <atomic>
#include <iostream>
#include <thread>
#include <vector>

int main() {
    std::atomic<int> counter{0};
    std::vector<std::thread> workers;
    for (int i = 0; i < 8; ++i)
        workers.emplace_back([&]{ for (int n = 0; n < 10'000; ++n) counter.fetch_add(1, std::memory_order_relaxed); });
    for (auto &t : workers) t.join();

    std::atomic<bool> flag{false};
    bool expected = false;
    flag.compare_exchange_strong(expected, true);

    std::cout << "counter=" << counter << " flag=" << flag.load() << '\n';
    return counter == 80'000 ? 0 : 1;
}
