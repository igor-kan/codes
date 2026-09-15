// Ranges algorithms with projections and custom comparators.
#include <algorithm>
#include <iostream>
#include <ranges>
#include <string>
#include <vector>

struct Employee {
    std::string name;
    int age;
};

int main() {
    std::vector<Employee> staff{{"Ada", 36}, {"Grace", 45}, {"Alan", 41}};
    std::ranges::sort(staff, {}, &Employee::age);

    auto names = staff | std::views::transform(&Employee::name)
                       | std::views::common;
    for (const auto &name : names) std::cout << name << ' ';
    std::cout << '\n';
    return 0;
}
