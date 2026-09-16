#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>

std::vector<std::string> fizzBuzz(int n) {
    std::vector<std::string> result;
    for (int value = 1; value <= n; ++value) {
        if (value % 15 == 0) result.push_back("FizzBuzz");
        else if (value % 3 == 0) result.push_back("Fizz");
        else if (value % 5 == 0) result.push_back("Buzz");
        else result.push_back(std::to_string(value));
    }
    return result;
}

int main() {
    assert((fizzBuzz(5) == std::vector<std::string>{"1", "2", "Fizz", "4", "Buzz"}));
    assert(fizzBuzz(15).back() == "FizzBuzz");
    std::cout << "412 fizz buzz ok\n";
    return 0;
}
