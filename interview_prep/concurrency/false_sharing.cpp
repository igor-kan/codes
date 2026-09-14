// False sharing vs cache-line padded counters.
#include <atomic>
#include <chrono>
#include <iostream>
#include <thread>

struct Padded {
    alignas(64) std::atomic<long> value{0};
    char padding[64 - sizeof(std::atomic<long>)];
};

struct Unpadded { std::atomic<long> value{0}; };

template <typename Counters>
long run_benchmark() {
    Counters counters[2];
    auto start = std::chrono::steady_clock::now();
    std::thread t1([&]{ for (int i = 0; i < 5'000'000; ++i) counters[0].value.fetch_add(1, std::memory_order_relaxed); });
    std::thread t2([&]{ for (int i = 0; i < 5'000'000; ++i) counters[1].value.fetch_add(1, std::memory_order_relaxed); });
    t1.join(); t2.join();
    return std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now() - start).count();
}

int main() {
    long unpadded = run_benchmark<Unpadded>();
    long padded = run_benchmark<Padded>();
    std::cout << "unpadded=" << unpadded << "ms padded=" << padded << "ms\n";
    return 0;
}
