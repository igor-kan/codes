// Self-balancing AVL tree.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

struct Node {
    int key, height = 1;
    Node *left = nullptr, *right = nullptr;
    explicit Node(int k) : key(k) {}
};

int height(Node *n) { return n ? n->height : 0; }
void update(Node *n) { n->height = 1 + std::max(height(n->left), height(n->right)); }

Node *rotate_right(Node *y) {
    Node *x = y->left;
    y->left = x->right;
    x->right = y;
    update(y);
    update(x);
    return x;
}

Node *rotate_left(Node *x) {
    Node *y = x->right;
    x->right = y->left;
    y->left = x;
    update(x);
    update(y);
    return y;
}

Node *balance(Node *n) {
    update(n);
    int factor = height(n->left) - height(n->right);
    if (factor > 1) {
        if (height(n->left->left) < height(n->left->right)) n->left = rotate_left(n->left);
        return rotate_right(n);
    }
    if (factor < -1) {
        if (height(n->right->right) < height(n->right->left)) n->right = rotate_right(n->right);
        return rotate_left(n);
    }
    return n;
}

Node *insert(Node *n, int key) {
    if (!n) return new Node(key);
    if (key < n->key) n->left = insert(n->left, key);
    else if (key > n->key) n->right = insert(n->right, key);
    else return n;
    return balance(n);
}

void inorder(Node *n, std::vector<int> &out) {
    if (!n) return;
    inorder(n->left, out);
    out.push_back(n->key);
    inorder(n->right, out);
}

int main() {
    Node *root = nullptr;
    for (int key : {10, 20, 30, 40, 50, 25}) root = insert(root, key);
    std::vector<int> out;
    inorder(root, out);
    assert(std::is_sorted(out.begin(), out.end()));
    std::cout << "avl tree ok\n";
    return 0;
}
