#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

bool happyNumber(int n) {
    std::set<int> seen;
    while (n != 1 && seen.find(n) == seen.end()) {
        seen.insert(n);
        int next = 0;
        while (n > 0) { int digit = n % 10; next += digit * digit; n /= 10; }
        n = next;
    }
    return n == 1;
}

int main() {
    assert(happyNumber(19) && !happyNumber(2));
    std::cout << "202 happy number ok\n";
    return 0;
}
