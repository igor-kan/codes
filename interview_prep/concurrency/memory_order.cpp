// Publisher/subscriber using acquire-release ordering.
#include <atomic>
#include <cassert>
#include <iostream>
#include <thread>

int main() {
    std::atomic<bool> ready{false};
    int payload = 0;

    std::thread producer([&] {
        payload = 42;                                   // non-atomic write
        ready.store(true, std::memory_order_release);   // publishes it
    });

    std::thread consumer([&] {
        while (!ready.load(std::memory_order_acquire)) {}  // synchronizes-with
        assert(payload == 42);
        std::cout << "payload=" << payload << '\n';
    });

    producer.join(); consumer.join();
    return 0;
}
