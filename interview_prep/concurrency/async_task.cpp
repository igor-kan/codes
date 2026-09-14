// std::async, deferred and async launch policies.
#include <chrono>
#include <future>
#include <iostream>

int slow_add(int a, int b) {
    std::this_thread::sleep_for(std::chrono::milliseconds(5));
    return a + b;
}

int main() {
    auto async_future = std::async(std::launch::async, slow_add, 2, 3);
    auto deferred_future = std::async(std::launch::deferred, slow_add, 10, 20);
    std::cout << async_future.get() << ' ' << deferred_future.get() << '\n';
    return 0;
}
