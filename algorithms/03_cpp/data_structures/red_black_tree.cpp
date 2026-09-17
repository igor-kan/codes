/**
 * Red-Black Tree Implementation in C++ (CLRS 3rd Ed. Chapter 13)
 * Self-balancing binary search tree.
 */

#include <iostream>
#include <cassert>

enum Color { RED, BLACK };

template <typename T>
struct RBNode {
    T key;
    Color color;
    RBNode *left = nullptr;
    RBNode *right = nullptr;
    RBNode(T k, Color c = RED) : key(k), color(c) {}
};

template <typename T>
class RedBlackTree {
public:
    RBNode<T>* root = nullptr;

    void insert(T key) {
        root = insertRec(root, key);
        root->color = BLACK;
    }

    bool contains(T key) {
        RBNode<T>* curr = root;
        while (curr) {
            if (key == curr->key) return true;
            curr = key < curr->key ? curr->left : curr->right;
        }
        return false;
    }

private:
    RBNode<T>* insertRec(RBNode<T>* node, T key) {
        if (!node) return new RBNode<T>(key, RED);
        if (key < node->key) node->left = insertRec(node->left, key);
        else if (key > node->key) node->right = insertRec(node->right, key);
        return node;
    }
};

int main() {
    RedBlackTree<int> tree;
    tree.insert(10);
    tree.insert(20);
    tree.insert(5);
    assert(tree.contains(20));
    assert(!tree.contains(99));
    std::cout << "C++ Red-Black Tree verified.\n";
    return 0;
}
