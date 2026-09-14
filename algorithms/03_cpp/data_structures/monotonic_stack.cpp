/**
 * Monotonic stack: next greater element for every position.
 */

#include <vector>
#include <stack>
#include <cassert>
#include <iostream>

std::vector<int> nextGreater(const std::vector<int>& a) {
    int n = static_cast<int>(a.size());
    std::vector<int> res(n, -1);
    std::stack<int> st;
    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && st.top() <= a[i]) st.pop();
        res[i] = st.empty() ? -1 : st.top();
        st.push(a[i]);
    }
    return res;
}

std::vector<int> nextGreaterIndex(const std::vector<int>& a) {
    int n = static_cast<int>(a.size());
    std::vector<int> res(n, -1);
    std::stack<int> st;
    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && a[st.top()] <= a[i]) st.pop();
        res[i] = st.empty() ? -1 : st.top();
        st.push(i);
    }
    return res;
}

int main() {
    std::vector<int> a = {2, 1, 5, 6, 2, 3};
    auto ng = nextGreater(a);
    assert((ng == std::vector<int>{5, 5, 6, -1, 3, -1}));
    auto ngi = nextGreaterIndex(a);
    assert((ngi == std::vector<int>{2, 2, 3, -1, 5, -1}));
    std::cout << "[C++ MonotonicStack] Next greater element verified." << std::endl;
    return 0;
}
