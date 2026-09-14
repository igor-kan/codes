// A Tour of C++ -- pointers, references and const.
#include <iostream>
#include <span>

void scale(std::span<int> values, int factor) {
    for (int &value : values) value *= factor;
}

int main() {
    int x = 5;
    int &ref = x;       // reference alias
    int *ptr = &x;      // pointer to x
    const int &cref = x;

    *ptr = 6;
    ref += 1;
    int data[] = {1, 2, 3};
    scale(data, 10);

    std::cout << x << ' ' << cref << ' ' << data[2] << '\n';
    return 0;
}
