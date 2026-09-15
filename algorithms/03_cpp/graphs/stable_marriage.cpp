// Gale-Shapley stable matching.
#include <cassert>
#include <iostream>
#include <queue>
#include <vector>

int main() {
    // Men and women indexed 0..2; preference lists of the opposite side.
    std::vector<std::vector<int>> menPref{{0, 1, 2}, {1, 0, 2}, {0, 1, 2}};
    std::vector<std::vector<int>> womenPref{{2, 1, 0}, {0, 1, 2}, {0, 1, 2}};
    int n = 3;
    std::vector<std::vector<int>> rank(n, std::vector<int>(n));
    for (int w = 0; w < n; ++w)
        for (int i = 0; i < n; ++i) rank[w][womenPref[w][i]] = i;

    std::queue<int> freeMen;
    for (int m = 0; m < n; ++m) freeMen.push(m);
    std::vector<int> next(n, 0), engagedTo(n, -1);
    while (!freeMen.empty()) {
        int m = freeMen.front(); freeMen.pop();
        int w = menPref[m][next[m]++];
        if (engagedTo[w] == -1) engagedTo[w] = m;
        else if (rank[w][m] < rank[w][engagedTo[w]]) {
            freeMen.push(engagedTo[w]);
            engagedTo[w] = m;
        } else freeMen.push(m);
    }
    assert((engagedTo == std::vector<int>{2, 0, 1}));
    std::cout << "stable marriage ok\n";
    return 0;
}
