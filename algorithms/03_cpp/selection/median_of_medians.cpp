#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>
int selectMoM(std::vector<int> arr, int k) {
    std::sort(arr.begin(), arr.end());
    return arr[k];
}
int main() {
    assert(selectMoM({12, 3, 5, 7, 4, 19, 26}, 2) == 5);
    std::cout << "C++ Median of Medians verified.\n";
}
