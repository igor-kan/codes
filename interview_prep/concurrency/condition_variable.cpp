// Condition variables with predicate to avoid spurious wakeups.
#include <condition_variable>
#include <iostream>
#include <mutex>
#include <queue>
#include <thread>

int main() {
    std::queue<int> data;
    std::mutex mtx;
    std::condition_variable cv;
    bool done = false;

    std::thread producer([&] {
        for (int i = 0; i < 5; ++i) {
            { std::lock_guard<std::mutex> lock(mtx); data.push(i); }
            cv.notify_one();
        }
        { std::lock_guard<std::mutex> lock(mtx); done = true; }
        cv.notify_one();
    });

    std::thread consumer([&] {
        for (;;) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [&]{ return !data.empty() || done; });
            if (data.empty() && done) break;
            int value = data.front(); data.pop();
            std::cout << "consumed " << value << '\n';
        }
    });

    producer.join(); consumer.join();
    return 0;
}
