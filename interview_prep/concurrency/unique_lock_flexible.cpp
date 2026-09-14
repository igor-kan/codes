// std::unique_lock: deferred locking, unlocking and ownership transfer.
#include <iostream>
#include <mutex>
#include <thread>

std::mutex mtx;

void process(int id, std::unique_lock<std::mutex> lock) {
    std::cout << "processing " << id << '\n';
    lock.unlock();
    std::this_thread::sleep_for(std::chrono::milliseconds(1));
    lock.lock();
}

int main() {
    std::unique_lock<std::mutex> lock(mtx, std::defer_lock);
    lock.lock();
    std::thread t(process, 1, std::move(lock));
    t.join();
    std::cout << "done\n";
    return 0;
}
