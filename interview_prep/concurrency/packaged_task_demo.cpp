// Wrapping a callable in std::packaged_task.
#include <future>
#include <iostream>
#include <thread>

int main() {
    std::packaged_task<int(int, int)> task([](int a, int b) { return a * b; });
    std::future<int> future = task.get_future();
    std::thread worker(std::move(task), 6, 7);
    std::cout << "product=" << future.get() << '\n';
    worker.join();
    return 0;
}
