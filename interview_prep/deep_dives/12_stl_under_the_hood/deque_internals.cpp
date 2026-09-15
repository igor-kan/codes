// deque: constant-time push at both ends (map of fixed-size blocks).
#include <deque>
#include <iostream>

int main() {
    std::deque<int> dq;
    for (int i = 0; i < 5; ++i) dq.push_back(i);
    dq.push_front(-1);
    dq.push_back(5);
    for (int value : dq) std::cout << value << ' ';
    std::cout << "\nfront=" << dq.front() << " back=" << dq.back() << '\n';
    return 0;
}
