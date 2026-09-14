// A Tour of C++ -- standard containers.
#include <iostream>
#include <map>
#include <unordered_set>
#include <vector>

int main() {
    std::vector<int> numbers{5, 3, 1, 4, 2};
    std::map<std::string, int> scores{{"ada", 10}, {"grace", 9}};
    std::unordered_set<std::string> tags{"cpp", "systems", "interviews"};

    int sum = 0;
    for (int n : numbers) sum += n;

    std::cout << "sum=" << sum << " ada=" << scores.at("ada")
              << " tags=" << tags.size() << '\n';
    return 0;
}
