// Aho-Corasick multi-pattern matching.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

struct Node {
    std::array<int, 26> next;
    int fail = 0;
    std::vector<std::string> out;
    Node() { next.fill(-1); }
};

class AhoCorasick {
  public:
    AhoCorasick() { nodes_.emplace_back(); }

    void add(const std::string &pattern) {
        int node = 0;
        for (char ch : pattern) {
            int c = ch - 'a';
            if (nodes_[node].next[c] == -1) {
                nodes_[node].next[c] = static_cast<int>(nodes_.size());
                nodes_.emplace_back();
            }
            node = nodes_[node].next[c];
        }
        nodes_[node].out.push_back(pattern);
    }

    void build() {
        std::queue<int> queue;
        for (int c = 0; c < 26; ++c)
            if (nodes_[0].next[c] != -1) { nodes_[nodes_[0].next[c]].fail = 0; queue.push(nodes_[0].next[c]); }
        while (!queue.empty()) {
            int node = queue.front();
            queue.pop();
            for (int c = 0; c < 26; ++c) {
                int child = nodes_[node].next[c];
                if (child != -1) {
                    int fallback = nodes_[node].fail;
                    while (fallback && nodes_[fallback].next[c] == -1) fallback = nodes_[fallback].fail;
                    if (nodes_[fallback].next[c] != -1) fallback = nodes_[fallback].next[c];
                    nodes_[child].fail = fallback;
                    nodes_[child].out.insert(nodes_[child].out.end(),
                                             nodes_[fallback].out.begin(), nodes_[fallback].out.end());
                    queue.push(child);
                }
            }
        }
    }

    std::vector<std::string> search(const std::string &text) {
        std::vector<std::string> found;
        int node = 0;
        for (char ch : text) {
            int c = ch - 'a';
            while (node && nodes_[node].next[c] == -1) node = nodes_[node].fail;
            node = nodes_[node].next[c] == -1 ? 0 : nodes_[node].next[c];
            found.insert(found.end(), nodes_[node].out.begin(), nodes_[node].out.end());
        }
        return found;
    }

  private:
    std::vector<Node> nodes_;
};

int main() {
    AhoCorasick machine;
    for (const std::string &pattern : {"he", "she", "his", "hers"}) machine.add(pattern);
    machine.build();
    auto found = machine.search("ushers");
    assert(std::find(found.begin(), found.end(), "he") != found.end());
    assert(std::find(found.begin(), found.end(), "she") != found.end());
    std::cout << "aho-corasick ok\n";
    return 0;
}
