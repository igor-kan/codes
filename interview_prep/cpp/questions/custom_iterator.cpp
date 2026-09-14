// A minimal input iterator over a range of even numbers.
#include <iostream>
#include <iterator>
#include <vector>

class EvenRange {
  public:
    explicit EvenRange(int limit) : limit_(limit) {}
    struct Iterator {
        int current;
        using iterator_category = std::input_iterator_tag;
        using value_type = int;
        using difference_type = std::ptrdiff_t;
        int operator*() const { return current; }
        Iterator &operator++() { current += 2; return *this; }
        bool operator!=(const Iterator &other) const { return current != other.current; }
    };
    Iterator begin() const { return Iterator{0}; }
    Iterator end() const { return Iterator{limit_}; }

  private:
    int limit_;
};

int main() {
    std::vector<int> evens;
    for (int value : EvenRange(10)) evens.push_back(value);
    for (int value : evens) std::cout << value << ' ';
    std::cout << '\n';
    return 0;
}
