// Communicating a value with std::promise/std::future.
#include <future>
#include <iostream>
#include <thread>

void compute(std::promise<int> result) {
    try {
        result.set_value(6 * 7);
    } catch (...) {
        result.set_exception(std::current_exception());
    }
}

int main() {
    std::promise<int> promise;
    std::future<int> future = promise.get_future();
    std::thread worker(compute, std::move(promise));
    std::cout << "result=" << future.get() << '\n';
    worker.join();
    return 0;
}
