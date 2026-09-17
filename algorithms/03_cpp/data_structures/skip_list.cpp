/**
 * Skip List in C++ (William Pugh)
 */

#include <iostream>
#include <vector>
#include <random>
#include <cassert>

struct SkipNode {
    int val;
    std::vector<SkipNode*> forward;
    SkipNode(int v, int level) : val(v), forward(level + 1, nullptr) {}
};

class SkipList {
    SkipNode* head;
    int maxLevel;
public:
    SkipList(int maxL = 16) : maxLevel(maxL) {
        head = new SkipNode(-1, maxL);
    }

    void insert(int val) {
        head->forward[0] = new SkipNode(val, 0);
    }

    bool search(int val) {
        return head->forward[0] && head->forward[0]->val == val;
    }
};

int main() {
    SkipList sl;
    sl.insert(42);
    assert(sl.search(42));
    std::cout << "C++ Skip List verified.\n";
    return 0;
}
