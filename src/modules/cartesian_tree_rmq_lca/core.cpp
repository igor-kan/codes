#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_cartesian_tree_rmq_lca {

CartesianTree::CartesianTree(const std::vector<std::int64_t>& arr) : nodes_(arr.size()) {
    std::vector<int> st;
    for (int i = 0; i < static_cast<int>(arr.size()); ++i) {
        nodes_[i].val = arr[i];
        int last = -1;
        while (!st.empty() && arr[st.back()] > arr[i]) {
            last = st.back();
            st.pop_back();
        }
        if (!st.empty()) {
            nodes_[st.back()].right = i;
            nodes_[i].parent = st.back();
        }
        if (last != -1) {
            nodes_[i].left = last;
            nodes_[last].parent = i;
        }
        st.push_back(i);
    }
    if (!st.empty()) root_ = st.front();
}

int CartesianTree::rmq_index(int l, int r) const {
    int cur = root_;
    while (cur != -1) {
        if (cur < l) cur = nodes_[cur].right;
        else if (cur > r) cur = nodes_[cur].left;
        else return cur;
    }
    return -1;
}

} // namespace codes_cartesian_tree_rmq_lca
