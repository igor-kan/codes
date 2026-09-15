// Module consumer.
import math;
#include <iostream>

int main() {
    std::cout << add(2, 3) << ' ' << multiply(4, 5) << ' '
              << stats::mean(2.0, 4.0) << '\n';
    return 0;
}
