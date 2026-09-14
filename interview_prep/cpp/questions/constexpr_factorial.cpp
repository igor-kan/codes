// Compile-time factorial with static_assert verification.
#include <iostream>

consteval long factorial(int n) {
    long result = 1;
    for (int i = 2; i <= n; ++i) result *= i;
    return result;
}

static_assert(factorial(10) == 3'628'800);

int main() {
    std::cout << factorial(12) << '\n';
    return 0;
}
