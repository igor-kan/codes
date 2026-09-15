// Binary max-heap.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <queue>
#include <vector>

int main() {
    std::priority_queue<int> heap;
    for (int v : {5, 3, 8, 1, 4}) heap.push(v);
    int prev = 1 << 30;
    std::vector<int> out;
    while (!heap.empty()) {
        int x = heap.top();
        heap.pop();
        assert(x <= prev);
        prev = x;
        out.push_back(x);
    }
    std::cout << "max heap ok: " << out.front() << '\n';
    return 0;
}
