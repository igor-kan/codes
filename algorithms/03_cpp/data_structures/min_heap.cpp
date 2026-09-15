// Binary min-heap.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

class MinHeap {
  public:
    void push(int value) {
        data_.push_back(value);
        std::push_heap(data_.begin(), data_.end(), std::greater<int>());
    }
    int pop() {
        std::pop_heap(data_.begin(), data_.end(), std::greater<int>());
        int value = data_.back();
        data_.pop_back();
        return value;
    }
    bool empty() const { return data_.empty(); }

  private:
    std::vector<int> data_;
};

int main() {
    MinHeap heap;
    for (int value : {5, 3, 8, 1, 4}) heap.push(value);
    std::vector<int> out;
    while (!heap.empty()) out.push_back(heap.pop());
    assert(std::is_sorted(out.begin(), out.end()));
    std::cout << "min heap ok\n";
    return 0;
}
