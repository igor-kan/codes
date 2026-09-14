// Creating and using std::thread.
#include <iostream>
#include <thread>
#include <vector>

int main() {
    std::thread worker([]{ std::cout << "worker thread id=" << std::this_thread::get_id() << '\n'; });
    worker.join();

    std::vector<std::thread> pool;
    for (int i = 0; i < 4; ++i) pool.emplace_back([i]{ std::cout << "task " << i << '\n'; });
    for (auto &t : pool) t.join();
    return 0;
}
