// list: doubly linked nodes, splice and stable iterators.
#include <iostream>
#include <list>

int main() {
    std::list<int> items{1, 2, 3, 4, 5};
    auto it = items.begin();
    std::advance(it, 3);
    items.splice(items.begin(), items, it);  // O(1) move, iterators stable
    for (int value : items) std::cout << value << ' ';
    std::cout << '\n';
    return 0;
}
