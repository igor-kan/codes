// Treap (randomized balanced BST).
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <vector>

struct Node {
    int key, priority;
    Node *left = nullptr, *right = nullptr;
    explicit Node(int k) : key(k), priority(std::rand()) {}
};

void split(Node *root, int key, Node *&left, Node *&right) {
    if (!root) { left = right = nullptr; return; }
    if (root->key <= key) { split(root->right, key, root->right, right); left = root; }
    else { split(root->left, key, left, root->left); right = root; }
}

Node *merge(Node *a, Node *b) {
    if (!a || !b) return a ? a : b;
    if (a->priority > b->priority) { a->right = merge(a->right, b); return a; }
    b->left = merge(a, b->left);
    return b;
}

Node *insert(Node *root, int key) {
    Node *left, *right;
    split(root, key, left, right);
    return merge(merge(left, new Node(key)), right);
}

void inorder(Node *n, std::vector<int> &out) {
    if (!n) return;
    inorder(n->left, out);
    out.push_back(n->key);
    inorder(n->right, out);
}

int main() {
    std::srand(0);
    Node *root = nullptr;
    for (int key : {5, 2, 8, 1, 9, 3}) root = insert(root, key);
    std::vector<int> out;
    inorder(root, out);
    assert(out == std::vector<int>({1, 2, 3, 5, 8, 9}));
    std::cout << "treap ok\n";
    return 0;
}
