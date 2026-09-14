// Protecting shared data with std::mutex.
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>

int main() {
    long counter = 0;
    std::mutex mtx;
    std::vector<std::thread> workers;
    for (int i = 0; i < 8; ++i)
        workers.emplace_back([&] {
            for (int n = 0; n < 10'000; ++n) {
                std::lock_guard<std::mutex> lock(mtx);
                ++counter;
            }
        });
    for (auto &t : workers) t.join();
    std::cout << "counter=" << counter << '\n';
    return counter == 80'000 ? 0 : 1;
}
