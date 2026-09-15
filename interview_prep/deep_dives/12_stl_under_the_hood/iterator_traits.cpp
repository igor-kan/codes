// Iterator traits and tag dispatch for a custom iterator.
#include <iterator>
#include <iostream>
#include <vector>

template <typename Iterator>
void report(Iterator it) {
    using category = typename std::iterator_traits<Iterator>::iterator_category;
    if constexpr (std::is_same_v<category, std::random_access_iterator_tag>)
        std::cout << "random access, *it+2=" << *(it + 2) << '\n';
    else
        std::cout << "weaker iterator category\n";
}

int main() {
    std::vector<int> values{10, 20, 30};
    report(values.begin());
    return 0;
}
