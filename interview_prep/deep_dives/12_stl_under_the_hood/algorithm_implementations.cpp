// Implementing std::find, std::transform and std::accumulate from scratch.
#include <iostream>
#include <vector>

template <typename It, typename T>
It my_find(It first, It last, const T &value) {
    for (; first != last; ++first) if (*first == value) return first;
    return last;
}

template <typename It, typename Out, typename F>
Out my_transform(It first, It last, Out out, F fn) {
    for (; first != last; ++first, ++out) *out = fn(*first);
    return out;
}

template <typename It, typename T, typename F>
T my_accumulate(It first, It last, T init, F fn) {
    for (; first != last; ++first) init = fn(init, *first);
    return init;
}

int main() {
    std::vector<int> values{1, 2, 3, 4};
    auto found = my_find(values.begin(), values.end(), 3);
    std::vector<int> doubled(values.size());
    my_transform(values.begin(), values.end(), doubled.begin(), [](int n) { return n * 2; });
    int sum = my_accumulate(values.begin(), values.end(), 0, [](int a, int b) { return a + b; });
    std::cout << (found != values.end()) << ' ' << doubled.back() << ' ' << sum << '\n';
    return 0;
}
