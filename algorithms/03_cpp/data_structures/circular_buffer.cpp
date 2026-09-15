// Fixed-size circular buffer.
#include <cassert>
#include <iostream>
#include <vector>

class CircularBuffer {
  public:
    explicit CircularBuffer(std::size_t capacity) : data_(capacity) {}
    void push(int v) {
        data_[(head_ + size_) % data_.size()] = v;
        if (size_ < data_.size()) ++size_;
        else head_ = (head_ + 1) % data_.size();
    }
    int pop() {
        int v = data_[head_];
        head_ = (head_ + 1) % data_.size();
        --size_;
        return v;
    }
    std::size_t size() const { return size_; }

  private:
    std::vector<int> data_;
    std::size_t head_ = 0, size_ = 0;
};

int main() {
    CircularBuffer buffer(3);
    for (int i = 1; i <= 4; ++i) buffer.push(i);
    assert(buffer.pop() == 2 && buffer.pop() == 3 && buffer.pop() == 4);
    std::cout << "circular buffer ok\n";
    return 0;
}
