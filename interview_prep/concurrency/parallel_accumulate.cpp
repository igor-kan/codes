// Parallel accumulate with std::async and hardware_concurrency.
#include <algorithm>
#include <future>
#include <iostream>
#include <numeric>
#include <thread>
#include <vector>

template <typename Iterator, typename T>
T parallel_accumulate(Iterator first, Iterator last, T init) {
    const std::size_t length = static_cast<std::size_t>(std::distance(first, last));
    const std::size_t min_per_thread = 25;
    const std::size_t max_threads = (length + min_per_thread - 1) / min_per_thread;
    const std::size_t hardware = std::thread::hardware_concurrency();
    const std::size_t num_threads = std::max(1u, static_cast<unsigned>(std::min(max_threads, hardware)));
    const std::size_t block = length / num_threads;

    std::vector<std::future<T>> futures(num_threads - 1);
    std::vector<std::thread> threads(num_threads - 1);
    Iterator start = first;
    for (std::size_t i = 0; i < num_threads - 1; ++i) {
        Iterator end = start;
        std::advance(end, static_cast<std::ptrdiff_t>(block));
        std::packaged_task<T(Iterator, Iterator)> task(
            [](Iterator a, Iterator b) { return std::accumulate(a, b, T{}); });
        futures[i] = task.get_future();
        threads[i] = std::thread(std::move(task), start, end);
        start = end;
    }
    T total = std::accumulate(start, last, init);
    for (std::size_t i = 0; i < num_threads - 1; ++i) { total += futures[i].get(); threads[i].join(); }
    return total;
}

int main() {
    std::vector<int> data(10'000, 1);
    std::cout << "sum=" << parallel_accumulate(data.begin(), data.end(), 0) << '\n';
    return 0;
}
