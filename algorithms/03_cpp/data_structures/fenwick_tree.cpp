// Fenwick (binary indexed) tree for prefix sums.
#include <cassert>
#include <iostream>
#include <vector>

class FenwickTree {
  public:
    explicit FenwickTree(int n) : tree_(n + 1, 0) {}
    void add(int index, int delta) {
        for (++index; index < static_cast<int>(tree_.size()); index += index & -index)
            tree_[index] += delta;
    }
    int prefix_sum(int index) {
        int total = 0;
        for (++index; index > 0; index -= index & -index) total += tree_[index];
        return total;
    }
    int range_sum(int left, int right) { return prefix_sum(right) - prefix_sum(left - 1); }

  private:
    std::vector<int> tree_;
};

int main() {
    FenwickTree tree(8);
    int values[] = {1, 3, 5, 7, 9, 11};
    for (int i = 0; i < 6; ++i) tree.add(i, values[i]);
    assert(tree.prefix_sum(3) == 16);
    assert(tree.range_sum(2, 4) == 21);
    std::cout << "fenwick tree ok\n";
    return 0;
}
