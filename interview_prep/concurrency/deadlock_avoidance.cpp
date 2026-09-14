// Avoiding deadlock with std::scoped_lock and lock ordering.
#include <iostream>
#include <mutex>
#include <thread>

std::mutex a, b;

void safe() {
    std::scoped_lock lock(a, b);  // locks both atomically
    std::cout << "both locks held safely\n";
}

int main() {
    std::thread t1(safe);
    std::thread t2(safe);
    t1.join(); t2.join();
    return 0;
}
