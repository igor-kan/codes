// Parallel quicksort using std::async.
#include <algorithm>
#include <future>
#include <iostream>
#include <random>
#include <vector>

template <typename T>
std::vector<T> parallel_quick_sort(std::vector<T> input) {
    if (input.size() < 2) return input;
    const T pivot = input.front();
    std::vector<T> lower, upper;
    for (std::size_t i = 1; i < input.size(); ++i)
        (input[i] < pivot ? lower : upper).push_back(input[i]);
    auto lower_future = std::async(std::launch::async, [lower = std::move(lower)] { return parallel_quick_sort(lower); });
    std::vector<T> sorted_upper = parallel_quick_sort(std::move(upper));
    std::vector<T> result = lower_future.get();
    result.push_back(pivot);
    result.insert(result.end(), sorted_upper.begin(), sorted_upper.end());
    return result;
}

int main() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dist(0, 1000);
    std::vector<int> data(200);
    std::generate(data.begin(), data.end(), [&]{ return dist(gen); });
    auto sorted = parallel_quick_sort(data);
    std::cout << std::boolalpha << std::is_sorted(sorted.begin(), sorted.end()) << '\n';
    return std::is_sorted(sorted.begin(), sorted.end()) ? 0 : 1;
}
