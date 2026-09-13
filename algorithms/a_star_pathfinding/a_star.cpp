/**
 * A* Pathfinding Algorithm in C++
 * Uses std::priority_queue with Manhattan heuristic for optimal grid navigation.
 */

#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
#include <algorithm>
#include <cassert>

struct Point {
    int r, c;
    bool operator==(const Point& o) const { return r == o.r && c == o.c; }
    bool operator<(const Point& o) const {
        if (r != o.r) return r < o.r;
        return c < o.c;
    }
};

struct Node {
    Point pt;
    int f_score;
    int g_score;
    bool operator>(const Node& o) const {
        return f_score > o.f_score;
    }
};

int manhattan(Point a, Point b) {
    return std::abs(a.r - b.r) + std::abs(a.c - b.c);
}

std::vector<Point> a_star_grid(const std::vector<std::vector<int>>& grid, Point start, Point goal) {
    int rows = grid.size();
    int cols = grid[0].size();

    std::priority_queue<Node, std::vector<Node>, std::greater<Node>> pq;
    std::map<Point, int> g_score;
    std::map<Point, Point> came_from;

    g_score[start] = 0;
    pq.push({start, manhattan(start, goal), 0});

    const int dr[4] = {-1, 1, 0, 0};
    const int dc[4] = {0, 0, -1, 1};

    while (!pq.empty()) {
        Node top = pq.top();
        pq.pop();

        if (top.pt == goal) {
            std::vector<Point> path;
            Point curr = goal;
            path.push_back(curr);
            while (!(curr == start)) {
                curr = came_from[curr];
                path.push_back(curr);
            }
            std::reverse(path.begin(), path.end());
            return path;
        }

        if (top.g_score > g_score[top.pt]) continue;

        for (int i = 0; i < 4; ++i) {
            int nr = top.pt.r + dr[i];
            int nc = top.pt.c + dc[i];
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 0) {
                Point next = {nr, nc};
                int tentative_g = top.g_score + 1;
                if (g_score.find(next) == g_score.end() || tentative_g < g_score[next]) {
                    g_score[next] = tentative_g;
                    came_from[next] = top.pt;
                    pq.push({next, tentative_g + manhattan(next, goal), tentative_g});
                }
            }
        }
    }
    return {};
}

int main() {
    std::vector<std::vector<int>> grid = {
        {0, 0, 0, 0, 0},
        {1, 1, 1, 1, 0},
        {0, 0, 0, 0, 0},
        {0, 1, 1, 1, 1},
        {0, 0, 0, 0, 0}
    };

    auto path = a_star_grid(grid, {0, 0}, {4, 4});
    assert(path.size() == 17);
    std::cout << "[C++ A*] Path computed successfully: " << path.size() << " steps." << std::endl;
    return 0;
}
