// Segmented sieve of Eratosthenes.
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>

std::vector<int> simple_sieve(int limit) {
    std::vector<bool> prime(limit + 1, true);
    prime[0] = prime[1] = false;
    for (int i = 2; i * i <= limit; ++i)
        if (prime[i])
            for (int j = i * i; j <= limit; j += i) prime[j] = false;
    std::vector<int> primes;
    for (int i = 2; i <= limit; ++i)
        if (prime[i]) primes.push_back(i);
    return primes;
}

std::vector<int> segmented_sieve(int low, int high) {
    std::vector<int> base = simple_sieve(static_cast<int>(std::sqrt(high)) + 1);
    std::vector<bool> segment(high - low + 1, true);
    for (int prime : base) {
        int start = std::max(prime * prime, (low + prime - 1) / prime * prime);
        for (int value = start; value <= high; value += prime) segment[value - low] = false;
    }
    if (low <= 1) segment[0] = false;
    std::vector<int> primes;
    for (int i = 0; i <= high - low; ++i)
        if (segment[i]) primes.push_back(low + i);
    return primes;
}

int main() {
    auto primes = segmented_sieve(10, 30);
    assert((primes == std::vector<int>{11, 13, 17, 19, 23, 29}));
    std::cout << "segmented sieve ok\n";
    return 0;
}
