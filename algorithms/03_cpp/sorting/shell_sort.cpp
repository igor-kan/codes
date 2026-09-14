// Shell sort with Ciura's gap sequence.
#include <algorithm>
#include <iostream>
#include <vector>

void shell_sort(std::vector<int> &values) {
    const std::vector<int> gaps{701, 301, 132, 57, 23, 10, 4, 1};
    for (int gap : gaps)
        for (std::size_t i = gap; i < values.size(); ++i) {
            int temp = values[i];
            std::size_t j = i;
            while (j >= static_cast<std::size_t>(gap) && values[j - gap] > temp) {
                values[j] = values[j - gap];
                j -= gap;
            }
            values[j] = temp;
        }
}

int main() {
    std::vector<int> data{12, 34, 54, 2, 3, 90, 45};
    shell_sort(data);
    for (int value : data) std::cout << value << ' ';
    std::cout << '\n';
    return std::is_sorted(data.begin(), data.end()) ? 0 : 1;
}
