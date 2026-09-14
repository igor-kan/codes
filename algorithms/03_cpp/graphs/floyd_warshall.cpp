// All-pairs shortest paths (Floyd-Warshall).
#include <algorithm>
#include <iostream>
#include <limits>
#include <vector>

constexpr int kInf = std::numeric_limits<int>::max() / 2;

std::vector<std::vector<int>> floyd_warshall(std::vector<std::vector<int>> dist) {
    const std::size_t n = dist.size();
    for (std::size_t k = 0; k < n; ++k)
        for (std::size_t i = 0; i < n; ++i)
            for (std::size_t j = 0; j < n; ++j)
                dist[i][j] = std::min(dist[i][j], dist[i][k] + dist[k][j]);
    return dist;
}

int main() {
    std::vector<std::vector<int>> graph{
        {0, 3, kInf, 7},
        {8, 0, 2, kInf},
        {5, kInf, 0, 1},
        {2, kInf, kInf, 0},
    };
    auto dist = floyd_warshall(graph);
    std::cout << "d[0][2]=" << dist[0][2] << " d[0][3]=" << dist[0][3] << '\n';
    return (dist[0][2] == 5 && dist[0][3] == 6) ? 0 : 1;
}
